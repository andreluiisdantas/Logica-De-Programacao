def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f'A média de {nota1} e {nota2} é {media}')

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

calcular_media(nota1, nota2)