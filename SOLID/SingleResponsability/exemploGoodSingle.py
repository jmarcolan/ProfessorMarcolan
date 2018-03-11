    #código 2-classes seguindo o principio da responsabilidade única
class JogoProcessamento(object):
    def __init__(self):
    """ contrutor de um objeto que contem a lógica do jogo"""
        print("inicializou a classe!")

    def calcularFisica(self):
        print("calculando a física do jogo")


class JogoPersistencia(object):
    def __init__(self):
    """contrutor de um objeto que lida com a persistencia dos dados desse jogo"""
        print("inicializou a classe!")

    def gravarArquivo(self):
        print("gravando o estado corrente do jogo")

    def carregarArquivo(self):
        print("carrega o estado corrente do jogo")
