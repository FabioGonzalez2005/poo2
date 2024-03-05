### Parámetro posiconal
def tipicaFuncion(unpar:int, dospar:int)->None:
#def tipicaFuncion(unpar:int, dospar:int, /)->None:          #Cuidadín con el caracter /
    pass

tipicaFuncion(3, 6)
#unpar = 3
#dospar = 6

### Parámetro con valor por defecto
def tipicaFuncion(unpar:int, dospar = 6:int)->None:
    pass

tipicaFuncion(3)
#unpar = 3
#dospar = 6

### Parámetro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->None:
    pass

tipicaFuncion(3, 6, 6, 6, content=3)

### Parámetro nominal
def tipicaFuncion(*,unpar:int, dospar:int)->None
    pass

tipicaFuncion(ospar = 6, unpar = 3)
#unpar = 3
#dospar = 6