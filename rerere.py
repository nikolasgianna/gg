print("hello")

def toBoard(cells):

    board = set([])

    for x,row in enumerate(cells):
        for y,cell in enumerate(row):
            if cell:
                # print (x,y)
                 board.add((x,y))
                #  print (board)
    return board

start = [[0,1,0],
         [0,0,1],
         [1,1,1]]

print (toBoard(start))

board = toBoard(start)

def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x    , y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x    , y + 1
    yield x + 1, y + 1

def apply_iteration(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

# if __name__ == "__main__":
def run(board):
    number_of_iterations = 1
    for _ in range(number_of_iterations):
        board = apply_iteration(board)
    # print(board)
    return board

der = list(run(board))
print (der)

new_height = max( x for (x,y) in der) - min( x for (x,y) in der)
new_width =  max( y for (x,y) in der) - min( y for (x,y) in der)

offset_x = 0 - min( x for (x,y) in der)
offset_y = 0 - min( y for (x,y) in der)
print (new_height, new_width)

def toArray(der, height, width, offset_x, offset_y):

    new_der = [(z+offset_x, y+offset_y) for (z,y) in der]

    board = [[0] * width for row in range(height)]

    for cell in new_der:
        board[cell[0]][cell[1]] = 1

    return board

print (toArray(der, new_height+1, new_width+1, offset_x,offset_y))
new_der = [(z+offset_x, y+offset_y) for (z,y) in der]

print (der)
print (new_der)
