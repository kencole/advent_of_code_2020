def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day08p1.txt'

lines = read_input(filename)

def parse_line(line):
    instruction, value = line.split()
    return (instruction, int(value))

lines = [parse_line(line) for line in lines]

def get_indices_on_match(lines, func):
    idx_line = enumerate(lines)
    idxs = [idx for (idx, line) in idx_line if func(line)]
    return idxs

jmp_idxs = get_indices_on_match(lines, lambda x : x[0] == 'jmp')
nop_idxs = get_indices_on_match(lines, lambda x : x[0] == 'nop')

for corrupt_point in jmp_idxs + nop_idxs:
    acc = 0
    instruction_pointer = 0
    visited_instructions = set()

    # try correction
    corrupt_instr, value = lines[corrupt_point]
    if corrupt_instr == 'nop':
        lines[corrupt_point] = ('jmp', value)
    else:
        lines[corrupt_point] = ('nop', value)
    
    while True:
        if instruction_pointer >= len(lines):
            print(acc, corrupt_point)
            break
        if instruction_pointer in visited_instructions:
            break
        visited_instructions.add(instruction_pointer)
        instruction, value = lines[instruction_pointer]
        if instruction == 'acc':
            acc += value
            instruction_pointer += 1
        elif instruction == 'jmp':
            instruction_pointer += value
        else:
            instruction_pointer += 1

    # reset instructions to before correction
    corrupt_instr, value = lines[corrupt_point]
    if corrupt_instr == 'nop':
        lines[corrupt_point] = ('jmp', value)
    else:
        lines[corrupt_point] = ('nop', value)
    
