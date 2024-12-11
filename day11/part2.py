#!/usr/bin/env python

import sys
import math

class Arrangement():
    def __init__(self, infile):
        self.nums = dict()
        self.next_nums = dict()
        with open(infile, 'r') as fin:
            for e in next(fin).split():
                self.add_num(int(e))
    
    def add_num(self, num):
        if num not in self.nums:
            self.nums[num] = 0
        self.nums[num] += 1

    def add_to_next_nums(self, num, count):
        if num not in self.next_nums:
            self.next_nums[num] = 0
        self.next_nums[num] += count

    def process_nums(self):
        self.next_nums = dict()
        for num, count in self.nums.items():
            for next_num in process_num(num):
                self.add_to_next_nums(next_num, count)
        self.nums = self.next_nums

    def blink(self):
        self.process_nums()

    def count_stones(self):
        return sum(self.nums.values())


def process_num(num: int) -> list[int]:
    res = []
    if num == 0:
        return [num + 1]
    elif num_digits(num) % 2 == 0:
        return split(num)
    else:
        return [num * 2024]


def num_digits(num: int) -> int:
    if num == 0:
        return 1
    else:
        return math.floor(math.log10(num)) + 1


def split(num) -> list[int]:
    nd = num_digits(num)
    cp = nd - 1
    rest = num
    left = 0
    len_split = nd // 2
    for i in range(0, len_split):
        leading_digit = (rest // 10**cp)
        left += leading_digit * 10**(len_split - i - 1)
        rest -= leading_digit * 10**cp
        cp -= 1
    right = 0
    for i in range(0, len_split):
        leading_digit = (rest // 10**cp)
        right += leading_digit * 10**(len_split - i - 1)
        rest -= leading_digit * 10**cp
        cp -= 1
    return [left, right]


def main():
    infile = sys.argv[1]
    arr = Arrangement(infile)
    num_blinks = 75
    for _ in range(num_blinks):
        arr.blink()
    print(arr.count_stones())


if __name__ == "__main__":
    main()