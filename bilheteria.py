
print('-+-' * 10)
print('Bilheteria shopping Nelson')
print('-+-' * 10)

idade = int(input('qual a sua idade: '))

if idade < 18:
    print('Voce é menor de idade, paga apenas meio ingresso')
    print('Ingresso: 10R$')
    
elif idade <= 250:
    print('voce é velho pra caramba, o que ta fazendo na terra ainda? kkkk, ingresso é de graça')
    print('Ingresso: de graça')

else:
    print('Voce é de maior, paga inteira.')
    print('ingresso: 20R$')