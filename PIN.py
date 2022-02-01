import getpass
# import the getpass function for hiding the password when typing

attempt_count = int(3)
# no. of total available attempts
pininput = '1234'
# defne pininput as '1234' sting


client_input = getpass.getpass(prompt='Type your Pin: ')
# define the prompt for getpass

while client_input != pininput:
    # attempt while loop
    attempt_count = attempt_count - 1
    # condition for while loop
    if attempt_count == 0:
        print('<', 'Attempts left:', attempt_count, 'of 3.', 'Too many attempts. Account locked.', '>')
        break
    print('<', 'Attempts left:', attempt_count, 'of 3.', 'Incorrect PIN.', '>')
    client_input = getpass.getpass('Type your PIN: ')
#     getpass hides the password in this stage of the code

if client_input == pininput:
    print('<', 'Correct Pin.', '>')
# if statement outside of while loop
