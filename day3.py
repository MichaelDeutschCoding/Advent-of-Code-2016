import re

with open('day3_input.txt', 'r') as f:
    raw = f.readlines()

triangles = [[int(sub) for sub in re.findall(r'\d+', line)] for line in raw]

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

counter = 0
for triangle in triangles:
    if is_triangle(triangle[0], triangle[1], triangle[2]):
        counter += 1

print(counter)

def fancy_tri(sides):
    x, y, z = sorted(sides)
    return z < x + y
