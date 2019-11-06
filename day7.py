import re

pattern = r"\[.+?\]"

tot = 0
new = 0

with open("day7_input.txt") as f:
    data = f.readlines()

def check(string):
    for i in range(len(string) - 3):
        if string[i] == string[i+3] and \
        string[i+1] == string[i+2] and \
        string[i] != string[i+1]:
            #print(string[i:i+4])
            return True
    return False

def liner(line):
    bracks = re.findall(pattern, line)
    for b in bracks:
        if check(b):
            return False
    return check(line)


def part2(line):
    poss = []
    groups = re.split(r"\[|\]", line)
    for stuff in groups[::2]:
        for i in range(len(stuff) - 2):
            if stuff[i] == stuff[i+2] and stuff[i] != stuff[i+1]:
                poss.append(stuff[i:i+3])
    for i in range(len(poss)):
        poss[i] = str(poss[i][1] + poss[i][0] + poss[i][1])
    for stuff in groups[1::2]:
        for letters in poss:
            if letters in stuff:
                return True
    return False


for entry in data:
    if liner(entry):
        tot +=1
print("Part 1:", tot)


for entry in data:
    if part2(entry):
        new +=1
print("part 2:", new)





"""

test5 = "aba[bab]xyz"
test6 = "xyx[xyx]xyx"
test7 = "aaa[kek]eke"
test8 = "zazbz[bzb]cdb"
print("test5:", part2(test5))
print("test6:", part2(test6))
print("test7:", part2(test7))
print("test8:", part2(test8))



test1 = "abba[mnop]qrst"
test2 = "abcd[bddb]xyyx"
test3 = "aaaa[qwer]tyui"
test4 = "ioxxoj[asdfgh]zxcvbn"
print("test 1:", liner(test1))
print("test 2:", liner(test2))
print("test 3:", liner(test3))
print("test 4:", liner(test4))
"""