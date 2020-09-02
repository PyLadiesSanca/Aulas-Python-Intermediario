class Pyladies:
    def __init__ (self, nome, qtd_membros,tem_homens): 
        self.Nome = nome
        self.Qtd_membros = qtd_membros
        self.Tem_homens = tem_homens
        self.Nome_membros = nome_membros
        self.Data_Criacao = data_criacao
        
pyladies_araraquara = Pyladies("Pyladies ARARAQUARA", 10, False,[Clara, Milena, Leticia],"04/08/2020")


print(pyladies_araraquara.Nome)
print(pyladies_araraquara.Qtd_membros)
print(pyladies_araraquara.Tem_homens)
print(pyladies_araraquara.Nome_membros)
print(pyladies_araraquara.Data_Criacao)