import re

with open('day22_input.txt') as f:
    data = re.findall(r'-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T', f.read())
"""
disks = {}
for line in data:
    disks[(int(line[0]), int(line[1]))] = (int(line[2]), int(line[3]))
"""
new = [((int(line[0]), int(line[1])), int(line[2]), int(line[3])) for line in data]

print(new[:4])