#!/usr/bin/env python

import sys

class Position():
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def __add__(self, other):
        return Position(self.row + other.row, self.col + other.col)

    def __str__(self):
        return f"Position({self.row},{self.col})"


LOWER_RIGHT = Position(1, 1)
LOWER_LEFT = Position(1, -1)
UPPER_LEFT = Position(-1, -1)
UPPER_RIGHT = Position(-1, 1)


class SearchField():
    def __init__(self, path: str):
        self.field = parse(path)
        self.nrows = len(self.field)
        self.ncols = len(self.field[0])

    def count_xmas(self):
        s = 0
        for row in range(1, self.nrows - 1):
            for col in range(1, self.ncols - 1):
                p = Position(row, col)
                if self.at(p) == 'A':
                    s += self.xmas_at_pos(p)
        return s

    def xmas_at_pos(self, p: Position):
        diag1 = ''.join([self.at(p + UPPER_LEFT), self.at(p), self.at(p + LOWER_RIGHT)])
        diag2 = ''.join([self.at(p + UPPER_RIGHT), self.at(p), self.at(p + LOWER_LEFT)])
        if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM'):
            return True
        return False
        
    def at(self, p):
        return self.field[p.row][p.col]
            

def main():
    infile = sys.argv[1]
    sf = SearchField(infile)
    print(sf.count_xmas())
    

def parse(file: str):
    lines = []
    with open(file, 'r') as fin:
        for line in fin:
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    main()