import ply.lex as lex
from tkinter import *

# Palabras reservadas y tokens
palabra_reservada = {
    'fn': 'palabra_reservada',
    'cycle': 'palabra_reservada',
    'screen': 'palabra_reservada',
    'show': 'palabra_reservada',
    'when': 'palabra_reservada',
    'so': 'palabra_reservada',
    'run': 'palabra_reservada',
    'int': 'tipo',
    'string' : 'tipo',
}

tokens = list(palabra_reservada.values()) + [
    'variable',
    'identificador',
    'cadena',
    'numero',
    'incremento',
    'asignacion',
    'suma',
    'mayor_que',
    'mayor_igual',
    'punto',
    'dos_puntos',
    'punto_y_coma',
    'parentesis_a',
    'parentesis_c',
    'llave_a',
    'llave_c'
]

# Expresiones regulares para operadores y signos
t_suma = r'\+'
t_asignacion = r'='
t_mayor_que = r'>'
t_mayor_igual = r'>='
t_incremento = r'\+\+'
t_punto = r'\.'
t_dos_puntos = r'\:'
t_punto_y_coma = r'\;'
#t_comilla_doble = r'"|“|”'
t_parentesis_a = r'\('
t_parentesis_c = r'\)'
t_llave_a = r'\{'
t_llave_c = r'\}'
t_cadena = r'["“”][^"“”]*["“”]'


def t_variable(t):
    r'_[a-zA-Z_][a-zA-Z0-9]*'
    if t.value.upper() in palabra_reservada:
        t.value = t.value.upper()
        t.type = palabra_reservada[t.value]
    return t

def t_identificador(t):
    r'[a-z_][a-zA-Z0-9]*'
    if t.value.lower() in palabra_reservada:
        t.type = palabra_reservada[t.value.lower()]
    return t

def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_salto_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comentarios(t):
    r'\#.*'
    pass

def t_error(t):
    mensaje_error = f"Caracter no definido: '{t.value[0]}'"
    print(mensaje_error)
    a.append(mensaje_error)
    t.lexer.skip(1)

a = []

def analisis(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    a.clear()

    while True:
        tok = analizador.token()
        if not tok:
            break
        a.append(str(tok))
    return a

t_ignore = ' '
