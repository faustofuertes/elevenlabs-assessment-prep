###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print('Comparacion de cadenas')
print('Manzana < pera ?:', 'manzana' < 'pera') # True: NO COMPARA POR LONGITUD, compara LEXICOGRAFICAMENTE