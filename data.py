from datetime import date

hoje  = date.today() #hoje recebe o dia e ano atual

print(f'hoje é dia: {hoje}')

ano = hoje.year #ano recebe do hoje o year(ano)


nascimento = int(input('informe o ano que voce nasceu:'))

print(f'voce tem {ano - nascimento}')