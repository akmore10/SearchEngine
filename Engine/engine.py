from DataStructures.Trie import Trie
from Extraction.extract import *
from Backend.CSVDataSourceRead import CSVDataSourceReader
from Backend.RFilter import RFilter
import os
from dotenv import load_dotenv
from Backend.SKUDataSource import SKUDataSource



load_dotenv("../config.env")

class Engine:
    def __init__(self,dataSource , dataFilter):
        self.trie = Trie()
        self.data = ExtractData(dataSource , dataFilter).getData()
        self._buildEngine()
    
    def _buildEngine(self):
        for words , values in self.data.items():
            self.trie.insert(words,values)
    def search(self,searchText):
        return self.trie._iterator(searchText)


fileName = "DataSet/sales_data.csv"
cvsReader = CSVDataSourceReader(fileName)

obj = SKUDataSource(cvsReader)
result = obj.loads()


engine = Engine(cvsReader , RFilter())
indexList = engine.search("samsung").indexList

for index in indexList:
    

