class FileWriter:
    def __init__(self, fileName:str)->None:
        self.fileName = fileName
        self.i = open(self.fileName, "w+", "r")

    def write(self, mensaje:str)->str:
        self.i.write(mensaje)
        
    def read(self)->str:
        return self.i.readlines()

    def close(self)->str:
        self.i.close()

def main():
    prueba = FileWriter("fileWriter.txt")
    prueba.write("Hola")
    prueba.close()

    prueba = FileWriter("fileWriter.txt")
    prueba.read()
    prueba.close()

if __name__ == "__main__":
    main()