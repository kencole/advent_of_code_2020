def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day12p1.txt'

lines = read_input(filename)
actions = [(line[0], line[1:]) for line in lines]

boat_pos = [0, 0]
waypoint_pos = [1, 10]

for (action, amt) in actions:
    amt = int(amt)
    if action == 'N':
        waypoint_pos[0] += amt
    elif action == 'S':
        waypoint_pos[0] -= amt
    elif action == 'E':
        waypoint_pos[1] += amt
    elif action == 'W':
        waypoint_pos[1] -= amt
    elif action == 'L':
        for turn in range(0, amt, 90):
            waypoint_pos = [waypoint_pos[1], -waypoint_pos[0]]
    elif action == 'R':
        for turn in range(0, amt, 90):
            waypoint_pos = [-waypoint_pos[1], waypoint_pos[0]]        
    elif action == 'F':
        boat_pos[0] += waypoint_pos[0] * amt
        boat_pos[1] += waypoint_pos[1] * amt

print(abs(boat_pos[0]) + abs(boat_pos[1]))
        

