#Exercicio 07
frase = input("Digite uma frase: ").upper()

lista_vogal = []
vogais = 'AEIOU'

for letra in frase:
    if letra in vogais:
        lista_vogal.append(letra)

for vogal in vogais:
    quantidade = lista_vogal.count(vogal)
    if quantidade > 0:
        print(f'A letra ({vogal}) apareceu {quantidade} vez(es)')