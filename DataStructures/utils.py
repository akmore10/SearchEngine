from DataStructures.SKU import SKU

class Utils:
    @staticmethod
    def compareSKU(a : SKU,b :SKU):
        if a.sales > b.sales:
            return -1
        else:
            return 1
    @staticmethod
    def compareSKUByprice(a : SKU,b : SKU):
        if a.price > b.price:
            return 1
        else:
            return -1            