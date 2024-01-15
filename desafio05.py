n = int(input('Digite um número: '))

print(f'Tabuada do número {n}:')

for i in range(1, 11):
    result = n * i
    print(f'{n} x {i} = {result}')
