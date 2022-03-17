from factories.group_factory import groupFactory
class GroupController:
    def __init__(self,typ) -> None:
        self.groupServiceInterface=groupFactory(typ)
    
    def addGroup(self,id,name,members):
        group=self.groupServiceInterface\
            .addGroup(id,name,members)
        print(f"Group with {id} Created.")
        return group