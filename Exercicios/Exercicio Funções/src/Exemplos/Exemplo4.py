def tentar_mudar():
    a = 50 # Isso é uma nova váriavel local. Não muda a global.
    print(a) # Imprime 50

a = 7
tentar_mudar()
print(a) # Ainda imprime 7