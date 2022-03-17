from services.bill_service_interface import BillServiceInterface
from models.bill import Bill


class BillService(BillServiceInterface):
    billDetails={}
    
    def addBill(self,id,name,amount,contribution,paidBy):
        bill=Bill(id,name,amount,contribution,paidBy)
        BillService.billDetails[id]=bill
        return bill