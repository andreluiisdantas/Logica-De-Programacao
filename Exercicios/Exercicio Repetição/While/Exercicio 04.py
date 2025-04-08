#---------------------------Exercicio 4----------------------------------#

tamanho = int(input("Digite o tamanho da lista: "))
lista = []
contador = 0
soma = 0

while contador < tamanho:
    num = float(input("Digite um número: "))
    lista.append(num)
    soma = sum(lista)
    contador += 1

media = soma / tamanho
print(f'A média dos números é: {media:.2f}')