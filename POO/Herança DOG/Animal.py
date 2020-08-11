class Animal:
    def __init__ (self, Nome,Peso,Altura): 
        self._Nome = Nome
        self._Peso = Peso
        self._Altura = Altura
        self._Classe = None
        self._Especie =  None
    
    def Infos(self):
        print(f'\nNome: {self._Nome} \nPeso: {self._Peso} \nAltura: {self._Altura} \nClasse: {self._Classe} \nEspecie: {self._Especie}')
    
    def Comer(self):
        print(f"O {self._Especie} está comendo") 
    
    def Andar(self):
        print(f"O {self._Especie} está andando")