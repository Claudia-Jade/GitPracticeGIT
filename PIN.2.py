import getpass

pin = '1234'

total_attempts = 3
attempt_counter = total_attempts

# problem child need a separate term for total counts.

client_input = getpass.getpass(prompt='Type your Pin: ')

while client_input != pin:
    attempt_counter = attempt_counter - 1
    if attempt_counter == 0:
        print('<', 'Incorrect PIN.', 'Attempts left: ', attempt_counter, 'of', total_attempts,
              'Too many attempts. Account locked.', '>')
        break
    print('<',  'Incorrect PIN.', 'Attempts left:', attempt_counter, 'of', total_attempts, '>')
    client_input = getpass.getpass('Type your PIN: ')
if client_input == pin:
    print('<', 'Correct Pin.', '>')
