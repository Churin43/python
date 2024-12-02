import random

def adivinhar_numero():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    print('tente adivinhar o numero entre 1 e 100')

    while True:
        tentativa = int(input('seu palpite: '))
        tentativas += 1
        if tentativa < numero_secreto:
            print('mais alto!!!')
        elif tentativa > numero_secreto:
            print('mais baixo!!!')
        else:
            print(f'acertou!!, o numero era {numero_secreto}')
            print(f'acertou em: {tentativas} tentativas ')
            break

adivinhar_numero()