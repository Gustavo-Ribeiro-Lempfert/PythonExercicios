gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

acima3K = 0
for gasto in gastos:
    if gasto > 3000.00:
        acima3K += 1

print(f'Total de {acima3K} gastos acima de R$3000.00')