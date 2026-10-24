# SENTENCIAS CONDICIONALES
# EJECUTA CODIGO SI SE CUMPLEN CIERTSA CONDICIONES

import os
os.system('clear')

#cant_generos = int(input('Cuantos generos hay?\n'))
'''
#if cant_generos == 2:
#    print('Correcto')
#else:
#    print('Incorrecto')

edad = 18
if edad >= 18:
    print('Sos mayor de edad.')
else:
    print('Sos menor de edad.')

print('Sentencia condicional ELIF')

nota = 3
if nota >=9:
    print('Excelente nota!')
elif nota >=7:
    print('Buena nota')
else:
    print('Desaprobado')

# && -> and
# || -> or
print('Condiciones multiples')
age = 18
tiene_carnet = True

if age >= 18 and tiene_carnet == True:
    print('Estas autorizado para conducir.')
else:
    print('No estas autorizado para conducir.')

tiene_carnet = True
esta_ebrio = True

if esta_ebrio != False or tiene_carnet != True:
    print('No estas autorizado para conducir.')

tiene_carnet = False
esta_ebrio = False

if esta_ebrio or not tiene_carnet:
    print('No estas autorizado para conducir.')


print('\nAnidar condicionales')
edad = 17
tiene_dinero = False

if edad >= 18:
    if tiene_dinero:
        print('Pasa a la discoteca brother')
    else:
        print('Los secos no pueden pasar')
else:
    print('Los menores no pueden pasar')

if edad < 18:
    print('Los menores no pueden pasar')
elif tiene_dinero:
    print('Pasa a la discoteca brother')
else:
    print('Los secos no pueden pasar')

numero = 5
el_numero_es_3 = numero == 3

if el_numero_es_3:
    print('El numero es 3')
else:
    print('El numero no es 3')


print('Condicion ternaria')
# es una forma consisa de hacer if-else
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple]

edad = 18
print('Es mayor de edad') if edad >= 18 else print('Es menor de edad') 


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

#print('Introduce a: ', end='')
#a = int(input())
#print('Introduce b: ', end='')
#b = int(input())

#if a > b:
#    print('A es el mas grande')
#elif a == b:
#    print('Son iguales')
#else:
#    print('B es el mas grande')


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

#print('Introduce el numero A: ', end='')
#a = int(input())
#print('Introduce la operacion (+, -, *, /): ', end='')
#operacion = input()
#print('Introduce el numero B: ', end='')
#b = int(input())

#if operacion == '+':
#    print(f'Resultado: {a + b}')
#elif operacion == '-':
#    print(f'Resultado: {a - b}')
#elif operacion == '*':
#    print(f'Resultado: {a * b}')
#elif operacion == '/':
#    print(f'Resultado: {a / b}')
#else:
#    print('Algo hiciste mal pa')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = int(input('Introduci una año: '))

if (anio % 4) == 0 and not :
    print('Es bisiesto')
elif (anio % 100 ) == 0 and (anio % 400) != 0:
    print('No es bisiesto')
'''


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

#edad = int(input('Introduci tu edad:'))

#if edad <= 2:
#    print('Sos un bebe')
#elif edad <= 12:
#    print('Sos un Niño')
#elif edad <= 17:
#    print('Sos un Adolescente')
#elif edad <= 64:
#    print('Sos un Adulto')
#else:
#    print('Sos un Adulto mayor')

def categorizar_edad(edad:int):
    '''Esta funcion recibe una edad y la categoriza entre: bebe - niño - asolescente - adulto - adulto mayor'''
    categoria = ''
    if edad < 2:
        categoria = 'bebe'
    elif edad < 12:
        categoria = 'niño'
    elif edad < 17:
        categoria = 'adolescente'
    elif edad < 64:
        categoria = 'adulto'
    else:
        categoria = 'adulto mayor'
    return str(categoria)

def pedir_edad():
    '''Esta funcion pide y devuelve una edad valida'''
    edad = 0
    while edad <= 0:
        try:
            edad = int(input('Ingresa una edad mayor a 0 : '))
        except:
            print('Porfavor ingresa una edad valida')
    return int(edad)

edad = pedir_edad()
print(f'La edad que ingresas corresponde a un {categorizar_edad(edad)}')
