###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Fausto Fuertes\nMar del Plata")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(f'a = {type(a)}')
print(f'b = {type(b)}')
print(f'c = {type(c)}')
print(f'd = {type(d)}')
print(f'e = {type(e)}')

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(type(int('12345')))
print(int(3.99), type(int(3.99))) # BORRA TODOS DPS DEL PUNTO NO APROXIMA


print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

#name, age, height = input('Dame tu nombre, tu edad  y tu altura:\n').split()
#print(f'Te llamas {name}, tenes {age} años y medis {height}. O NO BROTHER')

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

numero_pi = round(3.1416)
print(f'El resultado es: {int(numero_pi / 2)}')