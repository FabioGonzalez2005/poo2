## Ejercicio 2

```mermaid
classDiagram
    note "Vehículo"
    Vehículo <|-- Automovil
    Automovil <|-- Camión
    Vehículo <|-- Bicicleta
    Bicicleta <|-- Moto

    Vehículo : +int ruedas
    Vehículo : +str color
    Vehículo: +info()
```
    

## Ejercicio 3
Escribir una clase que convierta un número entero en número romano

opción b: número romano a número entero