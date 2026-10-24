import os
os.system("clear")

# FUNCIONES!
# bloques de codigo reutilizables y parametrzables para hacer tareas especificas

''' Definicion de una funcion
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstrnig
    # cuerpo de una funcion
    return valores_de_retorno #opcional

nombre_de_la_funcion(argumento1, argumento2, ...)

# el parametro es lo que acepta la funcion
# el argumento es el valor que se envia a la funcion
'''

def saludar(nombre):
    print(f'Hola {nombre}! Como estas ?')

gente_a_saludar = ['fufulame31','valenbiendevago','beigelporciento','nicoasterisco']
for gente in gente_a_saludar:
    saludar(gente)

# DOCUMENTAR UNA FUNCION
def restar (a:int, b:int):
    '''Resta dos numeros y devuelve el resultado'''
    return int(a - b)

print(restar.__doc__)

# parametros por defecto
def multiplicar_por_dos(a:int,b=2):
    '''Esta funcion recibe un numero y lo multiplica por dos'''
    return int(a*b)

print(multiplicar_por_dos(10,10))

# argumentos por posicion
def describir_persona(nombre:str,edad:int,sexo:str):
    '''Esta funccion recibe 3 paramtros y describe a una persona'''
    print(f'Hola, mi nombre es {nombre}, soy {sexo} y tengo {edad} años.')

# parametros posicionales
# llegan tal cual el orden que se mandan
describir_persona('fufulame31', 22,'hombre')

# parametros nombrados
describir_persona(edad=22, sexo='hombre',nombre='fufulame31')

# argumento de longitud de variables (*args)
# ITERAR PARAMETROS
# ARGUMENTOS DINAMICOS
def sumar_numeros(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma
print(sumar_numeros(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))

# argumentos de clave-valor variables (**kwargs)
def mostrar_informacion_de(**kwargs):
    for key, value in kwargs.items():
        print(f'Key: {key}\nValue: {value}')

mostrar_informacion_de(nombre='fufulame31', edad=22, sexo='poco')
print('\n')
mostrar_informacion_de(apellido='lame', seniority='semi-senior', company='laburen.com')
print('\n')
mostrar_informacion_de(nombre='fufulame31', edad=22, sexo='poco')
print('\n')