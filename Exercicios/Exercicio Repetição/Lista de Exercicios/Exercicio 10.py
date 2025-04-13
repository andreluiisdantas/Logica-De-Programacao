#Exercicio 10
tamanho = int(input("Digite a quantidade de numeros na lista: "))
lista = []

for i in range(tamanho):
    i += 1
    num = int(input("Digite um número: "))
    lista.append(num)

maior_num = max(lista)
print(f'O maior número da lista é: {maior_num}')

lista.remove(maior_num)
maior_num = max(lista)

print(f'O segundo maior número da lista é: {maior_num}')