import re

with open('day20_input.txt') as f:
    raw =  re.findall(r'(\d+)-(\d+)', f.read())

print(raw[:4])


blocked_ranges = sorted([(int(d), int(e)) for d, e in raw])
print(len(blocked_ranges))
print(blocked_ranges[:5])

def open(ranges):
    i = 0
    for (low, high) in ranges:
        yield from range(i, low)
        i = max(i, high+1)

available = list(open(blocked_ranges))

print(available[0])
print(len(available))