class Pyladies:
    def __init__ (self, nome,tem_homens,nome_membros,data_criacao): 
        self.Nome = nome
        self.Qtd_membros = len(nome_membros)
        self.Tem_homens = tem_homens
        self.Nome_membros = nome_membros
        self.Data_Criacao = data_criacao
        
pyladies_araraquara = Pyladies("Pyladies ARARAQUARA", False,['Ana','Clara','priscila'],"04/08/2020")

print(pyladies_araraquara.Nome)
print(pyladies_araraquara.Qtd_membros)
print(pyladies_araraquara.Tem_homens)
print(pyladies_araraquara.Nome_membros)
print(pyladies_araraquara.Data_Criacao)