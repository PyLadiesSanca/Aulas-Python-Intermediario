class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.Nome = nome
        self.Qtd_membros = qtd_membros
        self.Tem_homens = tem_homens
    
    @property #método get
    def Nome(self): 
        return self.__Nome

    @Nome.setter
    def __Nome(self, nome):
       self.__Nome = nome
   
pyladies_bauru = Pyladies("Pyladies Bauru", 10, True)
pyladies_bauru.Nome = "Juliana"
print(pyladies_bauru.Nome)


