from DataStructures.SKU import SKU
from Backend import CSVDataSourceRead
from Backend.Interface.IDataSource import DataSource


class SKUDataSource(DataSource):
    def __init__(self,dataSourceRead : CSVDataSourceRead):
        self.data = dataSourceRead.reads()

    def loads(self) -> list[SKU]:
        result = []

        for index in self.data.index:
            r = []
            for column_name in self.data.columns:
                value = self.data.at[index, column_name]
                r.append(value)
            result.append(self._convertListToObject(r))
            
        return result
    def _convertListToObject(self,values) -> SKU:
        return SKU(values[0],values[1],values[2],values[3],values[4],values[5])