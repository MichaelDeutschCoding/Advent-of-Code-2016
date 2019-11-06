import re

p = re.compile(r'\((\d+)x(\d+)\)')

with open('day9_input.txt') as f:
    text = f.read()

def adjust_len(match):
    return int(match.group(1)) * (int(match.group(2)) - 1) - len(match.group(0))

def decompress(text):
    matchlist = [p.search(text)]

    while True:
        m = p.search(text, matchlist[-1].end() + int(matchlist[-1].group(1)))
        if m:
            matchlist.append(m)
        else:
            break

    print(len(matchlist))
    total = len(text)
    for match in matchlist:
        if p.search(text, match.end(), match.end() + int(match.group(2))):

            total += decompress(text[match.end():match.end() + int(match.group(2))])
        
        total += adjust_len(match)
    return total

#print(decompress(text))

def ultra(text):
    tot = 0
    i = 0
    while i < len(text):
        m = p.match(text, i)
        if not m:
            i += 1
            tot += 1
            continue
        else:
            C, R = map(int, m.groups())
            i = m.end()
            tot += R * ultra(text[i: i+C])
            i += C

    return tot

assert ultra('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

print (ultra(text))