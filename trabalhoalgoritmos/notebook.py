from computador import Computador
class Notebook(Computador):
    def __init__(self, modelo, cor, preco,tempo_de_bateria):
        super().__init__(modelo, cor, preco)
        self.__tempo_de_bateria = tempo_de_bateria
    
    def getInformacoes(self):
        return f"{super().getInformacoes()}" + f"\n tempo da bateria:{self.__tempo_de_bateria}"
    
    def cadastrar(self, modelo, cor ,preco , tempo_de_bateria):
        return super().cadastrar()
        self.modelo = modelo 
        self.cor = cor 
        self.preco = preco
        self.tempo_de_bateria = tempo_de_bateria
