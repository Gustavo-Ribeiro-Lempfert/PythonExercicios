temp = int(input('Digite uma temperatura em Celcius'))
soma = 0
contador = 0

while temp != -273:
    soma += temp
    contador += 1
    temp = int(input('Digite uma temperatura em Celcius'))

media = soma / contador

print(f'A media das temperaturas é {media}')