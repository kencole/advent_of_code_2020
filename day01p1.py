def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day01p1.txt'

nums = [int(line) for line in read_input(filename)]
seen = set()

for n in nums:
    if 2020 - n in seen:
        print(n, 2020 - n, n * (2020 - n))
    seen.add(n)

