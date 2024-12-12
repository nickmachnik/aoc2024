#!/usr/bin/env python

import sys
from queue import Queue
import numpy as np

class Map():
    def __init__(self, infile):
        self._parse(infile)
        self.nrows = len(self.map)
        self.ncols = len(self.map[0])
        # self._print_map()

    def _print_map(self):
        for row in self.map:
            print(''.join([str(e) for e in row]))

    def get_price_sum(self):
        price_sum = 0
        self.visited = np.zeros_like(self.map)
        for row in range(self.nrows):
            for col in range(self.ncols):
                if not self.visited[row, col]:
                    self.visited[row, col] = 1
                    price_sum += self.get_price_of_patch((row, col))
        return price_sum

    def add_entry_to_row_perim(self, perim, p, direction):
        row, col = p
        if row not in perim:
            perim[row] = set()
        perim[row].add((col, direction))

    def add_entry_to_col_perim(self, perim, p, direction):
        row, col = p
        if col not in perim:
            perim[col] = set()
        perim[col].add((row, direction))

    def get_price_of_patch(self, start):
        area = 0
        perims_row = {}
        perims_col = {}
        patch_sym = self.at(start)
        q = Queue()
        q.put(start)
        while not q.empty():
            pos = q.get()
            area += 1
            for nb in self.get_neighbors(pos): 
                if not self.is_in_bounds(nb) or self.at(nb) != patch_sym:
                    # figure out if this is above, below, left or right
                    # horizontal perim, up or down?
                    if nb[0] < pos[0]:
                        # above
                        self.add_entry_to_row_perim(perims_row, nb, 'up')
                    elif nb[0] > pos[0]:
                        # below
                        self.add_entry_to_row_perim(perims_row, pos, 'down')
                    elif nb[1] < pos[1]:
                        # left
                        self.add_entry_to_col_perim(perims_col, nb, 'left')
                    elif nb[1] > pos[1]:
                        # right
                        self.add_entry_to_col_perim(perims_col, pos, 'right')
                elif not self.visited[nb[0], nb[1]]:
                    q.put(nb)
                    self.visited[nb[0], nb[1]] = 1
        # resolve perims
        prm = 0
        for row, entries in perims_row.items():
            se = sorted(list(entries))
            # print(row, se)
            n_parts = 1
            for i in range(1, len(se)):
                if se[i][1] != se[i - 1][1] or (se[i][0] - se[i - 1][0]) > 1:
                    n_parts += 1
            prm += n_parts
        for col, entries in perims_col.items():
            se = sorted(list(entries))
            # print(se, col)
            n_parts = 1
            for i in range(1, len(se)):
                if se[i][1] != se[i - 1][1] or (se[i][0] - se[i - 1][0]) > 1:
                    n_parts += 1
            prm += n_parts
        # print(patch_sym, area, prm)
        return area * prm

    def get_neighbors(self, pos: (int, int)):
        cand = [
            (pos[0], pos[1] + 1),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0] - 1, pos[1]),
        ]
        return cand

    def is_in_bounds(self, p):
        return p[0] >= 0 and p[1] >= 0 and p[0] < self.nrows and p[1] < self.ncols

    def at(self, pos: (int, int)):
        return self.map[pos[0]][pos[1]]

    def _parse(self, infile):
        self.map = []
        with open(infile, 'r') as fin:
            for line in fin:
                self.map.append([e for e in line.strip()])

def main():
    infile = sys.argv[1]
    m = Map(infile)
    print(m.get_price_sum())

if __name__ == "__main__":
    main()