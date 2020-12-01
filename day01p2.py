def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day01p1.txt'

nums = [int(line) for line in read_input(filename)]
seen = set()

nums.sort()

for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
        curr_sum = nums[i] + nums[j] + nums[k]
        if curr_sum == 2020:
            print(nums[i], nums[j], nums[k],
                  nums[i] * nums[j] * nums[k])
            break
        elif curr_sum < 2020:
            j += 1
        else:
            k -= 1
