import os
os.system("clear")
# LISTAS
# secuencia mutable de elementos
# puede contener elementos de distintos tipos
'''
print('Crear listas')

lista1 = [1,2,3,4,5]
lista2 = ['uno','dos','tres']
lista3 = [1,'dos',3.3]
lista_vacia = []
lista_de_listas = [[1,2],[3,4]] # O MATRICES
matrix = [[1,2],[3,4]] # O MATRICES

print('Acceder a elementos por indice')
print(lista1[3])
print(lista1[-1]) # ACCEDE A LA ULTIMA POSICION, UNA MENOS DESDE LA ULTIMA

print(matrix[0][1])

# SLICING; REBANADO DE LISTAS
#print(lista[DESDE:HASTA:PASO]) PASO SERIA DE A CUANTOS SALTA
lista1=[1,2,3,4,5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:4]) # [1, 2, 3, 4] del primero al 4
print(lista1[1:]) # [1, 2, 3, 4, 5s] del 1 al ultimo
print(lista1[:]) # te crea una copia

print(lista1[::2])
print(lista1[::-1]) # LA INVERTIMOS

# Modificar una lista

lista1[0] = 120
print(lista1)

# añadir elementos a una lista

# forma lenta
lista1 = lista1 + [6,7,8]
print(lista1)

#forma rapida
lista1+=[9,10,11]
print(lista1)

print('EJERCICIOS\n\n')

#recuperar longitud de una lista
print('Longitud de la lista1: ', len(lista1))


# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print(mensaje[7:])

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
primera_posicion = numeros[0]
numeros[0] = numeros[4]
numeros[4] = primera_posicion
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sanguche = pan + ingredientes + pan_abajo
print(sanguche)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
lista+= lista
print(lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
lista = [10, 20, 30, 40, 50] # El centro es 30

centro = int(len(lista) / 2 + 1)
print(f'El elemento del centro se encuentra en la posicion: {centro} y es {lista[centro-1]}')

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]

lista[:3] = [lista[2],lista[1],lista[0]]
print(lista)
'''