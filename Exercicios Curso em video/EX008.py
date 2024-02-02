n = float(input('Digite um distância em metros: '))

km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f'{n} Metros \n'
      f'{km}km\n'
      f'{hm}hm\n'
      f'{dam}dam\n'
      f'{dm}dm\n'
      f'{cm}cm\n'
      f'{mm}mm')