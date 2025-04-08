#Exericio 01
lista = []

for i in range (10):
    lista.append(int(input("Digite um número")))
    i += 1

multiplo = 0
for numero in lista:
    if numero % 3 == 0:
        multiplo += 1
print(f'A quantidade de número multiplos de 3 na lista é: {multiplo}')