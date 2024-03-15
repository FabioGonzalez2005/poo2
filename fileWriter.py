class fileWriter:
    def __init__(self, fileName:str)->None:
        self.fileName = fileName

    def write(self, mensaje:str)->str:
        with open(self.fileName, 'w') as file:
            file.write(mensaje)
        
    def read(self)->str:
        with open(self.fileName, 'r') as file:
            return file.read()

if __main__ == "__main__":
    main()