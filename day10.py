import re
from collections import defaultdict

with open('day10_input.txt') as f:
    instructions = f.read()

H = re.findall(r'value (\d+) goes to (.+)', instructions)
has = defaultdict(set)
for tup in H:
    has[tup[1]].add(int(tup[0]))

gives = {}
G = re.findall(r'(.+) gives low to (.+) and high to (.+)', instructions)
for tup in G:
    gives[tup[0]] = (tup[1], tup[2])

def transfer(giver, getter, value):
    has[giver].remove(value)
    has[getter].add(value)

while not has['output 0']:
    for bot in gives:
        if len(has[bot]) > 1:
            transfer(bot, gives[bot][0], min(has[bot]))
            transfer(bot, gives[bot][1], max(has[bot]))
else:
    print('output 2 has:', has['output 2'])
    print('output 0 has:', has['output 0'])
    print('output 1 has:', has['output 1'])
