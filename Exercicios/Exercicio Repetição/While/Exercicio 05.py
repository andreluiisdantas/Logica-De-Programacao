#---------------------------Exercicio 5----------------------------------#

opcoes = ""

while opcoes != "SAIR":

    opcoes = input("Escolha uma opção: \n(+) - Somar\n(-) - Subtrair\n(*) - Multiplicar \n(/) - Dividir\n(Sair) - Sair\n").upper()

    if opcoes == "+" or opcoes == "-" or opcoes == "*" or opcoes == "/":
        match opcoes:

            case "+":
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                resultado = num1 + num2
                print(f'\n{num1} + {num2} = {resultado}\n')
            case "-":
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                resultado = num1 - num2
                print(f'\n{num1} - {num2} = {resultado}\n')
            case "*":
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                resultado = num1 * num2
                print(f'\n{num1} * {num2} = {resultado}\n')
            case "/":
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
                if num1 != 0 and num2 != 0 :
                    resultado = num1 / num2
                    print(f'\n{num1} / {num2} = {resultado}\n')
                else:
                    print("Erro: Divisão por zero.")
    elif opcoes == "SAIR":
        print("Saindo...")
    else:
        print("Opção invalida")