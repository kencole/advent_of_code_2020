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

def apply_mask_to_addr(mask, addr):
    addr = bin(addr)[2:]
    addr = '0' * (len(mask) - len(addr)) + addr
    for i in range(len(mask)):
        c = mask[i]
        if c == '0':
            continue
        elif c == '1':
            addr = replace_at(addr, i, '1')
        elif c == 'X':
            addr = replace_at(addr, i, 'X')
    return addr

def get_all_offsets(offsets, offset_sums, i = 0, curr_sum = 0):
    if i == len(offsets):
        offset_sums.append(curr_sum)
        return offset_sums
    get_all_offsets(offsets, offset_sums, i + 1, curr_sum + offsets[i])
    get_all_offsets(offsets, offset_sums, i + 1, curr_sum)
    return offset_sums

mem = {}
    
def write_val_to_floating_addr(addr, val):
    offsets = [
        2**(len(addr) - i - 1)
        for i in range(len(addr))
        if addr[i] == 'X'
    ]
    base = "".join([c if not c == 'X' else '0' for c in addr])
    base = int(base, base = 2)
    for offset in get_all_offsets(offsets, []):
        mem[base + offset] = val

mask = None

for line in lines:
    addr, val = parse_line(line)
    if addr == 'mask':
        mask = val
    else:
        write_val_to_floating_addr(apply_mask_to_addr(mask, addr), val)
    
totals = 0
for (key, val) in mem.items():
    totals += val

print(totals)
