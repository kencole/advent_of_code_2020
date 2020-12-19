def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a  * b / gcd(a, b)


filename = 'day13p1.txt'

_, buses = read_input(filename)
buses = [int(bus) if not bus == 'x' else None for bus in buses.split(',')]

# offset, bus_number
offset_busnum = [pair for pair in enumerate(buses) if pair[1]]

def is_bus_satisfied(bus, offset, num):
    return (num % bus + offset) % bus == 0

curr_incr = offset_busnum[0][1]
curr_val = curr_incr
buses_satisfied = 0


while True:
    curr_offset, curr_bus = offset_busnum[buses_satisfied + 1]
    if is_bus_satisfied(curr_bus, curr_offset, curr_val):
        curr_incr = lcm(curr_incr, curr_bus)
        buses_satisfied += 1
    else:
        curr_val += curr_incr       
    if buses_satisfied + 1 >= len(offset_busnum):
        break

print(curr_val)
