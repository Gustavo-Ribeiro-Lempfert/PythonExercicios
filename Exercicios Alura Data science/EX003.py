letra = input('Digite uma letra: ')

if letra in 'aeiouAEIOU':
    print('Vogal')
elif letra in '1234567890':
    print('Numerico')
else:
    print('Consoante')