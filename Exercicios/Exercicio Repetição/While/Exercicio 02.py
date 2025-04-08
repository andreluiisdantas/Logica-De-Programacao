num = 0
qtd_numeros = 0

while qtd_numeros < 5:
    qtd_numeros += 1
    novo_num = num

    num = int(input("Digite um número"))

    if novo_num > num:
        num = novo_num
print("O maior número é: ",num)