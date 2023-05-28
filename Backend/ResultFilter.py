from Backend.Interface import IDataFilter
from DataStructures.SKU import SKU
from DataStructures.utils import Utils

class TopThreeMostSelling(IDataFilter):
    def  filter(self , data : list[SKU]):
        result = sorted(data ,cmp_to_key = Utils.compareSKU)
        return result[:3]

class TopThreeHighestSelling(IDataFilter):
    def filter(self,data:list[SKU]):
        result = sorted(data , cmp_to_key = Utils.compareSKUByprice)
        return  result[:3]

class TopThreeLowestSelling(IDataFilter):
    def filter(self,data:list[SKU]):
        result = sorted(data , cmp_to_key = Utils.compareSKUByprice)
        return result[-3:]
