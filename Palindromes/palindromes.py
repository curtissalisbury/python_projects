"""Find Palindromes"""

import load_dictionary

word_list = load_dictionary.load('words.txt')
palindrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindrome_list.append(word)

print(f'\nNumber of palindromes found = {len(palindrome_list)} \n')
print(*palindrome_list, sep='\n')
