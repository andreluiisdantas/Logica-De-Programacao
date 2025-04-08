#-----------Exercicio 2-----------#

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / (altura**2)

if IMC < 18.5:
    print("Baixo Peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Obesidade")
elif IMC < 40:
    print("Obesidade mórbida")
else:
    print("Obesidade mórbida II")