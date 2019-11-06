puzzle_input = '11011110011011101'

def extend(a):
    b = a[::-1]
    b = ''.join(['0' if x == '1' else '1' for x in b])
    return a + '0' + b

def pad(string, length):
    while len(string) < length:
        string = extend(string)
    return string[:length]

def checksum(string):
    while True:
        if len(string) % 2 == 1:
            return string
        else:
            string = ''.join(['1' if string[i] == string[i+1] else '0' for i in range(0, len(string), 2)])


def fill_disk(initial, length):
    full = pad(initial, length)
    print('checksum:', checksum(full))


fill_disk(puzzle_input, 35651584)