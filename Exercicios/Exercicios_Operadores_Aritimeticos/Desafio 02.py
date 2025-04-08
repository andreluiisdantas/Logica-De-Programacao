#Desafio 2
capital = float(input('Digite o Capital inicial do investimento: '))
juros = float(input('Digite o valor do juros do investimento: '))
periodo = float(input('Digite o periodo do investimento: '))

resultao = capital * (1 + (juros/100)) ** periodo

print(f'O montante final será: R$ {resultao:.2f}')