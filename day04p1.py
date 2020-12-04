def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day04p1.txt'

lines = read_input(filename)

passports = [[]]
for line in lines:
    tokens = line.split()
    if len(tokens) > 0:
        passports[-1].extend(tokens)
    else:
        passports.append([])

required_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
])

def get_key(key_val_pair):
    return key_val_pair.split(':')[0]

valid = 0
for passport in passports:
    present_fields = set()
    for kv_pair in passport:
        present_fields.add(get_key(kv_pair))
    if required_fields.issubset(present_fields):
        valid += 1
print(valid)
