import os
os.system('clear')

# 03 - Range
# Funcion que permite crear una secuencia de numeros, util para for NO ES UNA LISTA
# range(999) NO CREA UNA LISTA DEL 0 al 999 crea un rango y te da los numeros 'bajo demanda'
'''
print('Range()')

nums = range(5) # del 0 al 5
nums  = range(2,5) # del 2 al 5

for num in nums:
    print(num)

# range (inicio, fin, paso)
for num in range(0,1000,5):
    print(num)
for num in range(10,0,-1):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(f'{list_of_nums}')

for _ in range(5):
    print('Hacer cinco veces algo.')

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
contador = 1
for _ in range(10):
    print(contador)
    contador +=1


# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
contador = 1
for _ in range(20):
    if contador % 2 != 0:
        print(contador)
    contador+=1

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for num in range(5,50):
    if num %5 == 0:
        print(num)


# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for num in range(10,0,-1):
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
total = 0
for num in range(1,101):
    total+=num
print(f'El total de la suma de los numeros es: {total}')
'''

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = 0
while numero <=0:
    try:
        numero = int(input('Porfavor introduci un numero positivo: '))
    except:
        print('Error, porfavor introduci un numero positivo.')

for num in range(1,11):
    print(f'{num} x {numero} = {num * numero}')