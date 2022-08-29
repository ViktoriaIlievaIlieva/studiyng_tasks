import json

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.active = False

class UserManager:
    def __init__(self):
        self.users = []

    def load (self):
        file = open("users.json","r")
        file_content = file.read()
        file.close()

        list_with_python_dictionaries = json.loads(file_content)

        for dictionary in list_with_python_dictionaries:
            user = User()
            user.username = dictionary["username"]
            user.password = dictionary["password"]
            user.active = dictionary["active"]

            self.users.append(user)


    def save (self):
        list = []

        for index in self.users:
            dictionary_2 = {}
            dictionary_2 ["username"] = index.username
            dictionary_2 ["password"] = index.password
            dictionary_2 ["active"] = index.active
            list.append(dictionary_2)

        json_list_of_dictionaries = json.dumps(list)

        file= open ("users.json", "w")
        file.write(json_list_of_dictionaries)
        file.close()


