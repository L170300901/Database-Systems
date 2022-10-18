/**
 * @author Zhaonian Zou <znzou@hit.edu.cn>,
 * School of Computer Science and Technology,
 * Harbin Institute of Technology, China
 */


#include "executor.h"

#include <functional>
#include <string>
#include <iostream>
#include <ctime>
#include <vector>
#include "schema.h"
#include "storage.h"
#include "file_iterator.h"
#include "page_iterator.h"
#include <iomanip>
#include <sstream>
#include <cstring>
#include <cmath>


using namespace std;
static string JoinAttr;//connection properties name
std::multimap<string,string> JoinAttrs;//Save connection properties and corresponding tuples
namespace badgerdb {


/*
Translation bits sequence
*/
string translateBitsSeq(const string& bitsSeq){
    string attrV;
    stringstream ans;
    for(int i = 0; i < bitsSeq.length(); i++){
        if(bitsSeq[i] != 'X'){//Get bits sequence without 'x'.
            attrV += bitsSeq[i];
        }
    }
    int index = 0;
    int tmp = 0;
    for (int i = 0; i < attrV.length()/8; i++){
        index = 0;
        for (int j = 7; j >= 0; j--){
            if(attrV[j + i*8] == '1'){
                tmp += pow(2.0, index);//Calculate the value of binary number from the lowest position
            }
            index++;
        }
        char Attrvalue = char(tmp);//Decimal to character
        ans << Attrvalue;
        tmp = 0;
    }
    return ans.str();
}

/*
Compare file sizes
True if L is smaller
*/
bool compareLandR(File L,File R){
    int indexL = 0;
    int indexR = 0;
    FileIterator iterL = L.begin();
    FileIterator iterR = R.begin();
    ///ͳ��file1
    while(iterL!=L.end())
    {
        indexL++;
        iterL++;
    }
    ///ͳ��file2
    while(iterR!=R.end())
    {
        indexR++;
        iterR++;
    }
    return indexL <= indexR;
}

/*
You need to implement the tablescanner:: print() function to print tuples in the table.
The specific print format is defined by you.
You can refer to the tuple output format of DBMS such as MySQL and postgressql.
*/
void TableScanner::print() const {
  // Printer the contents of the table
  // Iterate through all pages in the file.
  File file = TableScanner::tableFile;
  BufMgr* buf = TableScanner::bufMgr;
  buf->flushFile(&tableFile);//Brush the document once
  FileIterator iterFile = file.begin();
  PageId pageBeginId = (*iterFile).page_number();//Get pageid from iterator
  TableSchema tableSch = TableScanner::tableSchema;
  cout<<"TableName is : "<<tableSch.getTableName()<<endl;
  if(tableSch.isTempTable()){
  	cout<<"Is it TempTable : TRUE"<<endl;
  }
  if(!tableSch.isTempTable()){
  	cout<<"Is it TempTable : FALSE"<<endl;
  }
  cout<<"The number of attribute is : "<<tableSch.getAttrCount()<<endl;
  stringstream attrsNS;
  stringstream edge;
  edge<<"#";
  attrsNS<<"\t";
  for(int i = 0; i < tableSch.getAttrCount(); i++){
        string attrN = tableSch.getAttrName(i);
        attrsNS<<attrN<<"\t\t";
        edge<<"---------------#";
  }
  cout<<edge.str()<<endl;
  cout<<attrsNS.str()<<endl;
  cout<<edge.str()<<endl;
  while(pageBeginId != 0){//Jump out when pageid equals 0
    Page* page;
    buf->readPage(&file, pageBeginId, page);//Get page object
    PageId pageid = page->page_number();
    SlotId slotid = page->begin().getNextUsedSlot(0);
    while(slotid != 0){
        stringstream attrV;
        RecordId recordid = {pageid, slotid};//Build recordid based on pageid and slotid
        slotid = page->begin().getNextUsedSlot(slotid);
        string bitsSeq = page->getRecord(recordid);//Get bits sequence of tuple through recordid
        string tupleTmp = translateBitsSeq(bitsSeq);
        attrV<<"\t";
        vector<string> attrs = split(tupleTmp, ",");
        int index = 0;
        for (vector<string>::iterator i = attrs.begin();i!= attrs.end();++i){
            if(index >= 2){
                string A = *i;
                attrV<<A<<"\t\t";
            }
            index++;
        }
        cout<<attrV.str()<<endl;
    }
    pageBeginId = (*iterFile).next_page_number();
    iterFile++;
  }
  cout<<edge.str()<<endl;
}

