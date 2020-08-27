class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.Nome = nome
        self.Qtd_membros = qtd_membros
        self.Tem_homens = tem_homens

    @property #método get
    def Nome(self): 
        return self._Nome

    @Nome.setter
    def Nome(self, nome):
       self._Nome = nome

   
pyladies_sanca = Pyladies("Pyladies Bauru", 10, True)

print(pyladies_sanca.Creators)


