def idade(nasc):
    nasc = nasc.split("/")

    if int(nasc[1]) < 7: #mês
        return 2020 - int(nasc[2])
    elif int(nasc[1])> 7: #mês
        return 2020 - int(nasc[2]) - 1
    else:   
        if int(nasc[0]) <= 28: #dia
            return 2020 - int(nasc[2])
        elif int(nasc[0])>28: #dia
            return 2020 - int(nasc[2]) - 1

def censura(idade,cens):
    if idade >= cens:
        return True
    else:
        return False

#codigo principal    
nasc = input("Coloque sua data de nacimento **/**/****: ")
film = int(input("Qual é a sensura do filme: "))

x = censura(idade(nasc),film)
#print(x)
print("\n Seja bem vindo Marcos :D \n Você podê ir na sessão\n\n\n")


