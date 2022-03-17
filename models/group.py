class Group:
    def __init__(self,id,name,members=[]) -> None:
        self.id=id
        self.name=name
        self.members=members

    def getID(self):
        return self.id
    def setId(self,id):
        self.id=id
    
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    def getMembers(self):
        return self.members
    def setMembers(self,members):
        self.members=members