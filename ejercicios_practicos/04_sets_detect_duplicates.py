"""
Mini topic — Python sets

A set is a collection that stores each value only once. For this assessment,
use it when you need to answer: "Have I already seen this value?"

The only syntax you need now:

seen = set()          # create an empty set
seen.add(value)       # add a value
value in seen         # True if the value is already in the set

Do not use a set when you need duplicates or the original order as output.
For that, use a list as well.
"""


"""
Exercise 1 — Detect duplicate numbers

You receive a list of integers. Return True if any number appears more than
once. Otherwise, return False.

Rules:
- An empty list returns False.
- A list with one number returns False.
- Negative numbers are valid.
- Use a set. Do not use list.count() or two nested loops.

Examples:
- Input: [1, 2, 3, 1]
  Output: True
- Input: [1, 2, 3, 4]
  Output: False
- Input: []
  Output: False
- Input: [-1, 0, 5, -1]
  Output: True
"""

# Write the function yourself below, including its name and parameters.
# Before coding, answer: at which exact moment can you know there is a duplicate?
'''
def check_duplicated(nums_list:list) -> bool:
  nums_set = set(nums_list)
  if len(nums_set) == len(nums_list):
    return False

  return True

print(check_duplicated([1,2,3]))
'''

"""
Exercise 2 — First repeated value

You receive a list of integers. Process it from left to right and return the
first value that appears for a second time.

Return None if every value appears only once.

Rules:
- Return the repeated value, not its index.
- An empty list returns None.
- Use a set. Do not use list.count() or two nested loops.

Examples:
- Input: [2, 5, 1, 2, 3, 5, 1]
  Output: 2
- Input: [4, 5, 6]
  Output: None
- Input: [7, 7]
  Output: 7
- Input: []
  Output: None
"""

# Write a new function below, including its name and parameters.
import os
os.system('clear')
'''
def check_duplicated(nums_list:list) -> int | None:
  nums_set = set()
  for num in nums_list:
    if num in nums_set:
      return num
    nums_set.add(num)

  return None

print(check_duplicated([]))
'''

"""
Exercise 3 — Keep unique values in order

You receive a list of integers. Return a new list that keeps only the first
appearance of each value, preserving the original order.

Rules:
- Do not change the input list.
- Use a set to remember what you have seen and a new list for the result.
- An empty list returns an empty list.

Examples:
- Input: [3, 1, 3, 2, 1]
  Output: [3, 1, 2]
- Input: [5, 5, 5]
  Output: [5]
- Input: []
  Output: []
- Input: [-1, 0, -1, 0, 2]
  Output: [-1, 0, 2]
"""

# Write a new function below, including its name and parameters.

def check_duplicated(nums_list:list) -> list:
  nums_set = set()
  new_nums_list = []

  for num in nums_list:
    if num not in nums_set:
      new_nums_list.append(num)
    nums_set.add(num)

  return new_nums_list

print(check_duplicated([-1, 0, -1, 0, 2]))