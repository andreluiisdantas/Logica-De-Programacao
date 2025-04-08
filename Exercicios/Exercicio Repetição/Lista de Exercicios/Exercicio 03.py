#Exercicio 03
opcao = True

while opcao:
    menu = input("Escolha a opção:\n(Entrar) (Sair) ").upper()

    if menu == 'ENTRAR':
        print("Entrando...")
    elif menu == 'SAIR':
        print("Saindo...")
        break
    else:
        print("Opção invalida")