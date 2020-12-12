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
nums = set(nums)

ways_to_get_to_memo = {0 : 1}
def ways_to_get_to(n):
    if n not in ways_to_get_to_memo:
        if n not in nums:
            ways_to_get_to_memo[n] = 0
        else:
            ways_to_get_to_memo[n] = \
                ways_to_get_to(n - 1) + \
                ways_to_get_to(n - 2) + \
                ways_to_get_to(n - 3)
    return ways_to_get_to_memo[n]


print(ways_to_get_to(max(nums)))
