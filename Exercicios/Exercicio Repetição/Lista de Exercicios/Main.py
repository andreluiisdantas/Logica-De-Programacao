"""
#Exercicio 01
lista = []

for i in range (10):
    lista.append(int(input("Digite um número")))
    i += 1

multiplo = 0
for numero in lista:
    if numero % 3 == 0:
        multiplo += 1
print(f'A quantidade de número multiplos de 3 na lista é: {multiplo}')
"""

"""
#Exercicio 02
senha = ''

while senha != 'Senha!123':
    senha = input("Digite uma senha: ")
    continue
print("Senha correta")
"""

"""
#Exercicio 03
opcao = True

while opcao:
    menu = input("Escolha a opção:\n(Entrar) (Sair) ").upper()

    if menu == 'ENTRAR':
        print("Entrando...")
    elif menu == 'SAIR':
        print("Saindo...")
        break
    else:
        print("Opção invalida")
"""

"""
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
print(f'Os números primos são {lista}')
"""

"""
#Exercicio 05
tentativa = 0

while tentativa < 3:
    senha = input("Digite a senha: ")
    tentativa += 1
    if senha != 'Senha!123':
        print(f'Senha incorreta! Você tem {3 - tentativa} tentativa(s)')
    else:
        print(f'Acesso liberado!')
        break
"""

"""
#Exercicio 06
lista_pares = []
lista_impares = []

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Números pares: {lista_pares}')
print(f'Números ímpares: {lista_impares}')
"""


#Exercicio 07


#Exercicio 08
































