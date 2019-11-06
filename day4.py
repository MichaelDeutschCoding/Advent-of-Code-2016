import re
from collections import Counter
from operator import itemgetter

with open('day4_input.txt') as f:
    data = f.read()

p = re.compile('-')
data = p.sub('', data)

codes = re.findall(r'([a-z-]+)(\d+)\[(\w{5})\]', data)

def is_real(tuple):
    count_dict = Counter(tuple[0])
    s = sorted(count_dict.items())
    ordered = sorted(s, key = itemgetter(1), reverse = True)
    for i in range(len(tuple[2])):
        if tuple[2][i] != ordered[i][0]:
            return False
    else:
        return int(tuple[1])

fakes = [
    ('aaaabbbzyx', '123', 'abxyz'),
    ('abcdefgh', '987', 'abcde'),
    ('notarealroom', '404', 'oarel'),
    ('totallyrealroom', '200', 'decoy')
]

def shift_car(c, n):
    if c.islower():
        return chr(((ord(c) - 97 + n) % 26) + 97)
    elif c.isupper():
        return chr(((ord(c)- 65 + n) % 26) + 65)
    else:
        return c

def cipher(s, n):
    m = ''
    for c in s:
        m += shift_car(c, n)
    return m


new = [tuple for tuple in codes if is_real(tuple)]

for line in new:
    if 'north' in cipher(line[0], int(line[1])):
        print(line[1])