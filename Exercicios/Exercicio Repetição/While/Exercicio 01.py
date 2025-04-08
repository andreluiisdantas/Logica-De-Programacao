#---------------------------Exercicio 1----------------------------------#

num = int(input("Digite um número de 5 a 10: "))

if num < 5 or num > 10:
   print("O número menor que 5")
elif num > 10:
    print("O número maior que 10")
else:
    while num > 0:
        print(num)
        num = num - 1