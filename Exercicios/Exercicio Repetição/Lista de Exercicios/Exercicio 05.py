#Exercicio 05
tentativa = 0

while tentativa < 3:
    senha = input("Digite a senha: ")
    tentativa += 1
    if senha != 'Senha!123':
        print(f'Senha incorreta! Você tem {3 - tentativa} tentativa(s)')
    else:
        print(f'Acesso liberado!')
        break