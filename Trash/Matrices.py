def generar_matrix(filas, columnas):
    mi_lista_de_listas = []
    for numero in range(0, filas):
        mi_lista_de_listas.append([])
        for num in range(0, columnas):
            mi_lista_de_listas[numero].append(0)
    return mi_lista_de_listas


def matrix_to_string(matrix):
    result = ""
    for fila in matrix:
        result += str(fila) + "\n"
    return result


print(matrix_to_string(generar_matrix(6, 2)))