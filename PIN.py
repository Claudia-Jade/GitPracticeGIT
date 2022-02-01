import getpass
# import the getpass function for hiding the password when typing

pininput = '1234'
# defne pininput as '1234' sting

attempt = getpass.getpass(prompt='Type your Pin: ')
# define the prompt for getpass
a = 0
# new variable for attempt counter

while attempt != pininput:
    # attempt while loop
    a = a + 1
    # condition for while loop
    if a > 2:
        print('<', 'Attempt No.', a, 'of 3.', 'Too many attempts. Account locked.', '>')
        break
    print('<', 'Attempt No.', a, 'of 3.', 'Incorrect PIN.', '>')
    attempt = getpass.getpass('Type your PIN: ')

if attempt == pininput:
    print('<', 'Correct Pin.', '>')
# if statement outside of while loop
