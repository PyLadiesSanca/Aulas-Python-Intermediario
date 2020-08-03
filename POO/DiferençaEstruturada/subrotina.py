#Entrada dos números
def entrada():
    entA,entB =input("Insira dois numeros aqui :) " ).split()
    return entA,entB

#Condicional
def conditional(entA, entB):
    return int(entA) % int(entB) == 0

#Resultado
def resultado(r):
    if r:
        print('é divisivel')
    else:
        print('Não é divisivel')
        
#Código principal 
A, B= entrada()
result = conditional(A,B)
resultado(result)