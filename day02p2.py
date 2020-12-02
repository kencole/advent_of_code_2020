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

lines = read_input(filename)
line_data = [parse_line(line) for line in lines]

valid = 0

for idxs, char, password in line_data:
    char_in_first_idx = False
    char_in_second_idx = False
    first_idx = idxs[0] - 1
    second_idx = idxs[1] - 1
    if first_idx < len(password):
        char_in_first_idx = (password[first_idx] == char)
    if second_idx < len(password):
        char_in_second_idx = (password[second_idx] == char)
    if (char_in_first_idx or char_in_second_idx) \
       and not (char_in_first_idx and char_in_second_idx):
        valid += 1
    
        
print(valid)


