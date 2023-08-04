import json
from task4 import User

list_users = []
a = User('vitalya', 1, 1)
b = User('boris', 2, 1)
c = User('arkadiy', 3, 2)
list_users.append(a)
list_users.append(b)
list_users.append(c)


with open('users.json', 'w') as j_file:
    f_dict = {i.level: {} for i in list_users}
    for i in list_users:
        f_dict.get(i.level).update({i.user_id: i.name})
    json.dump(f_dict, j_file)
