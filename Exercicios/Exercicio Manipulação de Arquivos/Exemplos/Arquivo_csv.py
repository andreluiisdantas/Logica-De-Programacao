import csv

with open("produtos.csv", "w") as f:
    escrever = csv.writer(f)
    escrever.writerow(["Nome", "Preço"])
    escrever.writerow(["livro", 20])

with open("produtos.csv", "r") as f:
    produtos = csv.reader(f)
    for row in produtos:
        print(" ".join(row))