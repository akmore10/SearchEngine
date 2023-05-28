from pandas import DataFrame
from dataclasses import dataclass
from DataStructures.SKU import *
from Backend.Interface.IDataSource import DataSourceRead
from Backend.RFilter import DataFilter

@dataclass
class ExtractData:
    def __init__(self,dataSourceRead : DataSourceRead,dataFilter : DataFilter):
        self.data : DataFrame = dataSourceRead.reads()
        self.dataFilter = dataFilter

    def _getUniqueValues(self,column) -> list[str]:
        return self.data[column].unique()

    def getData(self) -> dict:
        hashmap = {}
        for col in ["product_line","brand"]:
            uniqValues = self._getUniqueValues(col)
            for uniqValue in uniqValues:
                hashmap[self.dataFilter.filter(uniqValue)] = list(self.data[self.data[col] == uniqValue].index)
        return hashmap
