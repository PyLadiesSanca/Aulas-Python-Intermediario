#neste código mostraremos por que utilizar metodos get e set para
#a obtençao e modificaçao do atributo se tornar complexa como queira
class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.__Nome = nome #privado
        self.__Qtd_membros = qtd_membros #privado
        self.__Tem_homens = tem_homens #privado
        #supondo que criei um dicionário para os fundadores do capitulo:
        self.creators = {'Name':[],"E-mail":[]} #publico
    
    def SetCreators(self, name,email): #atributos sendo modificados
        print("Seus atributando foram setados")
        self.creators['Name'].append(name)
        self.creators['E-mail'].append(email)
    
    def GetCreators(self): #obtendo o atributo
        if self.creators['Name'] == []:
            return None
        else:
            return self.creators

    def GetNome(self):
        return self.__Nome
    
    def SetNome(self,valor):
        self.__Nome = valor.capitalize()

pyladies_sanca = Pyladies("PyLadies Sanca", 10, True)

pyladies_sanca.creators['Name'].append('Ana Dulce')
pyladies_sanca.creators['E-mail'].append('ana@blabla')

pyladies_sanca.SetNome("SAO CARLOS")

pyladies_sanca.SetCreators('Juliana Karoline', 'juk@blabla.com')
print(pyladies_sanca.GetCreators())
print(pyladies_sanca.GetNome())

