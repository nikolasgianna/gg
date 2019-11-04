#!/usr/bin/env python3

import sys

MAX_ARRAY = 100
MAX_ITERATIONS = 1000

def toArray(board):

    aliveCells = list(board)

    try:
        new_height = max( x for (x,y) in aliveCells) - min( x for (x,y) in aliveCells)
        new_width =  max( y for (x,y) in aliveCells) - min( y for (x,y) in aliveCells)
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

def positive_int(x):
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError("Minimum number of iterations is 1")
    if x > MAX_ITERATIONS:
        raise argparse.ArgumentTypeError("{} {}".format("Maximum number of iterations is", MAX_ITERATIONS))
    return x
