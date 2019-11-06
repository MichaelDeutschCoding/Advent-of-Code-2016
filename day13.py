fave = 1350
fave=10

goal = (31, 39)
goal = (7, 4)

def solve_space(location):
    x, y = location
    num = (x*x) + 3*x + 2*x*y + y + y*y + fave
    ones = bin(num).count('1')
    if ones % 2 == 0:
        return True
    return False

def neighbors(location):
    x, y = location
    highx, highy = goal

    if x > highx + 2 or y > highy +2:
        return []

    if x >= 1 and y >=1:
        return [  (x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    elif x==0 and y >=1:
        return [(x, y-1),(x+1, y), (x, y+1)]
    elif y==0 and x >=1:
        return [(x-1, y),(x, y+1), (x+1, y)]
    elif y==0 and x==0:
        return [(1, 0), (0, 1)]
    else:
        assert 1==2

# shortest = 200

valid_paths = []

def find_path(current, visited= []):
    # global shortest

    if current == goal:  #and len(visited) < shortest:
        #shortest = len(visited)
        print("I reached", current)
        #print(visited)
        print(len(visited))
        valid_paths.append(visited)
        return True
    visited.append(current)
    stack = []
    
    for location in neighbors(current):
        if location not in visited and solve_space(location):
            stack.append((location, visited))
    
    while stack:
        current, visited = stack.pop()
        visited = list(visited)
        find_path(current, visited)
            # return True
    
    # return False

find_path((1,1))

for path in valid_paths:
    print(len(path), path)

#104 was too high
#102 was too high