def FuncaoDoida(*paramentro):

    lista = list(paramentro)
    lista.sort()
    lista = [l*-2 for l in lista]
    return lista

#principal
print(FuncaoDoida(1,4,2,6,8,4))