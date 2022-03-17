from factories.user_factory import userFactory
class UserController:
    def __init__(self,typ) -> None:
        self.userServiceInterface=userFactory(typ)

    def addUser(self,id,name):
        user=self.userServiceInterface.addUser(id,name)
        print(f"User with {id} Created.")
        return user
