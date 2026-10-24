"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""
import os
os.system('clear')
'''
# MI MANERA
def count_characters(string:str, character:str):
    This function count how many of an exact characters appears on a string.
    count = 0
    for c in string:
        if c == character:
            count+=1
    return int(count)

if count_characters('Reed Richards','R') != count_characters('Johnny Jtorm','J'):
    print('Theres is no balance beetwen these two.')
else:
    print('There is balance beetwen these two.')

string = 'Reed Richards'
character = 'R'
print(f'There is {count_characters(character=character, string=string)} [{character}] in the word {string}.')
print('\n')
string = 'Johnny Storm'
character = 'J'
print(f'There is {count_characters(character=character, string=string)} [{character}] in the word {string}.')
'''

# Midu manera
def check_balance(text:str):
    '''This function check the balance beetwen these two texts'''
    count_r = text.count('R')
    count_j = text.count('J')
    return bool(count_r == count_j)

text = 'RRJJ'
if check_balance(text) == True:
    print('There is balance.')
else:
    print('There is no balance.')

