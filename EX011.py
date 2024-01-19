larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))

m2 = larg * alt
tinta = m2 * 2

print(f'{m2:.2f}m² de parede serão necessarios {tinta:.2f} litros de tinta para pintar')