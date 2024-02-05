num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

contador = num1 + 1
while contador > num1 and contador < num2:
    print(contador)
    contador += 1