#----------------------Exercicio 5---------------------#

tamanho = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(1, tamanho+1):
    lista.append(int(input("Digite um número: ")))

media = sum(lista)/tamanho

print(f'A média dos valores é: {media}')


#----------------------Outra Opção---------------------#

"""
tamanho = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(1, tamanho+1):
    lista.append(int(input("Digite um número: ")))

soma = 0
for numero in lista:
    soma = soma + numero

media = soma/tamanho

print(f'A média dos valores é: {media}')
"""