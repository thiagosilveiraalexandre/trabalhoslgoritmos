from computador import Computador
from desktop import Desktop
from notebook import Notebook

def imprimirInformacoes(computadores):
    for computador in computadores:
        print(computador.getInformacoes())

desktop = Desktop("Desktop para trabalho", "Azul",9000,2500)
notebook = Notebook("Notebook ASUS","Branco",4000,20)
computadores = [desktop,notebook]
imprimirInformacoes(computadores)