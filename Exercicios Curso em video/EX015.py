d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))

valor = (d * 60) + (km * 0.15)
print(f'O total a pagar fica R${valor}')
