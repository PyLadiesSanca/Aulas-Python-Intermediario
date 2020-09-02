import Animal as an #importanto classe mãe

class Gato(an.Animal): #classe filha
    def __init__(self, Nome,Peso,Altura):
        super().__init__(Nome,Peso,Altura)
        self._Classe = "Mamífero"
        self._Especie = "Gato"
        
    def Miar(self):
        print('miau')

    def Ronronar(self):
        print('rsrsrsrsr')
