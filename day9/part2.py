#!/usr/bin/env python

import sys

def main():
    infile = sys.argv[1]
    file_sizes = parse_input(infile)
    first_block_index = [0] * len(file_sizes)
    block_index = 0
    for dense_pos, pos_size in enumerate(file_sizes):
        first_block_index[dense_pos] = block_index
        block_index += pos_size

    # will just work on the checksums of the empty file slots first, then iterate over
    # file sizes again and add the rest
    checksums = [0] * len(file_sizes)

    # let's hope that n^2 complexity is alright here
    for back_pos in range(len(file_sizes) - 1, 0, -2):
        file_size = file_sizes[back_pos]
        file_id = (back_pos // 2)
        for gap_pos in range(1, back_pos, 2):
            if file_sizes[gap_pos] < file_size:
                continue
            # rm file from back, add to front, incr checksum, reduce gap size
            file_sizes[back_pos] = 0
            file_sizes[gap_pos] -= file_size
            for block_index in range(first_block_index[gap_pos], first_block_index[gap_pos] + file_size):
                checksums[gap_pos] += file_id * block_index
            first_block_index[gap_pos] += file_size
            break

    # now we've moved all files, we need to compute checksums of files at even positions and then add all checksums
    res = 0
    for i in range(len(file_sizes)):
        if i % 2 == 0:
            # compute checksum
            file_id = (i // 2)
            for block_index in range(first_block_index[i], first_block_index[i] + file_sizes[i]):
                checksums[i] += block_index * file_id
        res += checksums[i]
    print(int(res))


def parse_input(file):
    with open(file, 'r') as fin:
        return [int(e) for e in next(fin).strip()]


if __name__ == "__main__":
    main()