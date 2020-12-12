def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day10p1.txt'

lines = read_input(filename)
nums = [int(line) for line in lines]
nums.extend([0, max(nums) + 3])
nums.sort()

one_diffs = 0
three_diffs = 0

for (a, b) in zip(nums[:-1], nums[1:]):
    if b - a == 1:
        one_diffs += 1
    elif b - a == 3:
        three_diffs += 1

print(one_diffs * three_diffs)
