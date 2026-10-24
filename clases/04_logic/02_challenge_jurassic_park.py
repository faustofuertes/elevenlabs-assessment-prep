"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios 
carnívoros (es decir, la suma de todos los números pares en la lista).
"""

import os
os.system("clear")

def count_carnivore_dinasour_eggs(number_list:list) -> int:
    count = 0
    for number in number_list:
        if number % 2 == 0:
            count+=number
        
    return count

egg_list = [4,12,6,34,2,6,77,8,2,3,4]
print(f'There are {count_carnivore_dinasour_eggs(egg_list)} eggs from carnivore dinosaurs 🦖.')