# Dictionaries are similar to lists
# Lists have multiple values that are all assigned a place (number) in the list
# Dictionaries hold multiple values but instead of a number for the place they have a string (key)

this_is_a_list = [1, 2, 3]
this_is_a_list.append(4)
print("this_is_a_list[2] = ", this_is_a_list[2])


this_is_a_list = [1, 2, 3]
this_is_a_list.append(4)
index = 2
print("this_is_a_list[2] = ", this_is_a_list[index])

this_is_a_dictionary = { "a": 1, "b": 2, "blabla": 3 }
this_is_a_dictionary["anything as key"] = 4
print("this_is_a_dictionary[\"anything as key\"] = ", this_is_a_dictionary["anything as key"])

# Dictionaries can be used to describe a lot of stuff
# example:

user = {}
user["username"] = "viki"
user["password"] = "example"
user["gender"] = "female"
user["age"] = 26

print(user)

# Similar to how you can give a variable in the square brackets of a list you can use a variable of type string inside the dictionary as well

key = "username"
print(user[key])

# Dictionaries store their values in what is called a key-value pair so when you want to check all values within a dictionary you do this

for key in user:
    print(key, "=", user[key])

user = {}
user["username"] = "viki"
user["password"] = "example"
user["gender"] = "female"
user["age"] = 26


# Принтиране на вс потребители с for цикъл

list_of_users = []

user1 = {}
user1["username"] = "viki"
user1["password"] = "example"
user1["gender"] = "female"
user1["age"] = 27

user2 = {}
user2["username"] = "ico"
user2["password"] = "example_2"
user2["gender"] = "male"
user2["age"] = 26

user3 = {}
user3["username"] = "deni"
user3["password"] = "example_3"
user3["gender"] = "female"
user3["age"] = 26


list_of_users.append(user1)
list_of_users.append(user2)
list_of_users.append(user3)

for user in list_of_users:
  print (user ["username"])

  #Принтирай стойността, която стои зад ключа username във всеки речник (user) в листта (list_of_users)


# Принтиране на вс потребители с while цикъл

list_of_users = []

user1 = {}
user1["username"] = "viki"
user1["password"] = "example"
user1["gender"] = "female"
user1["age"] = 27

user2 = {}
user2["username"] = "ico"
user2["password"] = "example_2"
user2["gender"] = "male"
user2["age"] = 26

user3 = {}
user3["username"] = "deni"
user3["password"] = "example_3"
user3["gender"] = "female"
user3["age"] = 26


list_of_users.append(user1)
list_of_users.append(user2)
list_of_users.append(user3)

index = 0
while index < len(list_of_users):
  promenliva_1= list_of_users[index] # променливата става равна на целия речник, не само на един елемент 
  print (promenliva_1["username"]) # с promenliva_1 извикваме целия речник, в скобите извикваме ключа зад, който седи информацията, която ни трябва
  index= index + 1

# В лист запазваме еден и същ тип информация 
# В dictionary може да запазим различни типове информация 
# Най-често листовете се ползват, за да съдържат различните речници. А речниците се ползват за по-лесно е ясно каталогизиране на данни. 

