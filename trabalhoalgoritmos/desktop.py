from computador import Computador
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        return super().getInformacoes() + f"\n Potencia da Fonte:{self._potenciaDaFonte}"
    
    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        return super().cadastrar()
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.potenciaDaFonte = potenciaDaFonte