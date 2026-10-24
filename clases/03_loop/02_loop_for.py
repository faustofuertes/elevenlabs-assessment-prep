import os
os.system("clear")

# BUCLE FOR
'''
print('Iterar una lista')
lista = [1,2,3,4,5]
for numero in lista:
    print(numero)

# Permite iterar sobre cualquier cosa iterable
palabra = 'fufulame31'
for letra in palabra:
    print(f'{letra} -', end = " ") 

# enumerate()
frutas = ['mazana', 'pera', 'mandarina']
for index, fruta in enumerate(frutas):
    print(f'El indice de {fruta} es {index}')

# bucles anidados
letras = ['A','B','C']
numeros = [1,2,3]
for letra in letras:
    for numero in numeros:
        print(f'{letra} x {numero}')

# break
animales = ['perro','gato','raton','loro','pez','canario']
for idx, animal in enumerate(animales):
    if animal == 'loro':
        print(f'El loro esta escondido en la posicion {idx}')
        break

# continue
animales = ['perro','gato','raton','loro','pez','canario']
for animal in animales:
    if animal == 'loro':
        continue
    print(f'Animal: {animal}')

# comprension de listas
animales = ['perro','gato','raton','loro','pez','canario']
animales_upper = [animal.upper() for animal in animales]
animales_lower = [animal.lower() for animal in animales_upper]
print(animales_lower)


###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
total = 0
for numero in numeros:
    total+=numero
print(f'La media de `numeros` es: {total / len(numeros)}')


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 100, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numero_max = 0
for numero in numeros:
    if numero >= numero_max:
        numero_max = numero
print(f'El numero maximo es: {numero_max}')


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
nueva_lista = []
for palabra in palabras:
    if len(palabra) > 5:
        nueva_lista.append(palabra)
print(f'Asi queda la lista con palabras de mas de 5 letras: {nueva_lista}')


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["acasa", "arbol", "asol", "aelefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letra = input('Introduce una letra: ').lower()
cant = 0
for palabra in palabras:
    if letra in palabra[0]:
        cant +=1
print(f'{cant} palabras empiezan con la letra {letra}')
'''