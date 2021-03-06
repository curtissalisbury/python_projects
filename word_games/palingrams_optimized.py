"""Find all word pair palingrams in a dictionary file
    Checking with time to see duration of program run"""
import time
import load_dictionary

word_list = load_dictionary.load('words.txt')


# Find word-pair palingrams

def find_palingrams():
    """find dictionary palingrams"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = ''.join(reversed(word))
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[
                                                      end - i:] in words:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end - i:] and rev_word[
                                                      :end - i] in words:
                    pali_list.append((rev_word[:end - i], word))
    return pali_list


start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
print(f'Runtime for this program was {end_time - start_time} seconds')
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print(f'\nNumber of palingrams = {len(palingrams_sorted)}')
for first, second in palingrams_sorted:
    print(f'{first} {second}')
