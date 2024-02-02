import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

print(f'A hipotenusa vai medir {hi :.2f}')
