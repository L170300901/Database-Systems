/**
 * @author See Contributors.txt for code contributors and overview of BadgerDB.
 *
 * @section LICENSE
 * Copyright (c) 2012 Database Group, Computer Sciences Department, University of Wisconsin-Madison.
 */

#include <memory>
#include <iostream>
#include "buffer.h"
#include "exceptions/buffer_exceeded_exception.h"
#include "exceptions/page_not_pinned_exception.h"
#include "exceptions/page_pinned_exception.h"
#include "exceptions/bad_buffer_exception.h"
#include "exceptions/hash_not_found_exception.h"

namespace badgerdb { 

/*
This is the class constructor. 
Allocates an array for the buffer pool with bufs page frames and a corresponding BufDesc table. 
The way things are set up all frames will be in the clear state when the buffer pool is allocated. 
The hash table will also start out in an empty state. We have provided the constructor.
*/ 
BufMgr::BufMgr(std::uint32_t bufs)
	: numBufs(bufs) {
	bufDescTable = new BufDesc[bufs];

  for (FrameId i = 0; i < bufs; i++) 
  {
  	bufDescTable[i].frameNo = i;
  	bufDescTable[i].valid = false;
  }

  bufPool = new Page[bufs];

	int htsize = ((((int) (bufs * 1.2))*2)/2)+1;
  hashTable = new BufHashTbl (htsize);  // allocate the buffer hash table

  clockHand = bufs - 1;
}


/*
Flushes out all dirty pages and deallocates the buffer pool and the BufDesc table.
*/
BufMgr::~BufMgr() {
	//Clean dirty pages
	for(FrameId i = 0; i < numBufs; i++){
		if(bufDescTable[i].dirty == true){
			flushFile(bufDescTable[i].file);
		}
	} 
	//release
	delete[] bufDescTable;
	delete[] bufPool;
	delete hashTable;
}

/*
Advance clock to next frame in the buffer pool.
*/
void BufMgr::advanceClock()
{
	clockHand += 1;
	if(clockHand > numBufs - 1){
		clockHand = clockHand % numBufs;   //Clock reset
	}
}
/*
Allocates a free frame using the clock algorithm; 
if necessary, writing a dirty page back to disk. 
Throws BufferExceededException if all buffer frames are pinned. 
This private method will get called by the readPage() and allocPage() methods described below. 
Make sure that if the buffer frame allocated has a valid page in it, 
you remove the appropriate entry from the hash table.
*/
void BufMgr::allocBuf(FrameId & frame) 
{
	unsigned pinnedNum = 0;//number of pinned frame
	while(1){
		advanceClock();
		//See the experiment instruction for the logic flow chart
		//The code is compiled according to the process of experiment instruction 
		if(!bufDescTable[clockHand].valid){//Return directly when false
			frame = bufDescTable[clockHand].frameNo;
			return;
		}
		if(bufDescTable[clockHand].refbit){//Recently used or not
			bufDescTable[clockHand].refbit = false;
			continue;
		}
		if(bufDescTable[clockHand].pinCnt > 0){//pinned or not 
			pinnedNum += 1;
			if(pinnedNum >= numBufs){//Call bufferexceededexception() if all pinned
				throw BufferExceededException();
			} 
			else{
				continue;
			}
		}
		if(bufDescTable[clockHand].dirty){//Dirty page or not 
			bufDescTable[clockHand].file->writePage(bufPool[clockHand]);//Write back to disk 
			bufDescTable[clockHand].dirty = false;
		} 
		frame = bufDescTable[clockHand].frameNo;
		
		//Delete the previous page of the selected free frame first
		//Remove from hashtable
		try{
			hashTable->remove(bufDescTable[clockHand].file, bufDescTable[clockHand].pageNo); 
		} catch(HashNotFoundException e){}
		break;
	}
}


/*
First check whether the page is already in the buffer pool by invoking the lookup() method, 
which may throw HashNotFoundException when page is not in the buffer pool, 
on the hashtable to get a frame number. 
There are two cases to be handled depending on the outcome of the lookup() call:
Case 1: Page is not in the buffer pool.
Case 2: Page is in the buffer pool.
*/	
void BufMgr::readPage(File* file, const PageId pageNo, Page*& page)
{
	FrameId FI;
	//Case 2
	try{
		hashTable->lookup(file, pageNo, FI);//Find the frame of page
		 bufDescTable[FI].refbit = true;
		 bufDescTable[FI].pinCnt += 1;
		 page = bufPool + FI;//Return pointer
		
	}catch(HashNotFoundException e){
		//Case 1
		allocBuf(FI);//distribution
		bufPool[FI] = file->readPage(pageNo);//Read to cache pool
		hashTable->insert(file, pageNo, FI);//Add to hashtable
		bufDescTable[FI].Set(file, pageNo);//Set() 
		page = bufPool + FI; //Return pointer
	}
}


/*
Decrements the pinCnt of the frame containing (file, PageNo) and, 
if dirty == true, sets the dirty bit. 
Throws PAGENOTPINNED if the pin count is already 0. 
Does nothing if page is not found in the hash table lookup.
*/
void BufMgr::unPinPage(File* file, const PageId pageNo, const bool dirty) 
{
	FrameId FI;
	try{
		hashTable->lookup(file, pageNo, FI);//In hashtable
		if(bufDescTable[FI].pinCnt == 0){
			throw PageNotPinnedException("PinCnt is 0 now!", pageNo, FI);
		} 
		bufDescTable[FI].pinCnt -= 1;
		if(dirty){
			bufDescTable[FI].dirty = true;
		}
	} catch(HashNotFoundException e){}//Not in hashtable 
}

/*
Should scan bufTable for pages belonging to the file. 
For each page encountered it should: (a) if the page is dirty, 
call file->writePage() to flush the page to disk and then set the dirty bit for the page to false, 
(b) remove the page from the hashtable (whether the page is clean or dirty) and (c) invoke the Clear() method of BufDesc for the page frame.
Throws PagePinnedException if some page of the file is pinned. 
Throws BadBufferException if an invalid page belonging to the file is encountered.
*/
void BufMgr::flushFile(const File* file) 
{
	for (FrameId i = 0; i < numBufs; i++){
		if(bufDescTable[i].file == file){//Find the frame that belongs to the file 
			if(!bufDescTable[i].valid){// Invalid page belonging to the file
				throw BadBufferException(i, bufDescTable[i].dirty, bufDescTable[i].valid, bufDescTable[i].refbit);
			}
			if(bufDescTable[i].pinCnt > 0){//A page of the file is pinned
				throw PagePinnedException("The page is pinned now!", bufDescTable[i].pageNo, i);
			}
			if(bufDescTable[i].dirty){
				bufDescTable[i].file->writePage(bufPool[i]);//Refresh page to disk
				bufDescTable[i].dirty = false; 
			}
			hashTable->remove(file,bufDescTable[i].pageNo);//Remove page from hash table
			bufDescTable[i].Clear();// Call the clear() method of bufDesc
		}
	}
}

/*
The first step in this method is to to allocate an empty page in the specified file by invoking the file->allocatePage() method. 
This method will return a newly allocated page. Then allocBuf() is called to obtain a buffer pool frame. 
Next, an entry is inserted into the hash table and Set() is invoked on the frame to set it up properly. 
The method returns both the page number of the newly allocated page to the caller via the pageNo parameter and a pointer to the buffer frame allocated for the page via the page parameter.
*/
void BufMgr::allocPage(File* file, PageId &pageNo, Page*& page) 
{
	Page p = file->allocatePage();//Assign new page
	FrameId FI;
	allocBuf(FI);//Assign frame
	bufPool[FI] = p;
	pageNo = p.page_number();
	hashTable->insert(file, pageNo, FI);//Insert hashtable 
	bufDescTable[FI].Set(file, pageNo);//Set() 
	page = bufPool + FI; 
}

/*
This method deletes a particular page from file. 
Before deleting the page from file, 
it makes sure that if the page to be deleted is allocated a frame in the buffer pool, 
that frame is freed and correspondingly entry from hash table is also removed.
*/
void BufMgr::disposePage(File* file, const PageId PageNo)
{
    FrameId FI;
    try{
    	hashTable->lookup(file, PageNo, FI);//Find the frame where the deleted page is located 
    	hashTable->remove(file, PageNo); //Delete hashtable related entries 
		bufDescTable[FI].Clear();//Release frame 
	}catch(HashNotFoundException e){}
	file->deletePage(PageNo);//Delete page of file 
}


void BufMgr::printSelf(void) 
{
  BufDesc* tmpbuf;
	int validFrames = 0;
  
  for (std::uint32_t i = 0; i < numBufs; i++)
	{
  	tmpbuf = &(bufDescTable[i]);
		std::cout << "FrameNo:" << i << " ";
		tmpbuf->Print();

  	if (tmpbuf->valid == true)
    	validFrames++;
  }

	std::cout << "Total Number of Valid Frames:" << validFrames << "\n";
}

}
