#Exercicio 08
import random

moeda = ['cara', 'coroa']
cara = 0
coroa = 0

while cara < 3 and coroa < 3:
    resultado = random.choice(moeda)
    print(f'Caiu o lado {resultado}')
    if resultado == 'cara':
        cara += 1
    else:
        coroa += 1

if cara < coroa:
    print("Caiu coroa mais vezes")
else:
    print("Caiu cara mais vezes")