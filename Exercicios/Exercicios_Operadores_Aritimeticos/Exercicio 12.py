#Exercicio 12
nota1 = float(input('Digite a primeira nota '))
peso1 = float(input('Digite o peso da primeira nota '))

nota2 = float(input('\nDigite a segunda nota '))
peso2 = float(input('Digite o peso da segunda nota '))

nota3 = float(input('\nDigite a terceira nota '))
peso3 = float(input('Digite o peso da terceira nota '))

resultado = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f'\nA média ponderada é: {resultado:.2f}')