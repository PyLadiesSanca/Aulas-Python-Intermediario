#Entrada dos números
entA,entB =input("Insira dois numeros aqui :)" ).split()
boolean = False

#Condicional
if int(entA) % int(entB) == 0:
    boolean = True

#Saída
if boolean:
    print('é divisivel')
else:
    print('Não é divisivel')