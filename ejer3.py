def myDiv(id:str, *clas:str, content:str)->str:
    resultado = ''
    resultado += '<div id="' + id + '" '

    if len (clas) != 0:
        resultado += 'class = "'

        for e in clas:
            resultado += e + ','

        resultado += '\b\b"'

    resultado += '>' + content + '</div>'

    return resultado

def main():
    print(myDiv("midiv", "bt_h1", "row", "clear", content="Lorem ipsum"))

if __name__ == "__main__":
    main()