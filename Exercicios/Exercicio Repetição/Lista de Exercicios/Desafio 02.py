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
