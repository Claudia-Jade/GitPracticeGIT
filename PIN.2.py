import getpass

pin = '1234'
# set pin.

total_attempts = 10
# total attempts variable. Can be changed
attempt_counter = total_attempts
# separate attempt counter influenced by total attempts

client_input = getpass.getpass(prompt='Type your Pin: ')
# hides the password entered to the terminal by the client

while client_input != pin:
    # opening while loop statement if client input is incorrect
    attempt_counter = attempt_counter - 1
    # tracks attempts made in loop
    if attempt_counter == 0:
        # condition for 0 attempts left
        print('<', 'Incorrect PIN.', 'Attempts left: ', attempt_counter, 'of', total_attempts,
              'Too many attempts. Account locked.', '>')
        break
    #     ends the loop
    print('<',  'Incorrect PIN.', 'Attempts left:', attempt_counter, 'of', total_attempts, '>')
    client_input = getpass.getpass('Type your PIN: ')
# end of conditional loop
if client_input == pin:
    print('<', 'Correct Pin.', 'Access granted.', '>')
#     breaks loop in contrary condition
