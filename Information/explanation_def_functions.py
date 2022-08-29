# Информация

# Приема и връща

def integer(text):
  if text == "5":
    return 5
  elif text == "6":
    return 6

a = integer("5")





# 1. Не приема и не връща нищо
def my_function():
  print("Hello")
  print("I am a function")

my_function()

# 2. Не приема нищо, връща стринг "Hello"
def my_function():
  return "Hello"

text = my_function()

# 3. Приема стойности, но не връща нищо
def my_function(a, b):
  print("a: ", a)
  print("b: ", b)

my_function(3, 5)

# 4. Приема стойности и връща стойности
def my_function(a, b):
  a_list = []
  a_list.append(a)
  a_list.append(b)
  return a_list

list_from_function = my_function(3, 5)
