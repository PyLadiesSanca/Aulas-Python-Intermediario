class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.__Nome = nome
        self.__Qtd_membros = qtd_membros
        self.__Tem_homens = tem_homens
    
    def GetNome(self):
        return self.__Nome
    
    def SetNome(self,valor):
        self.__Nome = valor
    
pyladies_bauru = Pyladies("Pyladies Bauru", 10, True)

pyladies_bauru.SetNome('Bauru-Leste')

print(pyladies_bauru.GetNome())



#self.__Infos_Membros = dict





