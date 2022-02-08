import getpass
pin = 1234
count = 0

while count < 3:
    supplied_pin = int(input("Enter Pin: "))
    if supplied_pin == pin:
        print("Correct Pin")
        break
    elif supplied_pin != pin:
        print("Incorrect Pin, Try again - attempt", count + 1, "of 3")
        count += 1
    else:
        print("Sorry - FAIL")