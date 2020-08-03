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