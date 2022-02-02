import getpass
# import the getpass function for hiding the password when typing

attempt_count = int(3)
# no. of total available attempts
pin = '1234'
# defne pininput as '1234' sting

InputCount = getpass.getpass(prompt='Type your Pin: ')
# define the prompt for getpass

while InputCount != pin:
    # attempt while loop
    attempt_count = attempt_count - 1
    # condition for while loop
    if attempt_count == 0:
        print('<', 'Attempts left: ', attempt_count, 'of 3.', 'Too many attempts. Account locked.', '>')
        break
    print('<', 'Attempt No.', attempt_count, 'of 3.', 'Incorrect PIN.', '>')
    InputCount = getpass.getpass('Type your PIN: ')
#     getpass hides the password in this stage of the code

if InputCount == pin:
    print('<', 'Correct Pin.', '>')
# if statement outside of while loop
