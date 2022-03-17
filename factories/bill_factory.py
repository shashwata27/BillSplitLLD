from services.bill_service import BillService
def billFactory(type):
    if type=="bill1":
        return BillService()