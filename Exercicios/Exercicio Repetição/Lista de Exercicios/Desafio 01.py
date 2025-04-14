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