from services.group_service import GroupService
def groupFactory(type):
    if type=="group1":
        return GroupService()