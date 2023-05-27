# SKU_ID,sku,product_line,brand,sales,price
from dataclasses import dataclass

@dataclass
class SKU:
    def __init__(self,id : int , sku : str,product_line : str, brand :str, sales:int, price :float):
        self.id = id
        self.sku = sku
        self.product_line = product_line
        self.brand = brand
        self.sales = sales
        self.price = price
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.id,self.sku,self.product_line,self.brand,self.sales,self.price)