class Retangulo(object):

    def __init__(self):
        self.tipo ="Retangulo"
        print("criado um Retangulo")

class Circulo(object):

    def __init__(self):
        self.tipo ="Retangulo"
        print("criado um Retangulo")

class CalculadoraDeAreas(object):

    def __init__(self):
        self.figuras = []

    def adicionaRetangulos(self,retangulos):
        """metodo que serve para adicionar novas figuras na lista"""
        self.figuras.append(retangulos)

    def adicionaCirculos(self,circulo):
        """metodo que serve para adicionar novas figuras na lista"""
        self.figuras.append(circulo)

    def somaAreaDasFiguras(self):
        """metodo que serve para somar as areas dos retangulos que estao na lista """
        for figura in self.figuras:
            if(figura.tipo == "retangulo"):
                print("código que calcula a area do retangulo")
            if(figura.tipo == "circulo"):
                print("código que calcula a area do circulo")

            print("código que soma a nova area"+
                    "calculada com as areas dos anteriores")


r1 = Retangulo()
c1 = Circulo()
cal = CalculadoraDeAreas()
cal.adicionaRetangulos(r1)
cal.adicionaCirculos(c1)
cal.somaAreaDasFiguras()
