alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("LOPAL-Aula11-ManipulacaoArquivo-Exercicios-Criptografado.txt", "r", encoding="utf-8") as file:
    conteudo_criptografado = file.read().lower()

deslocamento = 3
conteudo_descriptografado = ""

for letra in conteudo_criptografado:
    if letra in alfabeto:
        posicao_atual = alfabeto.index(letra)
        nova_posicao = (posicao_atual - deslocamento) % len(alfabeto)
        conteudo_descriptografado += alfabeto[nova_posicao]
    else:
        conteudo_descriptografado += letra

print(conteudo_descriptografado)

with open("Texto_Descriptografado.txt", "w", encoding="utf-8") as f:
    f.write(conteudo_descriptografado)
