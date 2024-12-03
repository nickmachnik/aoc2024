#!/usr/bin/env python

import sys
import re


def main():
    infile = sys.argv[1]
    lines = parse(infile)
    print(sum(eval_muls(re.findall(r'mul\([0-9]+,[0-9]+\)', l)) for l in lines))

def eval_muls(muls):
    s = 0
    for mul in muls:
        sub = mul.strip(')')
        a, b = sub.split(',')
        _, a = a.split('(')
        s += int(a) * int(b)
    return s


def parse(file: str):
    lines = []
    with open(file, 'r') as fin:
        for line in fin:
            lines.append(line)
    return lines

if __name__ == "__main__":
    main()