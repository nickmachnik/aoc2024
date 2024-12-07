#!/usr/bin/env python

import sys
from copy import deepcopy

class Position():
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def tup(self):
        return (self.row, self.col)

    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)

    def __str__(self):
        return f"Position({self.row},{self.col})"

class Guard():
    def __init__(self, row, col, direction):
        self.position = Position(row, col)
        self.direction = self.sym2dir(direction)
        self.visited = set()
        self.visited.add(self.position.tup())

    def turn_right(self):
        self.direction = Position(self.direction.col, -1 * self.direction.row)

    def dir2sym(self):
        if self.direction.tup() == (-1, 0):
            return '^'
        elif self.direction.tup() == (0, 1):
            return '>'
        elif self.direction.tup() == (1, 0):
            return 'v'
        elif self.direction.tup() == (0, -1):
            return '<'
            
    def sym2dir(self, symbol):
        if symbol == '^':
            return Position(-1, 0)
        elif symbol == '>':
            return Position(0, 1)
        elif symbol == 'v':
            return Position(1, 0)
        elif symbol == '<':
            return Position(0, -1)
        else:
            exit("Unexpected dir symbol!")

    def next_position(self):
        return self.position + self.direction

    def move(self):
        self.position = self.next_position()
        self.visited.add(self.position.tup())


class Lab():
    def __init__(self, infile):
        self._parse(infile)
        self.nrows = len(self.grid)
        self.ncols = len(self.grid[0])

    def print_self(self):
        grid = deepcopy(self.grid)
        guard_symbol = self.guard.dir2sym()
        grid[self.guard.position.row][self.guard.position.col] = guard_symbol
        for row in grid:
            print(''.join(row))
        print()

    def move_guard(self):
        while self.is_in_bounds(self.guard.next_position()):
            if self.is_obstacle(self.guard.next_position()):
                self.guard.turn_right()
            else:
                self.guard.move()
            # self.print_self()

    def is_in_bounds(self, p):
        return p.row >= 0 and p.col >= 0 and p.row < self.nrows and p.col < self.ncols

    def is_obstacle(self, p):
        return self.at(p) == '#'

    def at(self, p):
        return self.grid[p.row][p.col]

    def _parse(self, infile):
        self.grid = []
        with open(infile, 'r') as fin:
            for row_ix, line in enumerate(fin):
                self.grid.append([])
                for col_ix, symbol in enumerate(line.strip()):
                    if symbol == '#':
                        self.grid[-1].append(symbol)
                    elif symbol == '.':
                        self.grid[-1].append(symbol)
                    else:
                        self.guard = Guard(row_ix, col_ix, symbol)
                        self.grid[-1].append('.')

def main():
    infile = sys.argv[1]
    lab = Lab(infile)
    lab.move_guard()
    print(len(lab.guard.visited))
    
if __name__ == "__main__":
    main()