from services.user_service_interface import UserServiceInterface
from models.user import User


class UserService(UserServiceInterface):
    userDeatils={}
    def addUser(self,id,name):
        user=User(id,name)
        UserService.userDeatils[id]=user
        return user