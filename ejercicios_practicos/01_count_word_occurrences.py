"""
Exercise 1 — Count word occurrences

Create a function that receives a list of words and returns a dictionary
showing how many times each word appears.

Rules:
- Do not distinguish uppercase from lowercase: "Hello" and "hello" count as
  the same word.
- If the list is empty, return an empty dictionary.
- Use a for loop, conditionals, and a dictionary. You do not need set or
  dict.get().

Examples:
- Input: ["Hello", "world", "hello", "HELLO"]
  Output: {"hello": 3, "world": 1}
- Input: []
  Output: {}
- Input: ["Python"]
  Output: {"python": 1}
"""

# Write the function yourself below, including its name and parameters.
# Before calling it done, add and run your own print() statements.
# Test at least: an empty list, one word, and repeated words with different cases.
'''
import os
os.system("clear")

def word_counter(words_list:list) -> dict:
    word_dict = {}
    for word in words_list:
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
    return word_dict

list_of_words = ["Red", "blue", "green", "red", "yellow", "Blue", "black", "green", "RED", "violet", "blue", "gray", "Green", "yellow", "white"]
for key, value in word_counter(list_of_words).items():
    print(f'{key} : {value}')
'''

"""
Practice 2 — Count support statuses

You receive a list of support-ticket statuses. Return a dictionary with the
number of times each status appears.

Rules:
- Statuses must be counted case-insensitively: "Open" and "open" are the same.
- Keep each status in lowercase in the returned dictionary.
- If the list is empty, return an empty dictionary.
- Use a for loop, conditionals, and a dictionary. Do not use dict.get().

Examples:
- Input: ["Open", "closed", "OPEN", "Pending", "closed", "open"]
  Output: {"open": 3, "closed": 2, "pending": 1}
- Input: []
  Output: {}
- Input: ["Resolved"]
  Output: {"resolved": 1}
"""

# Write a new function below, including its name and parameters.
'''
def count_status_list(status_list:list) -> dict:
    status_dict ={}

    for status in status_list:
        if status.lower() in status_dict:
            status_dict[status.lower()] += 1
        else:
            status_dict[status.lower()] = 1

    return status_dict

status_list = ["Open", "closed", "OPEN", "Pending", "closed", "open"]
for key, value in count_status_list(status_list).items():
    print(f'{key}: {value}')
'''

"""
Practice 3 — Count vote choices

You receive a list of vote choices. Every choice is one of: "yes", "no", or
"abstain". Return a dictionary with the number of votes for each choice that
appears in the input.

Rules:
- Choices must be counted case-insensitively.
- Keep each choice in lowercase in the returned dictionary.
- Do not add choices that do not appear in the input.
- An empty list returns an empty dictionary.
- Use a for loop, conditionals, and a dictionary. Do not use dict.get().

Examples:
- Input: ["Yes", "no", "YES", "abstain", "No", "yes"]
  Output: {"yes": 3, "no": 2, "abstain": 1}
- Input: ["ABSTAIN", "abstain"]
  Output: {"abstain": 2}
- Input: []
  Output: {}
"""

def count_votes(votes_list:list) -> dict:
    votes_dict = {}
    for vote in votes_list:
        if vote.lower() in votes_dict:
            votes_dict[vote.lower()] +=1
        else:
            votes_dict[vote.lower()] = 1
    return votes_dict

votes_list = ["Yes", "no", "YES", "abstain", "No", "yes"]
for key, value in count_votes(votes_list).items():
    print(f'{key}: {value}')

# Write a new function below, including its name and parameters.
