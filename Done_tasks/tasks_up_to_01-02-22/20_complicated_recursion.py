# I just want to show you this exist - no task here
# This could be hard to get so ask me if you don't


def print_and_increment_up_to_100(number):
    if number >= 100:
        return

    print(number)
    print_and_increment_up_to_100(number + 1)

    # Calling the function from within itself is called recursion - after line twelve it will go back to line 4 but
    # number this time will be bigger with 1


print_and_increment_up_to_100(1)
