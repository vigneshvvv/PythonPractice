from abc import ABC, abstractmethod

class mainAbstract(ABC):

    @abstractmethod
    def sampleFunction(self):
        pass

    @abstractmethod    
    def functionTwo(self):
        pass


class DataFunction(mainAbstract):

    def sampleFunction(self):
        print("sample abstract function working fine")

    def functionTwo(self):
        print("This is sample Function Two")


data = DataFunction()
data.sampleFunction()
data.functionTwo()
