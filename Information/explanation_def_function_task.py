def greet():
  name = input("What is your name: ")
  time = input("Enter time of day: ")
  print("Good " + time + ", " + name + "!")
  
  return name, time

name_outside, time_outside = greet()
print("The name: " + name_outside)
print("The time: " + time_outside)


