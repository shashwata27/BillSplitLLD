from factories.bill_factory import billFactory

class BillController:
    def __init__(self,typ) -> None:
        self.billServiceInterface=billFactory(typ)

    def addBill(self,id,name,amount,contribution,paidBy):
        bill=self.billServiceInterface\
        .addBill(id,name,amount,contribution,paidBy)
        print(f"Bill with {id} Generated.")
        return bill

    def getUserBalance(self,userId):
        balance=0
        for billId,bill in self.billServiceInterface.billDetails.items():
            if userId in bill.getContribution().keys():
                balance-=bill.getContribution()[userId]
            if userId in bill.getPaidBy().keys():
                balance+=bill.getPaidBy()[userId]

        return balance
            