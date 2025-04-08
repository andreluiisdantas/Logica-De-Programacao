#---------------------------Exercicio 3----------------------------------#

num = int(input("Digite um número: "))
qtd = num

if num == 0:
    print(f"A fatorial é 1")

elif num < 0:
    print(f"A fatorial de número negativo não é definido")

else:
    while qtd > 1:
        qtd -= 1
        num = num * qtd
    print(f'A fatorial é {num}')
"""
#---------------------------Outra Opção----------------------------------#

num = int(input("Digite um número: "))

fatorial = 1
i = 1
while i <= num:
    fatorial *= i
    i += 1
    print(f'O fatorial do número é: {fatorial}')
    print(f"A fatoria é {num}")
"""