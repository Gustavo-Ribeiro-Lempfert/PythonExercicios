valor = int(input('Digite um valor: '))

while valor < 0 or valor > 5:
    print('Valor invalido!')
    valor = int(input('Digite um valor: '))

print('Valor valido')