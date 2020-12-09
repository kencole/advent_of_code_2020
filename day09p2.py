from collections import deque

def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day09p1.txt'

lines = read_input(filename)
nums = [int(line) for line in lines]


target = 776203571

window_start = 0
window_sum = 0


for (idx, num) in enumerate(nums):
    if window_sum == target:
        print(min(nums[window_start : idx + 1]) + \
              max(nums[window_start : idx + 1]))
        break 
    window_sum += num
    while window_sum > target:
        window_sum -= nums[window_start]
        window_start += 1
    
    
