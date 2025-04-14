"""
#Exercicio 01
lista = []

for i in range (10):
    lista.append(int(input("Digite um número")))
    i += 1

multiplo = 0
for numero in lista:
    if numero % 3 == 0:
        multiplo += 1
print(f'A quantidade de número multiplos de 3 na lista é: {multiplo}')
"""

"""
#Exercicio 02
senha = ''

while senha != 'Senha!123':
    senha = input("Digite uma senha: ")
    continue
print("Senha correta")
"""

"""
#Exercicio 03
opcao = True

while opcao:
    menu = input("Escolha a opção:\n(Entrar) (Sair) ").upper()

    if menu == 'ENTRAR':
        print("Entrando...")
    elif menu == 'SAIR':
        print("Saindo...")
        break
    else:
        print("Opção invalida")
"""

"""
#Exercicio 04
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

lista = []
multiplos = 0

if num1 < 0 or num2 < 0:
    print("Os números precisa ser positivos")
else:
    if num2 > num1:
        for x in range((num1 + 1), num2):
            for i in range(2, x):
                if x % i == 0:
                    multiplos += 1
            if multiplos == 0 and x > 1:
                lista.append(x)
            multiplos = 0
    else:
        if num1 > num2:
            for x in range((num2 + 1), num1):
                for i in range(2, x):
                    if x % i == 0:
                        multiplos += 1
                if multiplos == 0 and x > 1:
                    lista.append(x)
                multiplos = 0
print(f'Os números primos são {lista}')
"""

"""
#Exercicio 05
tentativa = 0

while tentativa < 3:
    senha = input("Digite a senha: ")
    tentativa += 1
    if senha != 'Senha!123':
        print(f'Senha incorreta! Você tem {3 - tentativa} tentativa(s)')
    else:
        print(f'Acesso liberado!')
        break
"""

"""
#Exercicio 06
lista_pares = []
lista_impares = []

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Números pares: {lista_pares}')
print(f'Números ímpares: {lista_impares}')
"""

"""
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
"""

"""
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
"""

"""
#Exercicio 09
tamanho = int(input("Digite a quantidade de numeros na lista: "))
lista = []
num_maior_media = []

for i in range(tamanho):
    i += 1
    num = int(input("Digite um número: "))
    lista.append(num)

media = sum(lista) / len(lista)
print(f'A média dos números é: {media}')

for i in range(len(lista)):
    if lista[i] > media:
        num_maior_media.append(lista[i])

print(f'O números acima da média é: {num_maior_media}')
"""

"""
#Exercicio 10
tamanho = int(input("Digite a quantidade de numeros na lista: "))
lista = []

for i in range(tamanho):
    i += 1
    num = int(input("Digite um número: "))
    lista.append(num)

maior_num = max(lista)
print(f'O maior número da lista é: {maior_num}')

lista.remove(maior_num)
maior_num = max(lista)

print(f'O segundo maior número da lista é: {maior_num}')
"""

"""
#Desafio 01
populacao = int(input("Digite o número inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução: "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade: "))
num_geracoes = int(input("Digite o número de gerações a serem simuladas: "))

taxa_reproducao = taxa_reproducao * 0.01
taxa_mortalidade = taxa_mortalidade * 0.01

for geracao in range(1, num_geracoes + 1):
    nascimentos = populacao * taxa_reproducao
    mortes = populacao * taxa_mortalidade
    populacao = populacao + nascimentos - mortes
    populacao = (int(populacao))
    print(f"Geração: {geracao} | Coelhos:{populacao}")

print("\nSimulação concluída!")
"""

"""
#Desafio 02
import random

palavras = [
    "abacaxi", "computador", "python", "girassol", "viagem", "brasil",
    "escola", "janela", "chocolate", "bicicleta", "telefone", "montanha",
    "oceano", "elefante", "cachorro", "amizade", "familia", "teclado",
    "violao", "livro", "pipoca", "chuva", "relampago", "noite", "manha",
    "sabedoria", "aventura", "floresta", "estrela", "foguete", "jardim",
    "panqueca", "quintal", "sapato", "formiga", "caderno", "noticia",
    "fantasma", "praia", "carnaval", "travesseiro", "melancia", "avião"
]

palavra_secreta = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra_secreta]

letras_erradas = []
tentativas_restantes = 6


while tentativas_restantes > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Letras erradas:", ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_restantes}")

    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
        print("Boa! Você acertou uma letra.")
    else:
        letras_erradas.append(letra)
        tentativas_restantes -= 1
        print("Letra errada!")

if "_" not in letras_descobertas:
    print("\nVocê acertou")
    print("Palavra correta:", palavra_secreta)
else:
    print("\nAcabou as tentativas")
    print("A palavra era:", palavra_secreta)

"""


























