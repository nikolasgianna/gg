def neighbors(cell):
    x, y = cell
    block = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]
    # We only want the surrounding cells
    del block[4]
    return block

def getAliveCells(world):

    cells = set([])

    for x,row in enumerate(world):
        for y,cell in enumerate(row):
            if cell:
                 cells.add((x,y))
    return cells

def toArray(world, height, width, offset_x, offset_y):

    new_world = [(z+offset_x, y+offset_y) for (z,y) in world]

    board = [[0] * width for row in range(height)]

    for cell in new_world:
        board[cell[0]][cell[1]] = 1

    return board

def arrayToTiles(array):
    s = []
    for x,row in enumerate(array):
        for y,cell in enumerate(row):
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)

def tick(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

def outputDisplay(board):
    der = list(board)
    new_height = max( x for (x,y) in der) - min( x for (x,y) in der)
    new_width =  max( y for (x,y) in der) - min( y for (x,y) in der)
    offset_x = 0 - min( x for (x,y) in der)
    offset_y = 0 - min( y for (x,y) in der)
    # print (new_height, new_width)
    out = toArray(der, new_height+1, new_width+1, offset_x,offset_y)
    return arrayToTiles(out)

def run(board):
    number_of_iterations = 5

    # for __ in range(number_of_iterations):
    # while True:
        # input("Press Enter to continue...")
    board = tick(board)
    # print(board)
    return board


def main():

    fo = open("./input.txt")
    print(fo.read())
    start = [[1,1,1],
            [0,1,0],
            [0,1,0]]

    print(arrayToTiles(start))

    board = getAliveCells(start)
    # for __ in range(5):
    while True:
        input("Press Enter to run one step...")
        board = tick(board)
        print (outputDisplay(board))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nGame Stopped')
