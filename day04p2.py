def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

def validate_number(n, low, high, base = 10):
    try:
        n = int(n, base)
        return low <= n <= high
    except ValueError:
        return False

def validate_byr(val):
    if not len(val) == 4:
        return False
    return validate_number(val, 1920, 2002)
    
def validate_iyr(val):
    if not len(val) == 4:
        return False
    return validate_number(val, 2010, 2020)

def validate_eyr(val):
    if not len(val) == 4:
        return False
    return validate_number(val, 2020, 2030)

def validate_hgt(val):
    if not len(val) >= 2:
        return False
    in_or_cm = val[-2:]
    val = val[:-2]
    if in_or_cm == 'in':
        return validate_number(val, 59, 76)
    elif in_or_cm == 'cm':
        return validate_number(val, 150, 193)

def validate_hcl(val):
    if not (len(val) == 7 and val[0] == '#'):
        return False
    return validate_number(
        val[1:],
        int('000000', 16),
        int('ffffff', 16),
        base = 16
    )

def validate_ecl(val):
    return val in set([
        'amb', 'blu', 'brn', 'gry',
        'grn', 'hzl', 'oth'
    ])

def validate_pid(val):
    return len(val) == 9 and \
        validate_number(val,
                        000000000,
                        999999999)


validation_funcs = {
    'byr' : validate_byr,
    'iyr' : validate_iyr,
    'eyr' : validate_eyr,
    'hgt' : validate_hgt,
    'hcl' : validate_hcl,
    'ecl' : validate_ecl,
    'pid' : validate_pid
}

filename = 'day04p1.txt'

lines = read_input(filename)

passports = [[]]
for line in lines:
    tokens = line.split()
    if len(tokens) > 0:
        passports[-1].extend(tokens)
    else:
        passports.append([])
        
required_valid_fields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
])

def get_key_val(key_val_pair):
    return key_val_pair.split(':')

valid = 0
for passport in passports:
    present_fields = set()
    for kv_pair in passport:
        k, v = get_key_val(kv_pair)
        if k in validation_funcs:
            if validation_funcs[k](v):
                present_fields.add(k)
        else:
            present_fields.add(k)
    if required_valid_fields.issubset(present_fields):
        valid += 1
print(valid)
