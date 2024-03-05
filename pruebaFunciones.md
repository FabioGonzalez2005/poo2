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

### Ejercicio 3
def myDiv(id:str, *clas:str, content:str)->str:
    resultado = ''
    resultado += '<div id="' + id + '" '

    if len (clas) != 0:
        resultado += 'class = "'

        for e in clas:
            resultado += e + ','

        resultado += '"' 

    resultado += '>' + content + '</div>'

    return resultado


### Ejercicio 5
def myScrip(*src:str)->str:

Función que tiene como entrada un número indeterminado de cadenas de caracteres
y como salida de una cadena de caracteres. Probablemente transforma las entradas en la salida.