    JoinOperator::JoinOperator(const File& leftTableFile,
                               const File& rightTableFile,
                               const TableSchema& leftTableSchema,
                               const TableSchema& rightTableSchema,
                               Catalog* catalog,
                               BufMgr* bufMgr)
            : leftTableFile(leftTableFile),
              rightTableFile(rightTableFile),
              leftTableSchema(leftTableSchema),
              rightTableSchema(rightTableSchema),
              resultTableSchema(
                      createResultTableSchema(leftTableSchema, rightTableSchema)),
              catalog(catalog),
              bufMgr(bufMgr),
              isComplete(false) {
            if(compareLandR(leftTableFile,rightTableFile)){//Tables with fewer pages of files as base tables
                resultTableSchema = createResultTableSchema(leftTableSchema, rightTableSchema);
            }
			else{
				resultTableSchema = createResultTableSchema(rightTableSchema, leftTableSchema);
			}
    }


/*
Create a schema for the result relationship based on the lefttableschema and righttableschema.

Note that this is a natural connection.
*/
TableSchema JoinOperator::createResultTableSchema(
    const TableSchema& leftTableSchema,
    const TableSchema& rightTableSchema) {
  vector<Attribute> attrs;
  // TODO: add attribute definitions
  int numL = leftTableSchema.getAttrCount();
  int numR = rightTableSchema.getAttrCount();
  //put all the properties of one of the tables into 
  for (int i = 0; i < numL; i++){
  	string name = leftTableSchema.getAttrName(i);
	DataType attrType = leftTableSchema.getAttrType(i);
	int maxSize = leftTableSchema.getAttrMaxSize(i);
	bool isNotNull = leftTableSchema.isAttrNotNull(i);
	bool isUnique = leftTableSchema.isAttrUnique(i);
	Attribute tmp1((string &)name, (DataType &)attrType, maxSize, isNotNull, isUnique);
  	attrs.push_back(tmp1);
  }
  //Traverse another table's attribute. 
  //If it is equal to an added attribute, the attribute will not be added, and the attribute is a common attribute. 
  //Pay the name of the attribute to the global variable declared at the beginning.
  for (int i = 0; i < numR; i++){
  	int flag = 0;
  	//Properties found for connection
	for(vector<Attribute>::iterator it = attrs.begin();it!= attrs.end();++it){
		Attribute t = *it;
		if((string &)t.attrName == (string &)rightTableSchema.getAttrName(i)){
			flag = 1;
			JoinAttr = rightTableSchema.getAttrName(i);//common attribute
			break;
		}
	}
	if(flag == 0){
        string name = rightTableSchema.getAttrName(i);
        DataType attrType = rightTableSchema.getAttrType(i);
        int maxSize = rightTableSchema.getAttrMaxSize(i);
        bool isNotNull = rightTableSchema.isAttrNotNull(i);
        bool isUnique = rightTableSchema.isAttrUnique(i);
        Attribute tmp2((string &)name, (DataType &)attrType, maxSize, isNotNull, isUnique);
		attrs.push_back(tmp2);
	}
  }
  return TableSchema("JoinResultTABLE", attrs, true);
}


/*
Read the table into the buffer and record the information
*/
void writeToBuf(Page* page, BufMgr* buf, const TableSchema& tableSche){
	//Get pageid and start slot ID from page object
    PageId pageid = page->page_number();
    SlotId slotid = page->begin().getNextUsedSlot(0);
    int attrSum = tableSche.getAttrCount();
    string attrStr[attrSum];
    int JoinAttrNum = 0;
	//Get the total number of properties and traverse to find the subscript of the common properties of the two tables
    for(int i = 0; i < attrSum; i++){//Subscript for record connection properties
        if(tableSche.getAttrName(i) == JoinAttr){
            JoinAttrNum = i;
        }
    }
    while(slotid != 0){
        stringstream attrV;
        RecordId recordid = {pageid, slotid};//Build the recordid to get the byte sequence of the tuple
        slotid = page->begin().getNextUsedSlot(slotid);
        string bitsSeq = page->getRecord(recordid);
        string tupleTmp = translateBitsSeq(bitsSeq);
        vector<string> attrs = split(tupleTmp, ",");
        int index = 0;
        for (vector<string>::iterator i = attrs.begin();i!= attrs.end();++i){
            if(index >= 2 && i!=attrs.end()-1){
                string A = *i;
                attrStr[index - 2] = A;
                attrV<<A<<",";
            }
            index++;
        }
        JoinAttrs.insert(make_pair(attrStr[JoinAttrNum], attrV.str()));//Write the key value pair of the common attribute value -- connection tuple to the global variable joinattrs
    }
}

/*
join the page with the data in the buffer
Returns the number of tuples in the join table
*/
int join(File file,Page* page,const TableSchema& resultable,const TableSchema& tableSche, Catalog *catalog,BufMgr* bufMgr){
    int ResultTupleNum = 0;
	//Get pageid and start slot ID from page object
    PageId pageid = page->page_number();
    SlotId slotid = page->begin().getNextUsedSlot(0);
    int attrSum = tableSche.getAttrCount();
    string attrStr[attrSum];
    int JoinAttrNum = 0;
	//Get the total number of properties and traverse to find the subscript of the common properties of the two tables
    for(int i = 0; i < attrSum; i++){//Subscript for record connection properties
        if(tableSche.getAttrName(i) == JoinAttr){
            JoinAttrNum = i;
        }
    }
    while(slotid != 0){
        //Get tuple information in page one by one
        stringstream attrV;
        RecordId recordid = {pageid, slotid};//Build the recordid to get the byte sequence of the tuple
        slotid = page->begin().getNextUsedSlot(slotid);
        string bitsSeq = page->getRecord(recordid);
        string tupleTmp = translateBitsSeq(bitsSeq);
        vector<string> attrs = split(tupleTmp, ",");
        int index = 0;
        for (vector<string>::iterator i = attrs.begin();i!= attrs.end();++i){
            if(index >= 2 && i!=attrs.end()-1){
				//Traversal writes property values to string stream variables in turn
                string A = *i;
                attrStr[index - 2] = A;
                attrV<<A;
            }
            index++;
        }

        //Compare the connection attribute values one by one and perform the connection operation
        string tmp = attrStr[JoinAttrNum];
        if(JoinAttrs.count(tmp) != 0){//use the count method to see if the common attribute value is in joinattrs
            auto tupleAvail = JoinAttrs.find(tmp);
			//Iterate through all key values as key value pairs of common attribute values, write its value to a stringstream variable, and then write the tuple value in the previous page
            for(int i = 0; i < JoinAttrs.count(tmp); i++,tupleAvail++){
                    string s = tupleAvail->second;
                    stringstream atr_value_result;
                    atr_value_result<<s<<attrV.str();
                    atr_value_result.seekp(-1, atr_value_result.cur);
                    stringstream result;
                    result<<"INSERT INTO " <<resultable.getTableName()<<  " VALUES (" << atr_value_result.str()<<");";//Building SQL statements
                    string tuple = HeapFileManager::createTupleFromSQLStatement(result.str(), catalog);
                    HeapFileManager::insertTuple(tuple, file, bufMgr);
                    ResultTupleNum++;
            }
        }
    }
    bufMgr->flushFile(&file);//Write result file
    return ResultTupleNum;
}

