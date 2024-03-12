from automovil import Automovil
from bicicleta import Bicicleta
from moto import Moto
from camion import Camion

def main():
    seat = Automovil(4, "blanco")
    trek = Bicicleta(2, "roja")
    kawasaki = Moto(2, "roja")
    rover = Camion(6, "blanco")

    seat.informacion()
    trek.informacion()
    kawasaki.informacion()
    rover.informacion()

if __name__ == "__main__":
    main()