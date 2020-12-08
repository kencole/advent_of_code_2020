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

acc = 0
instruction_pointer = 0
visited_instructions = set()
    
while True:
    if instruction_pointer in visited_instructions:
        print(acc)
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

    
