
class DataFilter:
    def filter(self,data : any) -> any:
        pass

class RFilter(DataFilter):
    def filter(self, data: any) -> any:
        return data.lower().replace("\r","")