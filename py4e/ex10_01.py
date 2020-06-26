fname = input('Enter File Name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print(f'file "{fname}" cannot be found in working directory')
    quit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # if the key is not in the dictionary the value is 0 when it sees the
        # word again add 1 to the value
        counts[word] = counts.get(word, 0) + 1
# print(counts)

# find the most common word
largest = -1
the_word = None
for k, v in counts.items():
    if v > largest:
        largest = v
        the_word = k

# Get the top 5 words from the word list
tmp = list()
for k, v in counts.items():
    new_tuple = (v, k)
    tmp.append(new_tuple)

tmp = sorted(tmp, reverse=True)

for v, k in tmp[:5]:
    print(k, v)
