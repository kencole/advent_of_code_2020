def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day14p1.txt'

lines = read_input(filename)

def parse_line(line):
    addr, val = line.split(' = ')
    if addr[:3] == 'mem':
        addr = int(addr.split('[')[1].split(']')[0])
        val = int(val)
    return (addr, val)

def replace_at(s, i, c):
    return s[:i] + c + s[i + 1:]

def apply_mask(mask, val):
    val = bin(val)[2:]
    val = '0' * (len(mask) - len(val)) + val
    for i in range(len(mask)):
        c = mask[i]
        if c == '0':
            val = replace_at(val, i, '0')
        elif c == '1':
            val = replace_at(val, i, '1')
    return int(val, base = 2)

mem = {}
mask = None

for line in lines:
    addr, val = parse_line(line)
    if addr == 'mask':
        mask = val
    else:
        mem[addr] = apply_mask(mask, val)
    
totals = 0
for (key, val) in mem.items():
    totals += val

print(totals)
