y = 20 # Varaivel Global

def funcao():
    print(y) # Pode acessar o valor global


funcao()
print(y)

# Pode ser utilizada dentro da função mas o valor não pode ser alterado exceto com "global" antes da varaivel, descrito no Exemplo 3.