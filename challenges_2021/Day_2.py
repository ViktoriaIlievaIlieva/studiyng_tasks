lines = []
with open("challenges_2021/Day_2.txt", "r") as file:
  lines = file.readlines() 

x = 0
y = 0

for line in lines:
  splited_nasoki = line.split()
  number = int (splited_nasoki [1])
  if splited_nasoki [0] == "forward":
    x = x + number 
  elif splited_nasoki [0] == "down":
    y = y + number
  elif splited_nasoki [0] == "up":
    y = y - number

coordinates = x * y 
print (coordinates)
