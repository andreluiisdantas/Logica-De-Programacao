#-----------Exercicio 5-----------#

idades = [int(input("Digite a primeira idade")), int(input("Digite a segunda idade")), int(input("Digite a terceira idade"))]

maiorIdade = max(idades)
menorIdade = min(idades)

if idades[1] == idades[2] and idades[1] == idades[3]:
    print("Idades iguais")
else:
    print(f'A maior idade é: {maiorIdade}')
    print(f'A menor idade é: {menorIdade}')

#-----------Outra Opção-----------#

"""
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))

if idade1 > idade2 and idade1 > idade3:
    print(f'{idade1} é a maior idade')
    if idade2 < idade3:
        print(f'{idade2} é a menor idade')
    else:
        print(f'{idade3} é a menor idade')
elif idade2 > idade1 and idade2 > idade3:
    print(f'{idade2} é a maior idade')
    if idade1 < idade3:
        print(f'{idade1} é a menor idade')
    else:
        print(f'{idade3} é a menor')
elif idade3 > idade1 and idade3 > idade2:
    print(f'{idade3} é a maior idade')
    if idade1 < idade2:
        print(f'{idade1} é a menor idade')
    else:
        print(f'{idade2} é a menor idade')
else:
    print("Idades iguais")
"""