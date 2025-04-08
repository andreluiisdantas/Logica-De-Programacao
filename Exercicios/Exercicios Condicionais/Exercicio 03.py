#-----------Exercicio 3-----------#

quantidade = int(input("Digite a quantidade de produtos: "))
valorUnit = float(input("Digite o valor unitário de cada produto: "))

if quantidade > 100:

    desconto = valorUnit * 0.1
    valorFinal = quantidade * (valorUnit - desconto)

    print("O desconto será de 10%\n")
    print(f'Preço do produto: R$ {valorUnit:.2f}')
    print(f'Quantidade solicitada: {quantidade} unidades')
    print(f'O desconto por unidade será: R$ {desconto:.2f}')
    print(f'O valor final será: R$ {valorFinal:.2f}')

else:
    desconto = valorUnit * 0.05
    valorFinal = quantidade * (valorUnit - desconto)

    print("O desconto será de 5%\n")
    print(f'Preço do produto: R$ {valorUnit:.2f}')
    print(f'Quantidade solicitada: {quantidade} unidades')
    print(f'O desconto por unidade será: R$ {desconto:.2f}')
    print(f'O valor final será: R$ {valorFinal:.2f}')