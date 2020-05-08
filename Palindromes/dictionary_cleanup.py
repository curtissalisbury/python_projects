"""remove single letter words from list if not 'a' or 'i'"""
import load_dictionary

word_list = load_dictionary.load('words.txt')
word_list_clean = []

permissible = ('a', 'i')

# remove single letter words if not a or i
for word in word_list:
    if len(word) > 1:
        word_list_clean.append(word)
    elif len(word) == 1 and word in permissible:
        word_list_clean.append(word)
    else:
        continue
print(f'{word_list_clean}')
