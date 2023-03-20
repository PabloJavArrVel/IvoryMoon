from analizadorLexico import *
comandos = []

def parser_linea(linea):
    # Eliminar espacios en blanco al principio y al final de la línea
    linea = linea.strip()
    # Comprobar si la entrada es una sentencia válida
    argsSentencia = sentencia(linea)
    if argsSentencia == True:
        return True
    # Si la sentencia es válida y no hay nada sobrante, entonces la entrada es correcta
    if len(argsSentencia) == 4:
        success, rest, comando, valor = sentencia(linea)
        if success and len(rest) == 0:
            comandos.append(comando+valor)
            return True
        else:
            return False
    elif len(argsSentencia) == 3:
        success, rest, comando = sentencia(linea)
        if success and len(rest) == 0:
            comandos.append(comando)
            return True
        else:
            return False
    elif len(argsSentencia) == 2:
        return True

def parserIvory(programa):
    # Separar el programa en una lista de líneas
    lineas = programa.split("\n")
    iterador = 0
    # Iterar sobre cada línea del programa
    for linea in lineas:
        iterador += 1
        # Aplicar la lógica del parser a la línea
        if not parser_linea(linea):
            # Si la línea no es válida, imprimir un mensaje de error y salir del programa
            return iterador
    # Si todas las líneas del programa son válidas
    return comandos
