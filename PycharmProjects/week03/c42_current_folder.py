from __future__ import print_function
import os
def dict_users(username):
    dict = []
    path = '.'
    files = os.listdir(path)
    for i in range(len(username)):
        user = {"filename": files, "type": 1}
        dict.append(user)
    return dict
    for name in files:
        lis.append(name)
    return name
print(dict_users("apple"))