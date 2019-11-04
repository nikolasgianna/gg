#!/usr/bin/env python3

import sys, argparse

MAX_ARRAY = 100
MAX_ITERATIONS = 1000

def neighbors(cell):
    x, y = cell
    block = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]
    # We only want the surrounding cells
    del block[4]
    return block

def toArray(board):

    aliveCells = list(board)

    try:
        new_height = max( x for (x,y) in aliveCells) - min( x for (x,y) in aliveCells)
        new_width =  max( y for (x,y) in aliveCells) - min( y for (x,y) in aliveCells)
        offset_x = 0 - min( x for (x,y) in aliveCells)
        offset_y = 0 - min( y for (x,y) in aliveCells)
        new_world = [(z+offset_x, y+offset_y) for (z,y) in aliveCells]

        board = [[0] * (new_width + 1) for row in range(new_height+1)]

        for cell in new_world:

            board[cell[0]][cell[1]] = 1
    except ValueError:
        print ("No living cells left!!!")
        sys.exit()
    except UnboundLocalError:
        print ("No living cells left!!!")
        sys.exit()

    if new_height > MAX_ARRAY or new_width > MAX_ARRAY:
            # print ("Maximum array size exceeded")
        print ("{} {} {}".format("Maximum array size of", MAX_ARRAY, "exceeded"))
        sys.exit()

    return board

def arrayToTiles(array):
    s = []
    for x,row in enumerate(array):
        for y,cell in enumerate(row):
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    return ''.join(s)

def tick(board):

    # This is the heart of the whole Game
    # Every time this function runs, another generation is applied

    new_board = set([])

    # candidates is the union of currently living cells and all the neighbouring cells
    # but each one is only considered once using the set() function
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:

        # If the neighboring cells are alive cells they should be in the board list,
        # so we just count how many times that's true and that's the number of living
        # cells in the neighbourhood of each living cell
        count = sum((n in board) for n in neighbors(cell))

        # The next statement incorporates the whole logic of The Game of Life
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

def game(seed, iterations):

    cells = set([])
    for y, row in enumerate(seed.splitlines()):
        for x, cell in enumerate(row.strip()):
            if cell == '0':
                cells.add((y,x))

    if cells:

        print("Initial seed is: \n\n" + arrayToTiles(toArray(cells)))

        if iterations > 0:
            for __ in range(iterations):
                cells = tick(cells)
            return arrayToTiles(toArray(cells))
        else:
            while True:
                input("Press Enter to run one step...\n")
                cells = tick(cells)
                print (arrayToTiles(toArray(cells)))
    else: return ("No living cells in initial seed\n")

def positive_int(x):
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError("Minimum number of iterations is 1")
    if x > MAX_ITERATIONS:
        raise argparse.ArgumentTypeError("{} {}".format("Maximum number of iterations is", MAX_ITERATIONS))

    return x

def main():

    parser = argparse.ArgumentParser(allow_abbrev=False, description='A tutorial of argparse!')
    parser.add_argument("--input",required=False, default='', help="This is the 'i' variable")
    parser.add_argument("--iter", required=False, default=0, type=positive_int, help="This is the 'a' variable")
    args = parser.parse_args()
    input = args.input
    iterations = args.iter

    if input != '':
        try:
            fo = open(input)
            seed = fo.read()
        except FileNotFoundError:
            print('\nNo such file in input directory\n')
            sys.exit()
    else:
        print ("No living cells in initial seed\n")
        sys.exit()

    print (game(seed,iterations))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nGame Stopped')
