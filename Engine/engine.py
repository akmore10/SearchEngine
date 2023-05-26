from DataStructures.Trie import Trie
from Extraction.extract import *
from Data.CSVDataSourceRead import CSVDataSourceRead
from Data.RFilter import RFilter

class Engine:
    def __init__(self,dataSource , dataFilter):
        self.trie = Trie()
        self.data = ExtractData(dataSource , dataFilter).getData()
    
    def buildEngine(self):
        for words , values in self.data.items():
            self.trie.insert(words,values)
        print(self.trie.root.children)

fileName = "DataSource/sales_data.csv"
engine = Engine(CSVDataSourceRead(fileName) , RFilter())
engine.buildEngine()

