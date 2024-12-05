#!/usr/bin/env python

import sys
from functools import cmp_to_key


class UpdateSorter():
    def __init__(self, update, successors):
        self.u = update
        self.s = successors

    def compare(self, a, b) -> int:
        if a in self.s and b in self.s[a]:
            return -1
        elif b in self.s and a in self.s[b]:
            return 1
        else:
            return 0

    def sort_update(self) -> int:
        u = sorted(self.u, key=cmp_to_key(self.compare))
        return u[int((len(u) - 1) / 2)]


def main():
    infile = sys.argv[1]
    s, updates = parse(infile)
    print(sum(UpdateSorter(u, s).sort_update() for u in updates if not is_valid(u, s)))


def is_valid(update, successors) -> int:
    u = update
    s = successors
    pre = set()
    for e in u:
        if e in s and len(pre & s[e]) > 0:
            return False
        pre.add(e)
    return True


def parse(file: str):
    successors = {}
    updates = []
    with open(file, 'r') as fin:
        succ = True
        for line in fin:
            line = line.strip()
            if line == '':
                succ = False
                continue
            if succ:
                a, b = [int(e) for e in line.split('|')]
                if a not in successors:
                    successors[a] = set()
                successors[a].add(b)
            else:
                updates.append([int(e) for e in line.split(',')])
    return successors, updates


if __name__ == "__main__":
    main()