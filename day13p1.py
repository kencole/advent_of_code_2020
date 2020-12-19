def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day13p1.txt'

time, buses = read_input(filename)
time = int(time)
buses = [int(bus) for bus in buses.split(',') if not bus == 'x']

starts = [(time // bus) * bus + bus for bus in buses]
starts_buses = zip(starts, buses)
soonest = min(starts_buses, key=lambda p: p[0])
print((soonest[0] - time) * soonest[1])
