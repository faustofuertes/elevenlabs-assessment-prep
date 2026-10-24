import os
os.system("clear")

# BUCLES WHILE
# PERMITE EJECUTAR UN BLOQUE DE CODIGO SIEMPRE QUE SE CUMPLA UNA CONDICION

'''
print('Bucle while')

contador = 1

while contador != 0:
    contador += 1
    print(contador)
    if contador == 10:
        break ## sale del bucle


while contador < 100:
    print(contador)
    contador +=1
    if contador%5==0:
        print(f'El {contador} es multiplo de 5.')
        break

while contador < 100:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

print('Bucle while con else')
while contador < 100:
    print(contador)
    contador +=1
else:
    print('El bucle se termino')

print('Pedirle al usuario informacion')

number = -1
while number < 0:
    number = int(input('Ingresa un numero positivo: '))
    if number < 0:
        print('El numero tiene que ser positivo, intenta denuevo.-1')
else:
    print(f'Gracias! por escribir el {number}') 


number = -1
while number < 0:
    try:
        number = int(input('Ingresa un numero positivo: '))
        if number < 0:
         print('El numero tiene que ser positivo, intenta denuevo.')
    except:
        print('Error: porfavor ingresa un numero positivo.')

else:
    print(f'Gracias! por escribir el {number}') 


###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
contador = 1
while contador <= 10:
    print(contador)
    contador +=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 0
suma = 0
while contador <= 20:
    contador+=1
    if contador % 2 != 0:
        continue
    suma += contador
print(f'La suma de todos los numeros pares entre 1 y 20 es: {suma}')


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
number = 0

while number <= 0:
    try:
        number = int(input('Porfavor ingrese un numero entero positivo: '))
    except:
        print('Error: solo se admiten numeros.')

contador = 1
factorial = 1
while contador <= number:   
    factorial = factorial * contador
    contador += 1
print(f'El factorial de {number} es: {factorial}')
    
'''
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

def validate_password(password:str):
    '''This function validates if a password is larger than 8 characters.'''
    is_valid = False
    if len(password) > 8:
        is_valid = True
    return bool(is_valid)


password = input('Please enter your password: ')
while validate_password(password) == False:
    password = input('Please enter your password: ')
    is_valid = validate_password(password)
    if is_valid == True:
        break
print(f'Password of {len(password)} characters set succesfully !')


'''
# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
numero = int(input('Porfavor introduci un numero: '))
contador = 1
while contador <= 10:
    print(f'{numero} * {contador} = {numero * contador}')
    contador += 1
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
'''