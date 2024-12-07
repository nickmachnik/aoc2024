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

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


class Guard():
    def __init__(self, row, col, direction):
        self.position = Position(row, col)
        self.direction = self.sym2dir(direction)

    def load_state_backup(self):
        self.position = Position(*self.state_backup[0])
        self.direction = Position(*self.state_backup[1])

    def backup_state(self):
        self.state_backup = deepcopy(self.state())

    def state(self):
        return (self.position.tup(), self.direction.tup())

    def turn_right(self):
        self.direction = Position(self.direction.col, -1 * self.direction.row)

    def dir2sym(self, dir_tup):
        if dir_tup == (-1, 0):
            return '^'
        elif dir_tup == (0, 1):
            return '>'
        elif dir_tup == (1, 0):
            return 'v'
        elif dir_tup == (0, -1):
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

    def forward(self):
        self.position = self.next_position()


class Lab():
    def __init__(self, infile):
        self._parse(infile)
        self.nrows = len(self.grid)
        self.ncols = len(self.grid[0])
        self.guard_starting_pos = self.guard.position
        self.possible_blocks = set()

    def print_self(self, trace, block_position):
        grid = deepcopy(self.grid)
        for state in trace:
            p = state[0]
            guard_symbol = self.guard.dir2sym(state[1])
            grid[p[0]][p[1]] = guard_symbol
        grid[block_position.row][block_position.col] = 'O'
        for row in grid:
            print(''.join(row))
        print()

    def is_guard_starting_pos(self, pos):
        return self.guard_starting_pos == pos

    def is_loop_at_pos(self):
        blocked_pos = self.guard.next_position()
        self.add_block_at(blocked_pos)
        self.guard.backup_state()
        is_loop = False
        visited = set()
        while self.is_in_bounds(self.guard.next_position()):
            visited.add(self.guard.state())
            if self.is_obstacle(self.guard.next_position()):
                self.guard.turn_right()
            else:
                self.guard.forward()
            if self.guard.state() in visited:
                is_loop = True
                # self.print_self(visited, blocked_pos)
                break
        
        self.guard.load_state_backup()
        self.rm_block_at(blocked_pos)
        return is_loop
    
    def count_possible_blocks(self):
        while self.is_in_bounds(self.guard.next_position()):
            next_pos = self.guard.next_position()
            if self.is_obstacle(next_pos):
                self.guard.turn_right()
            elif not self.is_guard_starting_pos(next_pos) and next_pos.tup() not in self.possible_blocks and self.is_loop_at_pos():
                self.possible_blocks.add(next_pos.tup())
            else:
                self.guard.forward()
        return len(self.possible_blocks)

    def is_in_bounds(self, p):
        return p.row >= 0 and p.col >= 0 and p.row < self.nrows and p.col < self.ncols

    def is_obstacle(self, p):
        return self.at(p) == '#'

    def add_block_at(self, p):
        self.grid[p.row][p.col] = '#'

    def rm_block_at(self, p):
        self.grid[p.row][p.col] = '.'

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
    print(lab.count_possible_blocks())
    
if __name__ == "__main__":
    main()