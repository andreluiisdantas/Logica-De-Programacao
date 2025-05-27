with open("meu_arquivo.txt", "w") as file:
    file.write("Olá mundo!\n")
    file.write("Python é divertido")

with open("meu_arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)
