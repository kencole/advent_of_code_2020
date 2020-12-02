def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day02p1.txt'

def parse_line(line):
    allowable_range, char, password = line.split()
    allowable_range = tuple(int(n) for n in allowable_range.split('-'))
    char = char.replace(':', '')
    return allowable_range, char, password

def count_occurences(string, char):
    occurences = 0
    for c in string:
        if c == char:
            occurences += 1
    return occurences

lines = read_input(filename)
line_data = [parse_line(line) for line in lines]

valid = 0

for allowable_range, char, password in line_data:
    occurences = count_occurences(password, char)
    if occurences >= allowable_range[0] and \
       occurences <= allowable_range[1]:
        valid += 1

print(valid)


