/**
 * @author Zhaonian Zou <znzou@hit.edu.cn>,
 * School of Computer Science and Technology,
 * Harbin Institute of Technology, China
 */

#include "schema.h"
#include <vector>
#include <string>
#include <stdlib.h>
#include <iostream>
using namespace std;

/*
Cut string by specified character: returns vector type variable
*/
vector <string> split(const string& cutting, string sign){
	vector<string> ans;
	unsigned int indexFro = 0;
	unsigned int indexBack = 0;
	//Traverse cutting. 
	//If sign is encountered, add the substring before the sign to the vector traversal
	while(indexBack < cutting.length()){
		if(cutting[indexBack] == sign[0]){
			ans.push_back(cutting.substr(indexFro, indexBack-indexFro));
			indexFro = indexBack + 1;
	    }
	    indexBack++;
	    if(indexBack == cutting.length()){
	    	ans.push_back(cutting.substr(indexFro, indexBack-indexFro));
		}
	}
	//finally get the segmentation result
	return ans;
}

namespace badgerdb {


/*
According to the input string parameter SQL,
create the object of tableschema class and return the pointer of the object.
Input parameter SQL is the complete SQL CREATE TABLE statement string.
Property type in CREATE TABLE statement can only be int, char or varchar,
and property integrity constraint can only be not null or unique
*/
TableSchema TableSchema::fromSQLStatement(const string& sql) {
  string tableName;
  vector<Attribute> attrs;
  bool isTemp = false;
  // TODO: create attribute definitions from sql
  vector<string> aName = split(sql, " ");//First split the input SQL statement by the space
  tableName = aName[2];//The name of table is the third value of vector variable after segmentation
  //Temporary table if the name contains "#" or "##"
  if(aName[2].find("#",0)!=aName[2].npos || aName[2].find("##",0)!=aName[2].npos){
    isTemp = true;
  }
  //get attribute
  unsigned int froS = sql.find_first_of("(");
  unsigned int backS = sql.find_last_of(")");
  const string attrsString = sql.substr(froS + 1, backS - (froS + 1));
  vector<string>attrV = split(attrsString, ",");//Divide the attribute according to "," to get the definition of each attribute value
  enum DataType{INT,CHAR,VARCHAR};
  //push one by one
  for(vector<string>::iterator i = attrV.begin();i!= attrV.end();++i){
        string tmp = *i;
        if(tmp[0] == ' '){
            tmp = tmp.substr(1, tmp.length()-1);
        }
        vector<string>attrName = split(tmp, " ");
        string Aname = attrName[0];//The first one in the vector is the attribute name according to the space division
        DataType attrType;
        int maxSize = 0;
        bool isNotNull = false;
        bool isUnique = false;
        if(tmp.find("INT") != tmp.npos){
            attrType = INT;
            maxSize = 4;
        }
        if(tmp.find("CHAR") != tmp.npos){
            attrType = INT;
            int t = attrName[1].length();
            string S = attrName[1].substr(5, t-6);
            maxSize = atoi(S.data());
        }
        if(tmp.find("VARCHAR") != tmp.npos){
            attrType = INT;
            int t = attrName[1].length();
            string S = attrName[1].substr(8, t-9);
            maxSize = atoi(S.data());
        }
        if(tmp.find("NULL") != tmp.npos){
            isNotNull = true;
        }
        if(tmp.find("UNIQUE") != tmp.npos){
            isUnique = true;
        }
        Attribute attTmp(Aname, reinterpret_cast<badgerdb::DataType&>(attrType), maxSize, isNotNull, isUnique);
        attrs.push_back(attTmp);
  }
  return TableSchema(tableName, attrs, isTemp);
}

/*
The definition of print relation mode.
The specific print format is defined by you.
You can refer to the output format defined by DBMS such as MySQL and postgressql.
*/
void TableSchema::print() const {
  // TODO
  //Output table name, whether it is a temporary table, total attribute quantity, attribute name, type, maximum value, whether it is null, whether it is unique
  cout<<"TableName is : "<<getTableName()<<endl;
  if(isTempTable()){
  	cout<<"Is it TempTable : TRUE"<<endl;
  }
  else{
  	cout<<"Is it TempTable : FALSE"<<endl;
  }
  cout<<"The number of attribute is : "<<getAttrCount()<<endl;
  for(int i = 0; i < getAttrCount(); i++){
  	cout<<"The attribute at i is called : "<<getAttrName(i)<<", ";
  	cout<<"it's Type is : "<<getAttrType(i)<<", ";
  	cout<<"it's MaxSize is : "<<getAttrMaxSize(i)<<", ";
  	if(isAttrNotNull(i)){
  		cout<<"is it not null : TRUE, ";
	}
	if(!isAttrNotNull(i)){
		cout<<"is it not null : FALSE, ";
	}
	if(isAttrUnique(i)){
  		cout<<"is it Unique : TRUE, "<<endl;
	}
	if(!isAttrUnique(i)){
		cout<<"is it Unique : FALSE, "<<endl;
	}
  }
  }
}  // namespace badgerdb
