import pandas as pd

dados = pd.read_csv("Historico_pedidos.csv")

dados.to_json("Historico_pedidos.json", orient="records",  indent=4)