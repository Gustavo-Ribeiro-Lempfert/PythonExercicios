val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))
val3 = float(input('Digite o terceiro valor: '))

maior = val1
if val2 > val1:
    maior = val2
if val3 > val2:
    maior= val3
print(f'O maior valor é {maior}')

menor = val1
if val2 < val1:
    menor = val2
if val3 < val2:
    menor = val3
print(f'O menor valor é {menor}')