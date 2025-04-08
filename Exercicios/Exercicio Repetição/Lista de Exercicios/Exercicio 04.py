#Exercicio 04
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

lista = []
multiplos = 0

if num1 < 0 or num2 < 0:
    print("Os números precisa ser positivos")
else:
    if num2 > num1:
        for x in range((num1 + 1), num2):
            for i in range(2, x):
                if x % i == 0:
                    multiplos += 1
            if multiplos == 0 and x > 1:
                lista.append(x)
            multiplos = 0
    else:
        if num1 > num2:
            for x in range((num2 + 1), num1):
                for i in range(2, x):
                    if x % i == 0:
                        multiplos += 1
                if multiplos == 0 and x > 1:
                    lista.append(x)
                multiplos = 0
print(lista)