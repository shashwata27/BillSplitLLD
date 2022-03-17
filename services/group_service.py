from services.group_service_interface import GroupServiceInterface
from models.group import Group


class GroupService(GroupServiceInterface):
    groupDetails={}
    def addGroup(self,id,name,members):
        group=Group(id,name,members)
        GroupService.groupDetails[id]=group
        return group