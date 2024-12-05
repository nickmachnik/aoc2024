#!/usr/bin/env python

import sys


def main():
    infile = sys.argv[1]
    s, updates = parse(infile)
    print(sum(check_update(u, s) for u in updates))
    

def check_update(update, successors) -> int:
    u = update
    s = successors
    mid = u[int((len(u) - 1) / 2)]
    pre = set()
    for e in u:
        if e in s and len(pre & s[e]) > 0:
            return 0
        pre.add(e)
    return mid


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