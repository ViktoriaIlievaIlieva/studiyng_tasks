# print the values from 1 to 100 (each on a new line)
# but only print odd numbers i.e. 1,3,5,7,9,11...

count_value: int = 0
while count_value >= 0 and count_value < 100:
    count_value = count_value + 1
  
remainder: int = count_value % 2
if remainder == 1:
    print(count_value)

# DONE
