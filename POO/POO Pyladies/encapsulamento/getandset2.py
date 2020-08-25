class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.__Nome = nome
        self.__Qtd_membros = qtd_membros
        self.__Tem_homens = tem_homens
        self.__creators = {'Name':[],"E-mail":[]}
    def GetNome(self):
        return self.__Nome
    
    def SetNome(self,valor):
        self.__Nome = valor
    
    def SetCreators(self, name,email):
        self.__creators['Name'].append(name)
        self.__creators['E-mail'].append(email)
    
    def GetCreators(self):
        if self.__creators['Name'] == []:
            return None
        else:
            return self.__creators

pyladies_sanca = Pyladies("Pyladies Bauru", 10, True)
pyladies_sanca.SetCreators('Ana dulce', 'ana@blabla.com')

print(pyladies_sanca.GetCreators())