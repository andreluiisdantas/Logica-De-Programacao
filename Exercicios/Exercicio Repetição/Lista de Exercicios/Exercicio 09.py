#Exercicio 09
tamanho = int(input("Digite a quantidade de numeros na lista: "))
lista = []
num_maior_media = []

for i in range(tamanho):
    i += 1
    num = int(input("Digite um número: "))
    lista.append(num)

media = sum(lista) / len(lista)
print(f'A média dos números é: {media}')

for i in range(len(lista)):
    if lista[i] > media:
        num_maior_media.append(lista[i])

print(f'O números acima da média é: {num_maior_media}')

