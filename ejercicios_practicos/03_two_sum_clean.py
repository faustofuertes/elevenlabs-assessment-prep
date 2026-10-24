"""
Exercise 3 — Two Sum, assessment version

Create a function that receives a list of integers and a target.
Return the indices of two different elements whose sum equals the target.

Rules:
- The result must be a list [i, j] where i < j.
- If no valid pair exists, return None.
- Numbers may be repeated: [3, 3] with target 6 must return [0, 1].
- You may assume that, if a solution exists, there is only one valid pair.
- Solve it in one pass using a dictionary. Do not use two nested loops.

Examples:
- Input: [2, 7, 11, 15], 9
  Output: [0, 1]
- Input: [3, 2, 4], 6
  Output: [1, 2]
- Input: [3, 3], 6
  Output: [0, 1]
- Input: [], 1
  Output: None
- Input: [-3, 4, 3, 90], 0
  Output: [0, 2]
"""

# Write the function yourself below, including its name and parameters.
# Before calling it done, add and run your own print() statements.
# Test: empty, one element, duplicates, negative numbers, and no solution.

import os
os.system('clear')

def two_sum_target(num_list:list, target:int) -> list | None:
  # declaramos un dictionarie para guardar los key: num - value: index q VIMOS
  seen_dict = {}

  # iteramos la lista de numeros extrayendo index y numero
  for index, num in enumerate(num_list):

    # declaramos una variable missing (el numero que nos falta para llegar al target) que sale de la cuenta target - num de esa iteracion
    missing = target - num

    # nos fijamos si el numero que nos falta esta en nuestro seen_dict (dictionarie de los numeros que vimos)
    if missing in seen_dict:

      # si esta retornamos una lista con el value de ese numero encontrado en el seen_dcit (el index) y el index del num de esa iteracion
      return [seen_dict[missing], index]
    
    # si no esta registramos el index y el numero de esa iteacion en el dict
    seen_dict[num] = index
  
  return None

print(f'Input: [2, 7, 11, 15], 9\nOutput: {two_sum_target([2, 7, 11, 15], 9)}\n')
print(f'Input: [3, 2, 4], 6\nOutput: {two_sum_target([3, 2, 4], 6)}\n')
print(f'Input: [3, 3], 6\nOutput: {two_sum_target([3, 3], 6)}\n')
print(f'Input: [], 1\nOutput: {two_sum_target([], 1)}\n')
print(f'Input: [-3, 4, 3, 90], 0\nOutput: {two_sum_target([-3, 4, 3, 90], 0)}\n')

"""
Practice 2 — Does a target pair exist?

You receive a list of integers and a target. Return True if two different
elements in the list add up to the target. Otherwise, return False.

Rules:
- An element cannot be used twice unless it appears twice in the input.
- Solve it in one pass with a dictionary. Do not use two nested loops.
- An empty list and a list with one element return False.

Examples:
- Input: [2, 7, 11, 15], target = 9
  Output: True
- Input: [3], target = 6
  Output: False
- Input: [3, 3], target = 6
  Output: True
- Input: [1, 2, 3], target = 10
  Output: False
- Input: [-5, 2, 8], target = 3
  Output: True
"""
'''
# Write a new function below, including its name and parameters.

def two_sum_target(num_list:list, target:int) -> bool:
    nums_seen_dict = {}

    for index, num in enumerate(num_list):
        missing = target - num
        if missing in nums_seen_dict:
            return True
        nums_seen_dict[num] = index
    
    return False

#result = two_sum_target([2, 7, 11, 15], 9)
result = two_sum_target([3], 6)
#result = two_sum_target([3, 3], 6)
#result = two_sum_target([1, 2, 3], 10)
#result = two_sum_target([-5, 2, 8], 3)
if result:
    print('There a target pair.')
else:
    print('There is not a target pair.')
'''



"""
Practice 3 — Find target values

You receive a list of integers and a target. Return the first pair of values
that add up to the target as a list [first_value, second_value].

Return None if no valid pair exists.

Rules:
- Process the list from left to right.
- The first value in the returned pair must appear earlier in the input than
  the second value.
- A value cannot be reused unless it appears at least twice in the input.
- Solve it in one pass with a dictionary. Do not use two nested loops.

Examples:
- Input: [2, 7, 11, 15], target = 9
  Output: [2, 7]
- Input: [3, 2, 4], target = 6
  Output: [2, 4]
- Input: [3, 3], target = 6
  Output: [3, 3]
- Input: [1, 2, 3], target = 10
  Output: None
- Input: [-3, 4, 3, 90], target = 0
  Output: [-3, 3]
"""

# Write a new function below, including its name and parameters.

def two_sum_target(nums_list:list, target:int) -> list | None:
    nums_seen_dict = {}

    for num in nums_list:
        missing = target - num
        if missing in nums_seen_dict:
            return [missing, num]
        nums_seen_dict[num] = 1
    
    return None

print(two_sum_target([-3, 4, 3, 90], 0))