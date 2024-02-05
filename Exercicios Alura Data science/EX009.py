num = int(input('Digite um numero: '))

fatorial = 1
i = num

while i > 0:
    fatorial *= i
    i -= 1

print(f'O fatorial de {num} é {fatorial}')