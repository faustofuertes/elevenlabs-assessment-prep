# Las variable sirven para guardar datos en memoria
# Python es un lenguage de tipado dinamico y de tipado fuerte

name = "Fufulame"
print(name)

name = 'fufabiendezaza'
print(name)

# TIPADO DINAMICO
# el tipo de dato se determina en tiempo de ejecucion
print(type(name))

# Se puede cambiar el tipo de dato en tiempo de ejcucion
age = 32
print(type(name))

# Tipado FUERTE: Python no realiza conversiaones de tipo de manera automatica
#print(10  + "1") # esto revienta

print(f'Hola me llamo {name}, tengo {age - 10} años')

# No recomendada forma de asignar variables

age, name, sex = 32, 'fufulame31', 'man'
print(f'Me llamo {name}, soy un {sex} y tengo {age} años.')

# Convenciones de nombres de variables

nombre_y_apellido = 'fufulame' # SNAKE CASE
MI_CONSTANTE = 3.1416 # uppercase -> para falsa constante