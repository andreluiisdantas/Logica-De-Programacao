def media(lista):
    return sum(lista) / len(lista)


lista = []
tamanho = int(input("Digite o tamanho da lista: "))

for i in range(tamanho):
    num = int(input("Digite o número: "))
    lista.append(num)

resultado = media(lista)

print(f'A média da lista é: {resultado}')