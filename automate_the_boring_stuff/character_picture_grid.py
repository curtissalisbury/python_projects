grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'o', 'o', '.', '.', '.'],
    ['o', 'o', 'o', 'o', '.', '.'],
    ['o', 'o', 'o', 'o', 'o', '.'],
    ['.', 'o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o', '.'],
    ['o', 'o', 'o', 'o', '.', '.'],
    ['.', 'o', 'o', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')
    print('')
