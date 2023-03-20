import re
from typing import *

'''Analizador léxico del lenguaje IvoryMoon'''

def nombre_variable(texto:str) -> tuple[bool, str, str]:
    '''Identifica el nombre de la variable, retorna true 
    si lo encuntra así como el texto restante y el nombre 
    de la variable en sí'''
    resultado = re.match(r'[a-zA-Z]+', texto)
    if resultado:
        return True, texto[resultado.end():], resultado.group()
    else:
        return False, texto, None

def numero(texto:str) -> tuple[bool, str, str]:
    '''Retorna true si encuentra un número,
    además proporciona la string faltante y
    el valor encontrado'''
    resultado = re.match(r'\d+', texto)
    if resultado:
        return True, texto[resultado.end():], (" "+resultado.group())
    else:
        return False, texto, None

def color_RGB(texto: str) -> tuple[bool, str, str, str,str]:
    '''Retorna true si la función es RGB, el texto restante
    y los tres grupos de valores RGB en sí'''
    resultado = re.search(r'colorRGB\((\d{3}),(\d{3}),(\d{3})\)', texto)
    if resultado:
        return True, texto[resultado.end():], resultado.group(1), resultado.group(2), resultado.group(3)
    else:
        return False, texto, None, None, None
    
def color(texto:str) -> tuple[bool, str, str]:
    '''Retorna true si encuentra un color, proporciona
    la string faltante y el color encontrado en sí'''
    resultado = re.match(r'azul|rojo|negro|blanco', texto)
    if resultado:
        return True, texto[resultado.end():], resultado.group()
    else:
        return False, texto, None

def declaracion_variable(texto:str) -> tuple[bool, str, str,str]:
    '''Retorna true si el formato de declaración de variable es correcto
    además de la string faltante y el nombre y valor de la variable en sí'''
    if texto.startswith('$'):
        success1, rest1, nombre = nombre_variable(texto[1:])
        if success1:
            if rest1.startswith('='):
                success2, rest2, valor  = numero(rest1[1:])
                if success2:
                    return True, rest2, nombre, valor
    return False, texto, None, None

def mover_tortuga(texto:str) -> tuple[bool, str, str]:
    '''Retorna true si encuentra un enunciado de función valido,
    la string faltante y la función en sí'''
    resultado = re.match(r'arriba|abajo|izquierda|derecha', texto)
    if resultado:
        return True, texto[resultado.end():], resultado.group()
    else:
        return False, texto, None

def funcion_tortuga(texto:str) -> tuple[bool, str, str,str]:
    '''Verifica que la estructura de la función incluyendo el valor pasado
    sea correcto y retorna verdadero si lo es, además, proporciona la string
    faltante, la función a ejecutar y el valor pasado'''
    success1, rest1, comando = mover_tortuga(texto)
    if success1:
        if rest1.startswith('('):
            success2, rest2, valor = numero(rest1[1:])
            if success2:
                if rest2.startswith(')'):
                    return True, rest2[1:], comando, valor
    return False, texto, None, None

def cambiar_color_fondo(texto:str) -> tuple[bool, str]:
    '''Retorna true si encuentra un enunciado de cambio de color
    de fondo valido, además, retorna la string faltante'''
    if texto.startswith('cambiaColorDeFondo'):
        arg_start = texto.find('(')
        arg_end = texto.find(')')
        if arg_start != -1 and arg_end != -1:
            arg = texto[arg_start+1:arg_end]
            success1, rest1, valor1,valor2,valor3 = color_RGB(arg)
            if success1:
                return True, texto[arg_end+1:].strip()
            success2, rest2, valorColor = color(arg)
            if success2:
                return True, texto[arg_end+1:].strip(), valorColor
    return False, texto, None

def funcion_color(texto:str) -> tuple[bool, str, str]:
    '''Retorna verdadero si hay una expresión de color valida, además,
    proporciona el color a ejecutar'''
    success1, rest1, colorDeFuncion = color(texto)
    if success1:
        return True, rest1, colorDeFuncion
    success2, rest2, valor1, valor2, valor3 = color_RGB(texto)
    if success2:
        return True, rest2, ("colorRGB " + valor1 + " " + valor2 + " " + valor3)
    return False, texto, None

def repetir_funcion(texto):
    '''Esta no sirve :p'''
    if texto.startswith('repetir('):
        success1, rest1, valorRepeticion = numero(texto[8:])
        if success1:
            if rest1.startswith(')['):
                success2, rest2 = funcion_tortuga(rest1[2:])
                if success2:
                    if rest2.startswith(']'):
                        return True, rest2[1:], valorRepeticion
    return False, texto



def funcion_borrar(texto:str)->tuple[bool,str]:
    '''Retorna true si la función borrar es encontrada,
    además, proporciona la string faltante'''
    resultado = re.match(r'borrarTodo', texto)
    if resultado:
        return True, texto[resultado.end():]
    else:
        return False, texto

def linea_vacia(texto:str)->tuple[bool,str]:
    '''Retorna true si una línea vacia es encontrada,
    además, proporciona la string faltante'''
    resultado = re.match(r'\s+',texto)
    if resultado:
        return True, texto[resultado.end():]
    else:
        return False,texto


def funcion_orientar(texto:str)->tuple[bool,str,str]:
    '''Retorna true si la función orientar es encontrada,
    además, proporciona la string faltante y el valor de función'''
    if texto.startswith('girarRaton('):
        print("girar")
        success1, rest1, grados = numero(texto[10:])
        if success1:
            print(grados)
            if rest1.startswith(')'):
                return True, rest1[1:], grados
    return False, texto, None
def comentario(texto:str)->tuple[bool,str]:
    '''Detecta si existe un comentario en la línea
    y regresa true si lo detecta, además, proporciona la
    string faltante'''
    resultado = re.match(r'\s*#.*',texto)
    if resultado:
        return True, texto[resultado.end():]
    else:
        return False, texto



def sentencia(texto):
    success1, rest1, comando, valorVariable = declaracion_variable(texto)
    if success1:
        return True, rest1, comando, valorVariable
    success2, rest2 = repetir_funcion(texto)
    if success2:
        return True, rest2, "Repetir"
    success3, rest3, comandoFuncion, valorFuncion = funcion_tortuga(texto)
    if success3:
        return True, rest3, comandoFuncion, valorFuncion
    success4, rest4, comando = funcion_color(texto)
    if success4:
        return True, rest4, comando
    success5, rest5, valorColor = cambiar_color_fondo(texto)
    if success5:
        return True, rest5, ("colorFondo  " + valorColor)
    success6, rest6 = funcion_borrar(texto)
    if success6:
        return True, rest6, "borrar"
    success7, rest7= linea_vacia(texto)
    if success7:
        return True, rest7
    success8, rest8, grados = funcion_orientar(texto)
    if success8:
        return True, rest8, ("orientar " + grados)
    success9, rest9 = comentario(texto)
    if success9:
        return True, rest9
    return False, texto
