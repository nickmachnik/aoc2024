#!/usr/bin/env python

import sys

def main():
    infile = sys.argv[1]
    dense_mem = parse_input(infile)
    res = 0
    back_pos = len(dense_mem) - 1
    block_index = 0
    for dense_pos, pos_size in enumerate(dense_mem):
        if dense_pos > back_pos:
            break
        if dense_pos % 2 == 0:
            # just increment score
            file_id = (dense_pos / 2)
            for _ in range(pos_size):
                res += block_index * file_id
                block_index += 1
        else:
            # empty block, fill
            for _ in range(pos_size):
                if dense_mem[back_pos] == 0:
                    # jump to next file
                    back_pos -= 2
                dense_mem[back_pos] -= 1
                res += (back_pos / 2) * block_index
                block_index += 1
    print(int(res))


def parse_input(file):
    with open(file, 'r') as fin:
        return [int(e) for e in next(fin).strip()]


if __name__ == "__main__":
    main()