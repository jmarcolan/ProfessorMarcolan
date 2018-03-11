
class Formas():
    """Classe mais abstrata"""
    def calculaArea(self):
        pass

class Retangulo(Formas):
    """Classe concreta """
    def __init__(self):
        self.tipo ="retangulo"
        print("retangulo")

    def calculaArea(self):
        print("area do retangulo")

class Circulo(Formas):
    """Classe concreta """
    def __init__(self):
        self.tipo ="circulo"
        print("circulo")

    def calculaArea(self):
        print("area do circulo")

class CalculadoraDeAreas():
    def __init__(self):
        self.figuras = []

    def adicionaFigura(self,figura):
        self.figuras.append(figura)

    def calulaAreaDasFiguras(self):
        for figura in self.figuras:
            figura.calculaArea()
            print("soma da area nova com as antigas")


r1 = Retangulo()
# criado um Retangulo
c1 = Circulo()
# criado um Retangulo
cal = CalculadoraDeAreas()
cal.adicionaFigura(r1)
cal.adicionaFigura(c1)
cal.calulaAreaDasFiguras()
