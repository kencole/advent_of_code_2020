def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day07p1.txt'

lines = read_input(filename)


# returns (parent, [(child_count, child) ... ])
def parse_line(line):
    parent, children = line.split('contain')
    parent = parent.split('bags')[0].strip()
    children = children.split(',')
    for i in range(len(children)):
        child = children[i]
        child = child.split()
        if child[0] == 'no':
            return parent, []
        number_of_this_bag_type = int(child[0])
        bag_type = ' '.join(child[1:-1])
        children[i] = (number_of_this_bag_type, bag_type)
    return parent, children

lines = [parse_line(line) for line in lines]

# parent : {child : count, ...}
contains = {}

for (parent, children) in lines:
    contains[parent] = {}
    for (count, child) in children:
        contains[child] = {}

# child : [parent, ...]
is_in = {}

for (parent, children) in lines:
    is_in[parent] = []
    for (count, child) in children:
        contains[parent][child] = count

for (parent, children) in contains.items():
    for child in children:
        is_in[child].append(parent)

can_contain_shiny_gold = 0
visited = set(['shiny gold'])
to_visit = is_in['shiny gold'][:]
while len(to_visit) > 0:
    bag = to_visit.pop()
    if bag not in visited:
        can_contain_shiny_gold += 1
        to_visit.extend(is_in[bag])
        visited.add(bag)

print(can_contain_shiny_gold)
