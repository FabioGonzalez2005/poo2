from guagua import Guagua

def main():
    intercity = Guagua(asientos=50, ruedas=6)
    lanzaroteBus = Guagua(asientos=80, ruedas=8)

    intercity.desplazar(30)
    lanzaroteBus.desplazar(40, 60)

    intercity.informacion()
    lanzaroteBus.informacion()