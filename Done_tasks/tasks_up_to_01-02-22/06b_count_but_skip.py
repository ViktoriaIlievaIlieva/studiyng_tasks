# Count from 0 to 100
# but:
# 1. skip every third number

count_value: int = 0
while count_value >= 0 and count_value < 100:
    count_value = count_value + 1
    every_third: int = count_value % 3
    if every_third == 0:
        print(count_value)

# DONE
