class Cachorro:
    def __init__ (self, nome,Peso,Altura,Raca): 
        self.Nome = nome
        self.Peso = Peso
        self.Altura = Altura
        self.Raca = Raca
    
    def Latir(self):
        print('au au')
    
    def Comer(self):
        print("O cachorrro está comendo") 
    
    def Andar(self):
        print("O cachorro está andando")

    def infos(self):
        print(f'\nNome: {self.Nome} \nPeso: {self.Peso} \nAltura: {self.Altura} \nRaça: {self.Raca} ')

robertinho = Cachorro('robertinho',8.7, 0.87, 'Vira lata')

robertinho.Latir()
robertinho.Comer()
robertinho.Latir()
robertinho.Andar()
robertinho.infos()