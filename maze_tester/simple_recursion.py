maze = {
    'A' : ['B'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B', 'E'],
    'D' : ['B', 'F', 'G'],
    'E' : ['C'],
    'F' : ['D'],
    'G' : ['D', 'I'],
    'I' : ['G']
}

goal = 'G'

def find_path(current, visited):

    if current == goal:
        print("I found it! I'm at", goal)
        print(visited)
        print(len(visited))
        return True
    visited.append(current)
    stack = []

    for location in maze[current]:
        if location not in visited:
            stack.append((location, visited))

    while stack:
        current, visited = stack.pop()
        if find_path(current, visited):
            return True
    
    return False

find_path('A', [])