class Bill:
    def __init__(self,id,groupId,amount,contribution={},paidBy={}) -> None:
        self.id=id
        self.groupId=groupId
        self.amount=amount
        self.contribution=contribution
        self.paidBy=paidBy

    def getID(self):
        return self.id
    def setId(self,id):
        self.id=id
    
    def getGroupId(self):
        return self.groupId
    def setGroupId(self,groupId):
        self.groupId=groupId

    def getAmount(self):
        return self.amount
    def setAmount(self,amount):
        self.amount=amount

    def getContribution(self):
        return self.contribution
    def setContribution(self,contribution):
        self.contribution=contribution

    def getPaidBy(self):
        return self.paidBy
    def setPaidBy(self,paidBy):
        self.paidBy=paidBy