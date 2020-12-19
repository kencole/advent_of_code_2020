def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day12p1.txt'

lines = read_input(filename)
actions = [(line[0], line[1:]) for line in lines]

position = [0, 0]
direction = [0, 1]

for (action, amt) in actions:
    amt = int(amt)
    if action == 'N':
        position[0] += amt
    elif action == 'S':
        position[0] -= amt
    elif action == 'E':
        position[1] += amt
    elif action == 'W':
        position[1] -= amt
    elif action == 'L':
        for turn in range(0, amt, 90):
            direction = [direction[1], -direction[0]]
    elif action == 'R':
        for turn in range(0, amt, 90):
            direction = [-direction[1], direction[0]]        
    elif action == 'F':
        position[0] += direction[0] * amt
        position[1] += direction[1] * amt

print(abs(position[0]) + abs(position[1]))
        

