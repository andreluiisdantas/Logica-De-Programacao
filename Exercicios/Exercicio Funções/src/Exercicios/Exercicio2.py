def maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
num_maior = maior(num1, num2)

#########################################

"""
# Outra opção
def maior(lista):
    return max(lista)


lista = []

lista.append(int(input("Digite o primeiro número")))
lista.append(int(input("Digite o segundo número")))

num_maior = maior(lista)

print(num_maior)
"""