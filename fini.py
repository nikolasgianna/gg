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

def toArray(board):

    aliveCells = list(board)
    new_height = max( x for (x,y) in aliveCells) - min( x for (x,y) in aliveCells)
    new_width =  max( y for (x,y) in aliveCells) - min( y for (x,y) in aliveCells)
    offset_x = 0 - min( x for (x,y) in aliveCells)
    offset_y = 0 - min( y for (x,y) in aliveCells)

    new_world = [(z+offset_x, y+offset_y) for (z,y) in aliveCells]

    board = [[0] * (new_width + 1) for row in range(new_height+1)]

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

def main():

    fo = open("/Users/nikolasgiannakis/Desktop/input.txt")
    inp = fo.read()
    print (inp)
    start = set([])
    for y, row in enumerate(inp.splitlines()):
        for x, cell in enumerate(row.strip()):
            if cell == '0':
                start.add((y,x))

    # start = [[1,1,1],
    #         [0,1,0],
    #         [0,1,0]]

    out = toArray(start)
    print (arrayToTiles(out))

    print (start)
    board = start

    while True:
        input("Press Enter to run one step...")
        board = tick(board)
        print (arrayToTiles(toArray(board)))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nGame Stopped')
