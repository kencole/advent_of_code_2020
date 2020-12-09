from collections import deque

def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day09p1.txt'

lines = read_input(filename)
nums = [int(line) for line in lines]

current_window = deque(nums[:25])

def can_sum_to(queue, k):
    seen = set()
    for num in queue:
        if k - num in seen:
            return True
        else:
            seen.add(num)
    return False

for num in nums[25:]:
    if can_sum_to(current_window, num):
        current_window.popleft()
        current_window.append(num)
    else:
        print(num)
        break
