from Data.Interface.IDataFilter import DataFilter

class RFilter(DataFilter):

    def filter(self, data: any) -> any:
        return data.lower().replace("\r","")