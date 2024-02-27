import math

def area_do_circulo(raio):
    pi = math.pi
    area = pi * (raio ** 2)
    print(f'Área do círculo = {area:.2f}')

area_do_circulo(200)
