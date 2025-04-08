#-----------Exercicio 6-----------#

hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

if hora >= 0 and hora < 24 and minutos >= 0 and minutos < 60 and segundos >= 0 and segundos < 60:
    print("Horário valido")
else:
    print("Horário inválido")