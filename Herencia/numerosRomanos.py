class NumeroRomano:
    def __init__(self, numeroEntero):
        self.numeroEntero = numeroEntero

    def convertirARomano(self):
        tabla = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        resultado = ''
        for valor in tabla:
            while self.numeroEntero >= valor:
                resultado += tabla[valor]
                self.numeroEntero -= valor
        print(f"{self.numeroEntero} en números romanos es: {resultado}")

if __name__ == "__main__":
    primerNumero = NumeroRomano(354)
    primerNumero.convertirARomano()
