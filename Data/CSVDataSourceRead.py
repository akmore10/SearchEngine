
from pandas import DataFrame
from Data.Interface.IDataSource import DataSourceRead
import pandas as pd

class CSVDataSourceRead(DataSourceRead):
    def __init__(self,fileName):
        self.fileName = fileName
    def reads(self) -> DataFrame:
        return pd.read_csv(self.fileName)