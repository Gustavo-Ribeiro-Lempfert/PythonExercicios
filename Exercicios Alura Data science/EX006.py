colonia_A = 4
colonia_B = 10
dia = 1

taxa_A = 0.03
taxa_B = 0.015

while colonia_A < colonia_B:
    colonia_A *= 1 + taxa_A
    colonia_B *= 1 + taxa_B
    dia += 1

print(f'Levara {dia} dias para que a colonia A ultrapasse a colonia B')