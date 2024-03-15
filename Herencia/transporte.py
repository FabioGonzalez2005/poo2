class Transporte:
    def __init__(self, ruedas:int, asientos:int):
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(x:int, y:int = 0) -> None:
        print ("Desplazando a: ", x, y)

    def informacion(self) -> None:
        print ("Ruedas:", self.ruedas, "Asientos:", self.asientos)

if __name__ == "__main__":
    main()
