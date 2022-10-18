/**
 * @author Zhaonian Zou <znzou@hit.edu.cn>,
 * School of Computer Science and Technology,
 * Harbin Institute of Technology, China
 */

#include "storage.h"
#include "file_iterator.h"
#include "page_iterator.h"
#include "schema.h"
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include "exceptions/insufficient_space_exception.h"
#include "exceptions/page_not_pinned_exception.h"
using namespace std;


namespace badgerdb {

/*
Inserts a tuple into a relationship. This method has three parameters:

Tuple: the value of the tuple. We use string string to store tuples, but the contents of this tuple are not strings, which are byte sequences. You need to design the inner representation of tuples and implement it programmatically to read and write the contents of tuples.

File: handle to the data piece of the relationship.

Bufmgr: pointer to the buffer pool manager object.

Organize the new element group tuples according to the heap.
If the tuple is inserted successfully, the record number (recordid type) of the tuple is returned.
*/
RecordId HeapFileManager::insertTuple(const string& tuple,
                                      File& file,
                                      BufMgr* bufMgr) {
  // TODO
  Page* P;
  PageId pageId;
  RecordId recordId;
  for(FileIterator i = file.begin(); i != file.end(); ++i){//Traversing the pages of a file by using its iterator
    Page tmp = *i;
    pageId = tmp.page_number();//Get the ID of the traversed page according to the iterator
    if(pageId == Page::INVALID_NUMBER){//Page number not available
        break;
    }
    bufMgr->readPage(&file, pageId, P);//Get page object
    try{//Page has enough space to insert tuples
        recordId = P->insertRecord(tuple);//Get the recordid according to the insertrecord method of the page
        bufMgr->unPinPage(&file, pageId, true);//Set this page of the buffer pool to dirty
        return recordId;
    }catch(PageNotPinnedException e){
    }catch(InsufficientSpaceException e){
        bufMgr->unPinPage(&file, pageId, false);//Insufficient page space, write failed
    }
  }
  //Create a new page store tuple
  bufMgr->allocPage(&file, pageId, P);
  recordId = P->insertRecord(tuple);//Get the recordid according to the insertrecord method of the page
  bufMgr->unPinPage(&file,pageId,true);//Set this page of the buffer pool to dirty
  return recordId;
}

/*
Delete a tuple from the relationship. This method has three parameters.
The last two parameters, file and bufmgr, are the same as the same name parameters of inserttuple method.
The rid parameter of the deletetuple method is the record number (recordid type) of the tuple to be deleted.
*/
void HeapFileManager::deleteTuple(const RecordId& rid,
                                  File& file,
                                  BufMgr* bugMgr) {
  // TODO
  Page* P;
  PageId pageId = rid.page_number;
  bugMgr->readPage(&file,pageId,P);//Locate the page where you want to delete the record
  P->deleteRecord(rid);
}

/*
Convert tuples to bits sequences
The arrinfo parameter represents the property value of the insert, and Len represents the maxsize of the property value
*/
string BitsSequence(char* attInfo, int len){
    int flag = 1;
    stringstream ans;
    for (int i = 0; i < len; i++){
        for (int j = 0; j < sizeof(char)*8; j++){
            if(*(attInfo + i) != '\0' && flag == 1){
				//Bit number if the i-th bit of arrinfo is not '\ 0', 
				//then it will be bited and operated with 0x80. 
				//0x80 is 10000000. If 0x80 is cycled once, move the j-bit to the right. 
				//The purpose is to extract the bit value of attinfo bit by bit
                if(*(attInfo + i) & (0X80 >> j)){//0X80->10000000
                    ans << "1";
                }
                else{
                    ans << "0";
                }
            }
			//If the end is reached, then add x at the back
            else{
                flag = 0;
                ans << "X";
            }
        }
    }
    return ans.str();
}

/*
This method creates a tuple and returns it according to the SQL insert statement of input and the mode of insert relation.
*/
string HeapFileManager::createTupleFromSQLStatement(const string& sql,
                                                    const Catalog* catalog) {
  // TODO
  vector<string> Tname = split(sql, " ");
  string tableName = Tname[2];//get tablename
  stringstream bitsSeq;//result Bits Sequence
  stringstream attrsBitsSeq;//attribute bits sequence
  TableId tId = catalog->getTableId(tableName);
  stringstream tmp1;
  tmp1<<tId<<',';//After tableid information
  string tmp_1;
  tmp1>>tmp_1;
  bitsSeq<<BitsSequence((char*)tmp_1.c_str(), 5); //tableid write header file
  TableSchema tSchema = catalog->getTableSchema(tId);
  unsigned int froS = sql.find_first_of("(");
  unsigned int backS = sql.find_last_of(")");
  const string attrsString = sql.substr(froS + 1, backS - (froS + 1));
  int bSeqSize = 0;
  vector<string>attrsV = split(attrsString, ",");//get attribute value;
  int index = 0;
  for(vector<string>::iterator i = attrsV.begin();i!= attrsV.end();++i){
      int MaxSize = tSchema.getAttrMaxSize(index);//Traverse the values of different attributes, and get the maxsize of attributes from the table schema according to the values
      bSeqSize += MaxSize*8;
      string tmp = *i;
      for(int k = 0; k < tmp.length();k++){
        if(tmp[k] == ' ' || tmp[k] == '\''){
            tmp.erase(k,1);
            k--;
        }
      }
      tmp += ',';
      string valueTmp = BitsSequence((char*)tmp.data(), MaxSize+1);
      attrsBitsSeq<<valueTmp;
      index++;
  }
  bSeqSize += 64;//Add 8 bytes to represent the length of the tuple header (ID and size)
  stringstream tmp2;
  tmp2<<bSeqSize<<',';
  string tmp_2;
  tmp2>>tmp_2;
  bitsSeq<<BitsSequence((char*)tmp_2.c_str(), 5);//Add size information
  bitsSeq<<attrsBitsSeq.str();//Add attribute information
  return bitsSeq.str();
}
}  // namespace badgerdb
