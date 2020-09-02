#introdução a get() e set() em código modularizado
class Pyladies:
    def __init__ (self, Nome, Qtd_membros, tem_homens,nome_membros,data_criacao): 
        self.__Nome = Nome
        self.__Qtd_membros = Qtd_membros
        self.__Tem_homens = tem_homens
        self.__Nome_membros = nome_membros
        self.__Data_Criacao = data_criacao
    
    def GetNome(self):
        return self.Nome
    
    def SetNome(self,valor):
        self.__Nome = valor
    
    def GetQtdMembros(self):
        return self.Qtd_membros
    
    def SetQtdMembros(self,valor):
        self.__Qtd_membros = valor
    
    def GetTem_homens(self):
        return self.Tem_homens
    
    def SetTem_homens(self,valor):
        self.__Tem_homens = valor