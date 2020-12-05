def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

def make_replacement_func(replacements):
    def func(s):
        for replace, replace_with in replacements.items():
            s = s.replace(replace, replace_with)
        return s
    return func

front_back_to_binary = make_replacement_func({'F' : '0', 'B' : '1'})
left_right_to_binary = make_replacement_func({'L' : '0', 'R' : '1'})

filename = 'day05p1.txt'

lines = read_input(filename)

seats = [
    (front_back_to_binary(line[:-3]),
     left_right_to_binary(line[-3:]))
    for line in lines
]

seats = [
    (int(fb, base=2), int(lr, base=2))
    for (fb, lr) in seats
]

seat_ids = [8 * row + col for (row, col) in seats]

print(max(seat_ids))
