import random

numero = random.randint(0, 10)

palpite = int(input("Digite o número "))

if palpite < numero:
    print("O numero é maior")
    palpite = int(input("Digite outro número "))

    if palpite == numero:
        print("VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU KKKKKK")
else:
    print("O numero é menor")
    palpite = int(input("Digite outro número "))

    if palpite == numero:
        print("VOCÊ ACERTOU")
    else:
        print("VOCÊ ERROU KKKKKK")