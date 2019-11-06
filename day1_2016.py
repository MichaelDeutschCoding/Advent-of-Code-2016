
def move(starting, instructions, visited):
    x, y, heading = starting
    turn, d = instructions[0], int(instructions[1:])
    if turn == 'R':
        heading = (heading + 1) % 4
    elif turn == 'L':
        heading = (heading + 3) % 4
    else:
        print("Heading Error.")
        return
    
    if heading == 0: #going north
        for i in range(1, d+1):
            visited.append((x, y+i))
    elif heading == 1: #going east
        for i in range(1, d+1):
            visited.append((x+i, y))
    elif heading == 2: #going south
        for i in range(1, d+1):
            visited.append((x, y-i))
    else:           #going west
        for i in range(1, d+1):
            visited.append((x-i, y))

    return (visited[-1][0], visited[-1][1], heading)

def follow(l):

    tele = (0, 0, 0)
    visited = [(0, 0)]

    for step in l:
        tele = move(tele, step, visited)

    for i in range(len(visited)):
	    if visited[i] in visited[:i]:
		    print(f"found a double: {visited[i]} which appears at index {visited.index(visited[i])} and index {i}")
		    break
    else:
	    print("no doubles found")
    
    print(f"Total (taxicab) distance of destination {visited[-1]} from origin (0, 0) is: {abs(visited[-1][0]) + abs(visited[-1][1])}")


sample = ['L2', 'R3', 'L5', 'L2', 'R6', 'L3', 'L7', 'L8']
#follow(sample)

sample2 = ['R5', 'L5', 'R5', 'R3']
#follow(sample2)

sample3 = ['R2', 'R2', 'R2']
#follow(sample3)

puzzle_data = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

real_list = [x.strip() for x in puzzle_data.split(',')]
print('real list:')
follow(real_list)
