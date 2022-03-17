import sys
sys.path.append(r'D:\Projects\BillGenerator')
from controllers.bill_controller import BillController
from controllers.user_controller import UserController
from controllers.group_controller import GroupController

#types
userController=UserController('user1')
billController=BillController('bill1')
groupController=GroupController('group1')

user1=userController.addUser("user1","sam")
user2=userController.addUser("user2","chetan")
user3=userController.addUser("user3","omar")
user4=userController.addUser("user4","chintu")
user5=userController.addUser("user5","gijju")

members=[user1,user2,user3,user4,user5]
groupController.addGroup('group1','avengers',members)

#what they need to pay
contribution={'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}
#what they paid actually
paidBy={'user1':200,'user2':100,'user3':50,'user4':50,'user5':100}
billController.addBill('bill1','group1',500,contribution,paidBy)

print(billController.getUserBalance('user1'))
print(billController.getUserBalance('user2'))
print(billController.getUserBalance('user3'))

