#-----------Exercicio 10-----------#

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 < nota2 and nota1 < nota3:
    media = (nota2 + nota3) / 2
    print(f'A média das notas é: {media}')
elif nota2 < nota1 and nota2 < nota3:
    media = (nota1 + nota3) / 2
    print(f'A média das notas é: {media}')
else:
    media = (nota1 + nota2) / 2
    print(f'A média das notas é: {media}')