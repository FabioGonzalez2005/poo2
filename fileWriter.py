class fileWriter:
    def __init__(self, fileName:str)->None:
        self.fileName = fileName
        self.i = open(self.fileName, "w+", "r")

    def write(self, mensaje:str)->str:
        self.i.write(mensaje)
        
    def read(self)->str:
        self.i.readlines()

    def close(self)->str:

if __main__ == "__main__":
    main()