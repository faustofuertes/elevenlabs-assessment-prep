"""
Exercise 2 — First unique character

Create a function that receives a string and returns the index of the first
character that appears exactly once in the whole string.

If there is no unique character, return -1.

Rules:
- Compare characters exactly as received: "A" and "a" are different.
- An empty string returns -1.
- Use a dictionary to count characters, then loop through the string again to
  find the first character that matches the condition.

Examples:
- Input: "leetcode"
  Output: 0
- Input: "loveleetcode"
  Output: 2
- Input: "aabb"
  Output: -1
- Input: ""
  Output: -1
- Input: "aA"
  Output: 0
"""

# Write the function yourself below, including its name and parameters.
# Before calling it done, add and run your own print() statements.
# Test at least: empty, all repeated, one character, and uppercase/lowercase.
import os
os.system('clear')
'''
def first_unique_char(string:str) -> int:

  # declaro my_index y el dict vacio
  my_index = -1
  chars_dict = {}

  # recorro todo el string y lo mapeo
  for char in string:
    # si existe ese char en el dict (como key) le sumo uno (al value)
    if char in chars_dict:
      chars_dict[char] += 1
    # si no existe ese char en el dict (como key) lo agrego con uno (en el value)
    else:
      chars_dict[char] = 1

  # recorro todo el string exteyendo index y valor
  for index, char in enumerate(string):
  # si en mi dict existe esa key y tiene un valor de 1 (es un valor unico en el string)
    if chars_dict[char] == 1:
  # me guardo el index y corto ahi 
      my_index = index
      break

  return my_index
print(first_unique_char('loveleetcode'))

### MAS FACIL SIN DICTIONARIES
def first_unique_char(string:str) -> int:
  for index, character in enumerate(string):
    if string.count(character) == 1:
      return index
print(first_unique_char('abbcc'))
'''

"""
Practice 2 — First unique number

You receive a list of integers. Return the index of the first number that
appears exactly once in the whole list.

If every number is repeated, or the list is empty, return -1.

Rules:
- Negative numbers are valid.
- Use a dictionary to count every number, then loop through the list again to
  find the first number whose count is 1.
- Do not use set or dict.get().

Examples:
- Input: [4, 5, 4, 6, 5, 7]
  Output: 3
- Input: [2, 2, 8, 8]
  Output: -1
- Input: []
  Output: -1
- Input: [-1, 3, -1, 4]
  Output: 1
"""
'''
def first_unique_num(int_list:list) -> int:
  index = -1
  int_dict = {}

  # recorremos el string lo mapeamos key = num, value = count
  for int in int_list:
    if int in int_dict:
      int_dict[int] += 1
    else:
      int_dict[int] = 1
  
  # recorremos el string extrayendo index y valor
  for idx, int in enumerate(int_list):
    # evaluamos si ese int_list[int] el valor es 1 (ese int aparece una sola vez)
    if int_list[int] == 1:
      # si lo hace guardamos su index y cortamos el flujo
      index = idx
      break
  
  return index
print(first_unique_num([2,2,3,4,4,6,7]))
'''

# Write a new function below, including its name and parameters.


"""
Practice 3 — First unique word

You receive a list of words. Return the first word that appears exactly once
in the whole list, comparing words case-insensitively.

Return None if every word is repeated or if the list is empty.

Rules:
- "Cat" and "cat" count as the same word.
- Return the first word exactly as it originally appears in the input.
- Use a dictionary to count words, then loop through the list again to find
  the first unique word.
- Do not use set or dict.get().

Examples:
- Input: ["Cat", "dog", "cat", "bird", "DOG"]
  Output: "bird"
- Input: ["One", "one", "TWO", "two"]
  Output: None
- Input: ["Python"]
  Output: "Python"
- Input: []
  Output: None
"""

# Write a new function below, including its name and parameters.
'''
def firs_unique_word(word_list:list) -> str | None:
  unique_word = None
  words_dict = {}

  for word in word_list:
    if word.lower() in words_dict:
      words_dict[word.lower()] += 1
    else:
      words_dict[word.lower()] = 1
    
  for  word in word_list:
    if words_dict[word.lower()] == 1:
      unique_word = word
      break
  
  return unique_word

print(firs_unique_word(["Cat", "dog", "dog", "bird", "bird", "cat"]))
'''