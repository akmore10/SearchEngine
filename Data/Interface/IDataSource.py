from DataStructures.SKU import SKU
import pandas as pd
from pandas import DataFrame

class DataSource:
    def loads(self) -> list[any]:
        pass

class DataSourceRead:
    def reads(self) -> DataFrame:
        pass

    