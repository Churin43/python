#Algoritmo de login

#senha e user correto
user_correto  = 'bryan'
senha_correta = 1234

#input de usuario e senha
user_name  = str(input('digite seu nome de usuario: '))
user_senha = int(input('digite sua senha: '))

if user_name == user_correto and user_senha == senha_correta: #caso se tudo for correto
    print(f'seja bem vindo, {user_name}!')

elif user_name != user_correto: #usuario incorreto
    print('nome de usuario incorreto')

elif user_name == user_correto and user_senha != senha_correta: #usuario correto mas senha incorreta
    print('sua senha esta incorreta')

