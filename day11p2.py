def read_input(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [line.rstrip() for line in content]
    return content

filename = 'day11p1.txt'

lines = read_input(filename)
board = [[c for c in line] for line in lines]

def at(r, c, board):
    if r < 0 or r >= len(board) or \
       c < 0 or c >= len(board[r]):
        return ".", False
    return board[r][c], True

adjacents = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
]

def find_in_direction(direction, r, c, board):
    for i in range(1, max(len(board), len(board[0]))):
        char, in_board = at(
            direction[0] * i + r,
            direction[1] * i + c,
            board)
        if char != '.' or not in_board:
            return char

def set_new(r, c, board, new_board):
    current = board[r][c]
    if not current == '.':
        surrounding = [
            find_in_direction(offset, r, c, board)
            for offset in adjacents
        ]
        if current == 'L':
            if surrounding.count('#') == 0:
                new_board[r][c] = '#'
                return True
        elif current == '#':
            if surrounding.count('#') >= 5:
                new_board[r][c] = 'L'
                return True
    return False

scratch_board = [[c for c in line] for line in board]


has_changed = True
while has_changed:
    has_changed = False
    new_board = scratch_board
    for r in range(len(board)):
        for c in range(len(board[0])):
            new_board[r][c] = board[r][c]
    for r in range(len(board)):
        for c in range(len(board[0])):
            has_changed |= set_new(r, c, board, new_board)
    board, scratch_board = new_board, board
    

print(sum([line.count('#') for line in board]))