    void JoinOperator::printRunningStats() const {
        cout << "# Result Tuples: " << numResultTuples << endl;
        cout << "# Used Buffer Pages: " << numUsedBufPages << endl;
        cout << "# I/Os: " << numIOs << endl;
    }

/*
In order to implement the join algorithm, this experiment declares the onepassjoinoperator class.
Onepassjoinoperator inherits the joinoperator class.
You need to implement the onepassjoinoperator:: executor method.
*/
bool OnePassJoinOperator::execute(int numAvailableBufPages, File& resultFile) {
  if (isComplete)
    return true;
  catalog->addTableSchema(resultTableSchema,resultTableSchema.getTableName());
  TableSchema resultTableSche = resultTableSchema;
  File fileL = leftTableFile;
  File fileR = rightTableFile;
  BufMgr* buf = bufMgr;
  TableSchema tableScheL = leftTableSchema;
  TableSchema tableScheR = rightTableSchema;
  numResultTuples = 0;
  numUsedBufPages = 0;
  numIOs = 0;
  if(compareLandR(fileL, fileR)){//Make sure the right file is smaller
    fileL = rightTableFile;
    fileR = leftTableFile;
    tableScheL = rightTableSchema;
    tableScheR = leftTableSchema;
  }
  //Read the smaller table into buffer first
  FileIterator iterR = fileR.begin();
  PageId startIdR = (*iterR).page_number();
  JoinAttrs.clear();//In order not to affect subsequent operations, first clear the global variable joinattrs
  while(startIdR != 0){//Iterate over smaller table files with iterators
    //Read all pages of the table file into the buffer pool
	Page* p;
    buf->readPage(&fileR, startIdR, p);
    numIOs++;
    writeToBuf(p, buf, tableScheR);//Write it to the buffer pool and record the common attribute value -- the key value pair of the tuple containing the value
    numUsedBufPages++;
    startIdR = (*iterR).next_page_number();
    iterR++;
  }
  //Read in another table to start connection
  FileIterator iterL = fileL.begin();
  PageId startIdL = (*iterL).page_number();
  //Iterator is used to traverse the large table file, read the pages into the buffer pool in turn, and connect this page with each page of the smaller table file
  while(startIdL != 0){
    Page* p;
    buf->readPage(&fileL, startIdL, p);
    numIOs++;
    numResultTuples += join(resultFile, p, resultTableSche, tableScheL, catalog, buf);
    startIdL = (*iterL).next_page_number();
    iterL++;
  }
  numUsedBufPages++;
  isComplete = true;
  return true;
}

/*
In order to implement the block based nested join algorithm, this experiment declares the nestedloopjoinoperator class.
Nestedloopjoinoperator inherits the joinoperator class.
You need to implement the nestedloopjoinoperator:: executor method.
*/
bool NestedLoopJoinOperator::execute(int numAvailableBufPages, File& resultFile) {
  if (isComplete)
    return true;
  catalog->addTableSchema(resultTableSchema,resultTableSchema.getTableName());
  TableSchema resultTableSche = resultTableSchema;
  File fileL = leftTableFile;
  File fileR = rightTableFile;
  BufMgr* buf = bufMgr;
  TableSchema tableScheL = leftTableSchema;
  TableSchema tableScheR = rightTableSchema;
  numResultTuples = 0;
  numUsedBufPages = 0;
  numIOs = 0;
  if(compareLandR(fileL, fileR)){//Make sure the right file is smaller
    fileL = rightTableFile;
    fileR = leftTableFile;
    tableScheL = rightTableSchema;
    tableScheR = leftTableSchema;
  }
  // TODO: Execute the join algorithm
  int numUsedR = numAvailableBufPages - 1;//The M-1 block of the smaller file needs to be written to the buffer pool. M is the number of pages available in the buffer pool
  FileIterator iterR = fileR.begin();
  JoinAttrs.clear();//In order not to affect subsequent operations, first clear the global variable joinattrs
  
  while(iterR != fileR.end()){
	  //Loop through the smaller table file and write M-1 pages to the buffer pool
	for (int i = 0; i < numUsedR&&iterR!=fileR.end();i++,iterR++){
		PageId pageid = (*iterR).page_number();
		Page* p;
		bufMgr->readPage(&fileR, pageid, p);
		numUsedBufPages++;
		numIOs++;
		writeToBuf(p,bufMgr,tableScheR);//Write it to the buffer pool and record the common attribute value -- the key value pair of the tuple containing the value
	}

	FileIterator iterL = fileL.begin();
	PageId startid = (*iterL).page_number();
	////Iterator is used to traverse the large table file, read the pages into the buffer pool in turn, and connect this page with each page of the smaller table file
	while(startid != 0){
		Page* p;
		bufMgr->readPage(&fileL, startid, p);
		numIOs++;
		numResultTuples += join(resultFile, p, resultTableSche, tableScheL,catalog, bufMgr);
		startid = (*iterL).next_page_number();
		iterL++;
	}
	JoinAttrs.clear();//In order not to affect subsequent operations, first clear the global variable joinattrs
  }
  numUsedBufPages++;
  isComplete = true;
  return true;
}

    BucketId GraceHashJoinOperator::hash(const string& key) const {
        std::hash<string> strHash;
        return strHash(key) % numBuckets;
    }

    bool GraceHashJoinOperator ::execute(int numAvailableBufPages, File& resultFile) {
        if (isComplete)
            return true;

        numResultTuples = 0;
        numUsedBufPages = 0;
        numIOs = 0;
        // TODO: Execute the join algorithm
        isComplete = true;
        return true;
    }
}