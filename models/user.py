class User:
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name

    def getID(self):
        return self.id
    def setId(self,id):
        self.id=id
    
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name