instructions = ['cpy 1 a', 'cpy 1 b', 'cpy 26 d', 'jnz c 2', 'jnz 1 5', 'cpy 7 c', 'inc d', 'dec c', 'jnz c -2', 'cpy a c', 'inc a', 'dec b', 'jnz b -2', 'cpy c b', 'dec d', 'jnz d -6', 'cpy 19 c', 'cpy 11 d', 'inc a', 'dec d', 'jnz d -2', 'dec c', 'jnz c -5']

test = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']

from collections import Counter

def follow(instructions):
    c = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(instructions):
        if instructions[i].startswith('inc'):
            c[instructions[i][4]] += 1
            i +=1
            continue
        elif instructions[i].startswith('dec'):
            c[instructions[i][4]] -= 1
            i += 1
            continue
        elif instructions[i].startswith('cpy'):
            try:
                c[instructions[i][-1]] = int(instructions[i][4:6])
                i += 1
                continue
            except ValueError:
                c[instructions[i][-1]] = c[instructions[i][4]]
                i += 1
                continue
        elif instructions[i].startswith('jnz'):
            if not c[instructions[i][4]]:
                i += 1
                continue
            else:
                i += (int(instructions[i][-2:]) - 1)
                continue   

    return c['a']

#print(follow(test))
print(follow(instructions))