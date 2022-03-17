from abc import ABC,abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def addUser(self,id,name):
        pass