def dict_users(username):
    dict = []
    for i in range(len(username)):
        user = {"username": username[i], "ID": i+1}
        dict.append(user)
    return dict
print(dict_users(["Akai", "Roger", "Fanny", "Diggie"]))
dict_users([])