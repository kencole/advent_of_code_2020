def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day03p1.txt'


lines = read_input(filename)

width = len(lines[0])
trees = 0
x = 0

# 1 90
# 3 244
# 5 97
# 7 92
# 1 48

xchange = 3
ychange = 1

for y in range(0, len(lines), ychange):
    trees += 1 if lines[y][x % width] == '#' else 0
    x += xchange
print(trees)
