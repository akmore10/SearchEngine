from Data.CSVDataSourceRead import CSVDataSourceRead
import os
from pandas import DataFrame
from dotenv import load_dotenv
from Data.RFilter import RFilter
from Data.SKUDataSource import SKUDataSource
from DataStructures.SKU import SKU


load_dotenv("../config.env")
fileName = "../DataSource/sales_data.csv"
obj = CSVDataSourceRead(fileName)

def test_Data():
    assert type(obj.reads()) == DataFrame

def test_RFilter():
    testString = "akhilesh\r"
    obj = RFilter()
    assert obj.filter(testString) == "akhilesh"

def test_SKUDataSource():
    dataSource = SKUDataSource(obj)
    assert type(dataSource.loads()) == list