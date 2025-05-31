import pandas as pd

dados = pd.read_excel("Historico_pedidos.xlsx")

dados.to_csv("Historico_pedidos.csv", index=False)