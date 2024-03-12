class Vehiculo:
    def __init__(self, ruedas:int, color:str):
        self.ruedas = ruedas
        self.color = color

    def informacion(self) -> None:
        print ("Ruedas:", self.ruedas, "Color:", self.color)

if __name__ == "__main__":
    main()