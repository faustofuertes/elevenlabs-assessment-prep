import os
os.system("clear")
# LOS METODOS MAS IMPORTANTES DE LAS LISTAS

#agregar un elemento a una lista
'''
lista1 = [1,2,3,4,5]
lista1.append(6)
print(lista1)

lista1.insert(1, '@')
print(lista1) # inserta un elemento en la posicion que le indiquemos y empuja a todos los demas a la derecha

lista1.extend(['s', 'e', 'x']) # CONCATENA AL FINAL DE LA LISTA 
print(lista1)

#eliminar un elemento de una lista
#eliminar la primera aparicion de un elemento en una lista
lista1.remove('x')
print(lista1)

#eliminar por INDICE
lista1.pop() #elimina y devuelve el ultimo elemento de la lista
print(lista1)

lista1.pop(1) #elimina por indice
print(lista1)

lista1.clear() #elimia todos los elementos de la lista
print(lista1)

#ordenar listas
numbers = [3, 2, 44,10, 1]
numbers.sort()
print(numbers)

#contar cuantas veces se repite un elementos
animals = ['🐶','🙊','🐹','🦁','🐶']
print(f'El 🙊 aparece {animals.count('🙊')} veces.')

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
list=[1,2,3,4,5]
# Añade el número 6 al final usando append().
list.append(6)
# Inserta el número 10 en la posición 2 usando insert().
list.insert(1, 10)
# Modifica el primer elemento de la lista para que sea 0.
list[0] = 0
print(list)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print(lista_a)
# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
print(lista_a)
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
lista_a.pop(3)
print(lista_a)
# Limpia completamente lista_b usando clear().
lista_a.clear()
print(lista_a)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
lista = [1,2,3,4,5,6,7,8,9,10]
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
del(lista[2:4])
print(lista)
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: 
lista = [5, 2, 8, 1, 9, 4, 7]
# Ordena la lista de forma ascendente usando sort().
lista.sort()
print(lista)
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
print(f'El numero 2 se encuentra {lista.count(2)} veces.')
# Comprueba si el número 7 está en la lista usando in.
if 7 in lista:
    print('El 7 se encuentra en la lista')
else:
    print('El 7 no se encuentra en la lista')

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números 
original = [1, 2, 3]
# Crea una copia de la lista original llamada copia_1 usando slicing.
copia_1 = original[:]
# Crea otra copia llamada copia_2 usando copy().
copia_2 = original.copy()
# Crea una referencia a la lista original llamada referencia.
referencia = original
referencia[0] = 10
print(f'{original}\n{copia_1}\n{copia_2}\n{referencia}')
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: 
fruits = ["Manzana", "pera", "BANANA", "naranja"]
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
fruits_sorted_keyinsensitive = sorted(fruits, key = str.lower)
print(fruits)
'''