#Algoritmo para comparar tres entradas(recebe 3 valores e os compara), qual é maior ou qual é menor e se são iguais aos outros

print('-+-' * 7)
print('Comparador de Numeros')
print('-+-' * 7)

#Recebe os valores
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor:'))

#compara os 3 valores
#maior que todos
if valor1 > valor2 and  valor1 > valor3:
    print('-+-' * 7 + '\nResposta:' )
    print(f'{valor1} é maior que {valor2} e {valor3}')

elif valor2 > valor1 and valor2 > valor3:
    print('-+-' * 7 + '\nResposta:' )
    print(f'{valor2} é maior que {valor1} e {valor3}')

elif valor3 > valor1 and valor3 > valor2:
    print('-+-' * 7 + '\nResposta:' )
    print(f'{valor3} é maior que {valor1} e {valor2}')
    
#todos iguais
elif valor1 == valor2 == valor3:
    print('-+-' * 7 + '\nResposta:' )
    print('todos são iguais')
