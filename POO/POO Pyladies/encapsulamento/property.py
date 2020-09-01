class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.__setado = False
        self.Nome = nome
        self.Qtd_membros = qtd_membros
        self.Tem_homens = tem_homens
        self.__setado = True

    @property #método get
    def Nome(self): 
        return f"o nome do capítulo é: {self.__Nome}"

    @Nome.setter
    def getNome(self, nome):
        if self.__setado == False:
            self.__Nome = nome
        else:
            x = input("Certeza que quer mudar o nome? (s/n) ")
            if x == 's':
                self.__Nome = nome
           
pyladies_bauru = Pyladies("Pyladies Bauru", 10, True)

pyladies_bauru.getNome = "Pyladies Bauru leste"
print(pyladies_bauru.Nome)


