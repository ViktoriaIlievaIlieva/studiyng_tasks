# Dictionaries can be written on multiple lines

weather_report: dict = {
    "sofia": -5.0,
    "moscow": -15.0,
    "athens": 10,
    "rio": 30.0,
    "new york": 7.1,
    "san francisco": 22.5,
    "london": -11.0,
}


# TASK 1
# Write code that takes a city name from the user
# Write a function that RETURNs True if the city name is a key in the dictionary weather_report


user_city_1: str = input("Name a city: ")


def user_city(user_city_1: str) -> bool:
    list_with_keys = weather_report.keys()
    if user_city_1 in list_with_keys:
        return True
    else:
        return False

# Done


# TASK 2 
# Write code that calls the function from task 1 and saves the value into a variable city_report_exists
# If the city isn't in the dictionary print "We don't have a weather report for " + city name
# Else print "Today the temperature for " + city name + " is " + the value for that city


city_report_exists: bool = user_city(user_city_1)
if city_report_exists == False:
    print("We don't have a weather report for " + user_city_1)

new_record: str = input("Do you want to add new report? Yes or No? ")
if new_record == "yes":
    new_record_temperature: str = input("What is the temperature in" + user_city_1)
    weather_report[user_city_1] = int(new_record_temperature)
    print(weather_report)

else:
    print("Today the temperature for " + user_city_1 + " is " + str(weather_report[user_city_1]))
  

# Done 

# TASK 3
# Take the code from task 2 but modify it so that:
# if the city is not in the dictionary
# - you still print "We don't have a weather report for " + city name
# - ask weather the user wants to add one:
# a/ if the user writes "yes" then ask him for a value and put the new city name and value in the dictionary and print
# the whole dictionary
# b/ if the user writes anything different than "yes" you don't do anything more

# Done combined with Task 2
