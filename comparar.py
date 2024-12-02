#Algoritmo para comparar duas entradas(recebe 2 valores e os compara), qual é maior e qual é menor e se são iguais

print('-+-' * 7)
print('Comparador de Numeros')
print('-+-' * 7)

#Recebe os valores
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor: '))

#compara os valores
if valor1 > valor2:
    print('-+-' * 7 + '\nResposta:' )
    print(f'valor: {valor1}, é maior que o valor: {valor2}')

elif valor1 < valor2:
    print('-+-' * 7 + '\nResposta:' )
    print(f'valor: {valor1}, é menor que o valor: {valor2}')

elif valor1 == valor2:
    print('-+-' * 7 + '\nResposta:' )
    print(f'valor: {valor1}, é igual ao valor: {valor2}')
