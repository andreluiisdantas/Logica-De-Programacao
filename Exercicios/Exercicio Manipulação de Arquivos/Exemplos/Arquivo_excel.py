import pandas as pd

df = pd.DataFrame(
    {
        "Produto": ["Celular"],
        "Quantidade": [10]
    }
)

df.to_excel("vendas.xlsx", sheet_name="vendas", index=False)
print(pd.read_excel("vendas.xlsx", sheet_name="vendas"))

