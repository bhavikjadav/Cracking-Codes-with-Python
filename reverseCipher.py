message = 'Three can keep a secret, if Two of them are dead.'
# message = '.daed era meht fo owT fi ,terces a peek nac eerhT'
# message = 'Bhavik Chandrakant Jadav'
translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i -= 1

print(translated)
