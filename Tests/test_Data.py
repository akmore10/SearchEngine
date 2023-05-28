from Backend.CSVDataSourceRead import CSVDataSourceReader
from pandas import DataFrame
from Backend.RFilter import RFilter
from Backend.SKUDataSource import SKUDataSource
from DataStructures.SKU import SKU


fileName = "../DataSet/sales_data.csv"
obj = CSVDataSourceReader(fileName)

def test_Data():
    assert type(obj.reads()) == DataFrame

def test_RFilter():
    testString = "akhilesh\r"
    obj = RFilter()
    assert obj.filter(testString) == "akhilesh"

def test_SKUDataSource():
    dataSource = SKUDataSource(obj)
    assert type(dataSource.loads()) == list