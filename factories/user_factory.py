from services.user_service import UserService
def userFactory(typ):
    if typ=="user1":
        return UserService()