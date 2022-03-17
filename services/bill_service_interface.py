from abc import ABC,abstractmethod

class BillServiceInterface(ABC):
    @abstractmethod
    def addBill(self,id,name,amount,contribution,paidBy):
        pass