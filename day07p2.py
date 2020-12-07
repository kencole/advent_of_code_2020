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

for (parent, children) in lines:
    for (count, child) in children:
        contains[parent][child] = count

# calculates how many bags are in bag, including bag itself        
has_to_contain = {}
def count_has_to_contain(bag):
    if bag in has_to_contain:
        return has_to_contain[bag]
    bag_contains = 0
    for (child, count) in contains[bag].items():
        bag_contains += count * count_has_to_contain(child)
    has_to_contain[bag] = 1 + bag_contains
    return has_to_contain[bag]
        

print(count_has_to_contain('shiny gold') - 1)
