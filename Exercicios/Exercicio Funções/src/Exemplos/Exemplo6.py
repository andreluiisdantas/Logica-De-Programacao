def aumentar_contador():
    global contador
    contador += 1 # Alterando o valor

contador = 0
aumentar_contador()
print(contador)