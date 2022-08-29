lines = []
with open("challenges_2021/Day_1.txt", "r") as file:
  lines = file.readlines() 

list_of_numbers = []
for number in lines: 
  number = int (number)
  list_of_numbers.append (number) 

list_with_higher_numbers = []

index = 0 
while index < len (list_of_numbers) - 1:
  if list_of_numbers [index] < list_of_numbers [index + 1]:
    list_with_higher_numbers.append(list_of_numbers [index])
  index = index + 1

number_of_bigger_numbers = len (list_with_higher_numbers)
print (number_of_bigger_numbers)


  



# list_with_higher_numbers = []
# for index in list_of_numbers:
#   if index < index + 1:
#     list_with_higher_numbers.append(index)
# print (list_with_higher_numbers)

# number_of_bigger_numbers = len (list_with_higher_numbers)
# print (number_of_bigger_numbers)
  
    
#
