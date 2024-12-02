#Algoritmo que verifica se o numero é positivo ou negativo

num1 = int(input('digite um numero:'))

#verifica se o numero é menor que 0
if num1 < 0:
    print(f'{num1} negativo')
else:
    print(f'{num1} é positivo')