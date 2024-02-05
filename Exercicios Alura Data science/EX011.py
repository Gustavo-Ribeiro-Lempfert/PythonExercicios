num = int(input('Digite um numero para saber se é primo: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} Não é um numero primo')
            break
        else:
            print(f'{num} é um numero primo')
else:
    print(f'{num} não é um numero primo')