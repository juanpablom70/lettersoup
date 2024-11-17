import json
#Buscar una palabra en la sopa de letras
def find_word(letter_soup, word): 
    #convertir las palabras a mayuscular
    word = word.upper()
    #definir las direcciones de la busqueda (abajo,arriba,izquierda,derecha y las 4 diagonales)
    nextTo = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    #obtener la dimension de las sopa de letras (numero de filas y de columnas)
    columnas = len(letter_soup[0])
    filas = len(letter_soup)

    #Iterar por cada posicion de la matriz
    for i in range(filas):
        for j in range(columnas):
            #se inicia la busqueda si se encuentra la primera letra de una palabra a buscar
            if letter_soup[i][j] == word[0]:
                #explorar las posiciones que se habian definido en la variable nexto
                for posx, posy in nextTo:
                    valid = True
                    #calcular las posiciones concecuentes en cada letra
                    for k in range(len(word)):
                        new_i = i + k * posx
                        new_j = j + k * posy
                        #se valida si la posicion esta dentro de la matriz y si coincide con la palabra que se espera que coincida, si no coincide se retornara un False, se parara la busqueda, se iniciara otra busqueda y si la palabra si concuerda se retornara un True
                        if (new_i < 0 or new_i >= filas or 
                            new_j < 0 or new_j >= columnas or 
                            letter_soup[new_i][new_j] != word[k]):
                            valid = False
                            break
                    if valid:
                        return True
    return False
#funcion para crear un diccionario que almacene las palabras esperadas junto a un True o un False dependiendo si la palabra esta o no en la sopa de letras
def find_words(letter_soup, words, output_path="output.json"):
    results = {}
    for word in words:
        #se asigna a la variable el valor de la funcion, pues la anterior funcion en la encargada de buscar la palabra
        results[word] = find_word(letter_soup, word)
    #se escriben los resultados en archivo.json
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)
#leer el archivo y separarlo en lineas
def get_file_content(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
#lista para sopa de lesttras y palabras
    letter_soup = []
    words = []
    is_word_section = False
#recorre las lineas en content y si ve que las palabras encontradas estan despues del --- se agregara a la lista words
    for line in content:
        line = line.strip()
        if line == "---": 
            is_word_section = True
        elif is_word_section:
            words.append(line)
        else:
            letter_soup.append(line)

    return letter_soup, words
#definir las rutas de archivo
file_path = "archivo.txt"
output_path = "output.json"
#generar sopa de letras y palabras
letter_soup, words = get_file_content(file_path)
#llamar a la funcion de buscar las palabras y generar el reporte
find_words(letter_soup, words, output_path)
print(f"Reporte generado en {output_path}")