
from pandas import DataFrame
from Backend.Interface.IDataSource import DataSourceRead
import pandas as pd

class CSVDataSourceReader(DataSourceRead):
    def __init__(self,fileName):
        self.fileName = fileName
    def reads(self) -> DataFrame:
        return pd.read_csv(self.fileName)