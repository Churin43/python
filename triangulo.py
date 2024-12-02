#Algoritimo que verifica se um triangulo é equilatero ou escaleno

#medidas do triangulo
lado1 = float(input("primeiro lado: "))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('terceiro lado: '))

#equilatero = todos os lados são iguais
if lado1 == lado2 and lado1 == lado3:
    print('o triangulo é equilatero')

#escaleno = todos os lados são diferentes
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado1 and lado2 != lado3:
    print('o triangulo é escaleno')

#isosceles = dois são iguais e um diferente
elif lado1 == lado2 and lado2 != lado3 or lado3 == lado1 and lado1 != lado2 or lado2 or lado2 == lado3 and lado2 != lado1:
    print('o triangulo é isosceles')
