import Animal as an

class Cachorro(an.Animal):
    def __init__(self, Nome,Peso,Altura):
        super().__init__(Nome,Peso,Altura)
        self._Classe = "Mamífero"
        self._Especie = "Cachorro"
        

    def Latir(self):
        print('au au')

