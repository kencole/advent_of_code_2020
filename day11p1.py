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
        return "."
    return board[r][c]

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

def set_new(r, c, board, new_board):
    current = board[r][c]
    if not current == '.':
        surrounding = [
            at(r + offset[0], c + offset[1], board)
            for offset in adjacents
        ]
        if current == 'L':
            if surrounding.count('#') == 0:
                new_board[r][c] = '#'
                return True
        elif current == '#':
            if surrounding.count('#') >= 4:
                new_board[r][c] = 'L'
                return True
    return False
        

has_changed = True
while has_changed:
    has_changed = False
    new_board = [[c for c in line] for line in board]
    for r in range(len(board)):
        for c in range(len(board[0])):
            has_changed |= set_new(r, c, board, new_board)
    board = new_board
    

print(sum([line.count('#') for line in board]))
