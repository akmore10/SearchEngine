from pandas import DataFrame
from dataclasses import dataclass
from DataStructures.SKU import *
from collections import defaultdict
from Backend.Interface.IDataSource import DataSourceRead
from Backend.RFilter import RFilter,DataFilter
from Backend.CSVDataSourceRead import CSVDataSourceReader

@dataclass
class ExtractData:
    def __init__(self,dataSourceRead : DataSourceRead,dataFilter : DataFilter):
        self.data : DataFrame = dataSourceRead.reads()
        self.dataFilter = dataFilter

    def _getUniqueValues(self,column) -> list[str]:
        return self.data[column].unique()

    def getData(self) -> dict:
        hashmap = defaultdict(list)
        for col in ["sku","product_line","brand"]:
            uniqValues = self._getUniqueValues(col)
            for uniqValue in uniqValues:
                result = list(self.data[self.data[col] == uniqValue].index)
                for word in uniqValue.split(" "):
                    if word not in hashmap:
                        hashmap[self.dataFilter.filter(word).lower()] = result
                    else:
                        hashmap[self.dataFilter.filter(word).lower()].extend(result)
        return hashmap