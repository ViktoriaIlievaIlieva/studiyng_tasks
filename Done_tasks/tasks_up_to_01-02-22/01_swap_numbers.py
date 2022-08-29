x: str = input("Enter x first variable: ")
y: str = input("Enter y second variable: ")

# Swap variables so that x = y and y = x

copy_of_y: str = y
copy_of_x: str = x

x: str = copy_of_y
y: str = copy_of_x

print("Numbers after swap x =", x, ", y =", y)


# DONE
