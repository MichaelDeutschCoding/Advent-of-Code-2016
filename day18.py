puzzle_input = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'

def next_row(prev):
    new = []
    prev = '-' + prev + '-'
    for i in range(1,len(prev) - 1):
        if prev[i-1] == '^' and prev[i] == '^' and prev[i+1] != '^':
            new.append('^')
        elif prev[i+1] == '^' and prev[i] == '^' and prev[i-1] != '^':
            new.append('^')
        elif prev[i-1] == '^' and prev[i] != '^' and prev[i+1] != '^':
            new.append('^')
        elif prev[i-1] != '^' and prev[i] != '^' and prev[i+1] == '^':
            new.append('^')
        else:
            new.append('.')
    return ''.join(new)

test = '..^^.'

def room(tiles, length):
    safe = 0
    for row in range(length):
        safe += tiles.count('.')
        tiles = next_row(tiles)
    print(safe)

room(puzzle_input, 400000)