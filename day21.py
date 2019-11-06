from itertools import permutations

with open('day21_input.txt') as f:
    steps = f.read().split('\n')

def password(pword, steps):
    pword = list(pword)

    for step in steps:
        if step.startswith('rotate'):
            pword = rota(pword, step)
        elif step.startswith('swap'):
            pword = swap(pword, step)
        elif step.startswith('reverse'):
            pword = reverse(pword, step)
        elif step.startswith('move'):
            pword = move(pword, step)

    return ''.join(pword)

def rota(pword, step):
    if step[7] == 'b':
        n = pword.index(step[-1])
        if n >= 4:
            n += 2
        else:
            n += 1
        n = -(n % len(pword))
    elif step[7] == 'r':
        n = -(int(step[13]))
    elif step[7] == 'l':
        n = int(step[12])
    else:
        raise IndexError
    return pword[n:] + pword[:n]

def swap(pword, step):
    if step[5] == 'p':
        A, B = int(step[14]), int(step[-1])
        pword[A], pword[B] = pword[B], pword[A]
    else:       #swap letter
        A, B = pword.index(step[12]), pword.index(step[-1])
        pword[A], pword[B] = step[-1], step[12]
    return pword

def reverse(pword, step):
    X, Y = int(step[18]), int(step[-1])+1
    sub = pword[X: Y]
    sub = sub[::-1]
    pword[X:Y] = sub
    return pword

def move(pword, step):
    X, Y = int(step[14]), int(step[-1])
    pword.insert(Y, pword.pop(X))
    return pword


test = ['swap position 4 with position 0', 'swap letter d with letter b', 'reverse positions 0 through 4', 'rotate left 1 step', 'move position 1 to position 4', 'move position 3 to position 0', 'rotate based on position of letter b', 'rotate based on position of letter d']

#print(password('abcde', test))
#print(password('abcdefgh', steps))

print({''.join(p) for p in permutations('abcdefgh') if password(p, steps) == 'fbgdceah'}) 

