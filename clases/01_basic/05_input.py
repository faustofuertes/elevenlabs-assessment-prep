# Entrada de usuario - INPUT
# manera de que el usuario introduzca informacion

#print('Hola ! Como te llamas ? ')
#name = input()
#print(f'Te llamas: {name}')

# LA DIFERENCIA ES 
#name = input('Hola como te llamas ?\n')
#print(f'{name}! Encantado de conocerte')

# LOS INPUT SIEMPRE GUARDAN STRING ! HAY QUE CASTEARLOS !
#age = input('Cuantos años tienes? \n')
#print(f'Dentro de 20 años tendras: {int(age) + 20}')

print('Pedir multiples valores')
country, city = input('En que pais y ciudad vives? ').split()
print(f'Osea que vivis en {city}, {country}... interesante')