"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.
"""
import os
os.system('clear')

nums = [4, 5, 6, 2]
goal = 8

'''
def find_first_sum(nums:list, goal:int) ->list or none:
    for i in range(len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]
    return None 
print (find_first_sum(nums, goal))
'''

# Mismo problema pero resuelto con dictionaries

def find_first_sum(nums_list:list, goal:int) -> list or none:
    # creas un dict
    seen = {}

    # recorres la lista de numeros extryendo index y valor
    for index, value in enumerate(nums_list):

        # declaras una variable missing (el valor que te falta para llegar al goal) 
        missing = goal - value

        # chequeas si missing esta en el dict seen
        if missing in seen:

            # si esta retornas el valor de key = missing y el index del num de es iteracion
            return [seen[missing], index]
            
        seen[value] = index 

    return None

print(find_first_sum(nums,goal))