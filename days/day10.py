from .day import Day
from functools import reduce


def dense_hash(s: str) -> str:
    numbers = list(range(256))
    curr_pos, skip_size = 0, 0
    lengths = list(map(ord, s))
    lengths.extend([17, 31, 73, 47, 23])
    for _ in range(64):
        for length in lengths:
            if length > 1:
                start_pos, end_pos = curr_pos, (curr_pos + length - 1) % len(numbers)
                if end_pos > start_pos:
                    rev = list(reversed(numbers[start_pos:end_pos+1]))
                    numbers[start_pos:end_pos+1] = rev
                elif end_pos < start_pos:
                    rev = list(reversed(numbers[start_pos:] + numbers[:end_pos+1]))
                    lpart, rpart = rev[:len(numbers[start_pos:])], rev[len(numbers[start_pos:]):]
                    numbers[start_pos:] = lpart
                    numbers[:end_pos+1] = rpart
            curr_pos += length + skip_size
            curr_pos %= len(numbers)
            skip_size += 1

    dense_hash = []
    for i in range(0, len(numbers), 16):
        nums = numbers[i:i+16]
        digit = reduce(lambda x, y: x^y, nums, 0)
        dense_hash.append(f"{digit:02x}")
    return ''.join(dense_hash)


class Day10(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        numbers = list(range(256))
        curr_pos, skip_size = 0, 0
        lengths = list(map(int, self.data_lines()[0].split(',')))
        for length in lengths:
            if length > 1:
                start_pos, end_pos = curr_pos, (curr_pos + length - 1) % len(numbers)
                if end_pos > start_pos:
                    rev = list(reversed(numbers[start_pos:end_pos+1]))
                    numbers[start_pos:end_pos+1] = rev
                elif end_pos < start_pos:
                    rev = list(reversed(numbers[start_pos:] + numbers[:end_pos+1]))
                    lpart, rpart = rev[:len(numbers[start_pos:])], rev[len(numbers[start_pos:]):]
                    numbers[start_pos:] = lpart
                    numbers[:end_pos+1] = rpart
            curr_pos += length + skip_size
            curr_pos %= len(numbers)
            skip_size += 1
        return str(numbers[0]*numbers[1])

    def part2(self) -> str:
        return dense_hash(self.data_lines()[0])
