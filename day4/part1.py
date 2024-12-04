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


DIRS = [
    Position(0, 1),
    Position(1, 1),
    Position(1, 0),
    Position(1, -1),
    Position(0, -1),
    Position(-1, -1),
    Position(-1, 0),
    Position(-1, 1),
]


class SearchField():
    def __init__(self, path: str):
        self.field = parse(path)
        self.nrows = len(self.field)
        self.ncols = len(self.field[0])

    def count_xmas(self):
        s = 0
        for row in range(self.nrows):
            for col in range(self.ncols):
                p = Position(row, col)
                if self.at(p) == 'X':
                    s += self.count_xmas_from_pos(p)
        return s

    def count_xmas_from_pos(self, p: Position):
        res = 0
        for d in DIRS:
            res += self.xmas_in_dir(p, d)
        return res

    def is_valid_pos(self, p):
        return p.row >= 0 and p.col >= 0 and p.row < self.nrows and p.col < self.ncols

    def at(self, p):
        return self.field[p.row][p.col]

    def xmas_in_dir(self, p, d):
        xmas = 'XMAS'
        for i in range(len(xmas)):
            if not self.is_valid_pos(p) or self.at(p) != xmas[i]:
                return False
            p += d
        return True
            

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