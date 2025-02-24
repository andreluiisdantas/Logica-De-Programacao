"""
#Exercicio 1


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))


soma = num1 + num2


print(f'\nA soma dos número é {soma}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 2
numero = int(input("Digite um numero "))


resultado = numero % 2


print(f'O número é impar: {resultado != 0}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 3
valor1 = int(input('Digite um numero '))
valor2 = int(input('Digite outro numero '))

print(f'O primeiro número é maior que três: {valor1 > 3}')
print(f'O segundo número é menor que quatro: {valor2 < 4}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 4
numero = int(input('Digite um número '))
resultado = (numero ** 2) ** 0.5
print(f'O valor absoluto é {int(resultado)}')

#Outra forma
numero = int(input('Digite um número '))
print(f'O valor absoluto é {abs(numero)}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 5
valor1 = int(input('Digite o primeiro número '))
valor2 = int(input('Digite o segundo número '))

resultado1 = valor1 % 2
resultado2 = valor2 % 2

print(f'O primeiro valor é par: {resultado1 == 0}')
print(f'O segundo valor é par: {resultado2 == 0}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 6
valor1 = int(input('Digite o primeiro número '))
valor2 = int(input('Digite o segundo número '))

print(f'O primeiro valor é negativo: {valor1 < 0}')
print(f'O segundo valor é negativo: {valor2 < 0}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 7
valor1 = int(input('Digite o primeiro número '))
valor2 = int(input('Digite o segundo número '))
valor3 = int(input('Digite o terceiro número '))

resultado = (valor1 + valor2 + valor3) / 3

print(f'A média dos valores é: {resultado:.2f}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 8
valor1 = int(input('Digite o primeiro número '))
valor2 = int(input('Digite o segundo número '))

print(f'O valor1 + 15 é igual valor2 * 3: {(valor1 + 15) == (valor2 * 3)}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 9
dividendo = int(input('Digite o dividendo '))
divisor = int(input('Digite o divisor '))

resultado = dividendo / divisor
resto = dividendo % divisor

print(f'O resultado da divisão é: {resultado}')
print(f'O resto da divisão é: {resto}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 10
celsius = int(input('Digite a temperatura em graus celsius: '))

fahrenheit = celsius * 1.8 + 32

print(f'Valor convertidor para Fahrenheit: {fahrenheit}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 11
altura = float(input(f'Digite sua altura em metros '))
peso = float(input(f'Digite seu peso em kilos '))

imc = peso / altura** 2

print(f'Seu IMC é: {imc:.2f}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 12
nota1 = float(input('Digite a primeira nota '))
peso1 = float(input('Digite o peso da primeira nota '))

nota2 = float(input('\nDigite a segunda nota '))
peso2 = float(input('Digite o peso da segunda nota '))

nota3 = float(input('\nDigite a terceira nota '))
peso3 = float(input('Digite o peso da terceira nota '))

resultado = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f'\nA média ponderada é: {resultado:.2f}')
"""

#----------------------------------------------------------------------------------#

"""
#Exercicio 13
numero = int(input('Digite um numero: '))
expoente = int(input('Digite o expoente: '))

resultado = numero ** expoente

print(f'O resultado de {numero} elevado a {expoente} é: {resultado}')
"""



"""
#Desafio 1
numero = int(input('Digite um número '))

resultado = numero ** (1/3)

print(f'A raiz cúbica de {numero} é: {resultado:.2f}')
"""

#----------------------------------------------------------------------------------#

"""
#Desafio 2
capital = float(input('Digite o Capital inicial do investimento: '))
juros = float(input('Digite o valor do juros do investimento: '))
periodo = float(input('Digite o periodo do investimento: '))

resultao = capital * (1 + (juros/100)) ** periodo

print(f'O montante final será: R$ {resultao:.2f}')
"""

