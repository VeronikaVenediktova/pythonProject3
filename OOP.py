class User:
    description = "Regular Human User"
    
    def __init__(self, name, phone):
        self.name = "Vasiliy"
        self.phone = 1234567


user_1 = User("Nic", 1234)
user_2 = User("Bill", 3654)
# list_of_users = []
#
# while True:
#     name = input("Fill name: ")
#     if name == "q":
#         break
#     user_1 = User()
#     user_1.name = name
#     user_1.phone = int(input("Fill phone "))
#     list_of_users.append(user_1)
#
# for item in list_of_users:
#     print(item.name, item.phone)