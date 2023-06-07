from abc import  ABCMeta , abstractmethod
class Computador(metaclass=ABCMeta):
    def __init__(self, modelo,cor,preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return f"modelo:{self.modelo} \n cor:{self.cor} \n preco:{self.preco}"
    
    @abstractmethod
    def cadastrar(self):
        pass