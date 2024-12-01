from .day import Day
from .day10 import dense_hash


class Day14(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        in_val = self.data_lines()[0]
        hashes = [dense_hash(f"{in_val}-{i}") for i in range(128)]
        return str(sum(int(h, 16).bit_count() for h in hashes))

    def part2(self) -> str:
        in_val = self.data_lines()[0]
        hashes = [dense_hash(f"{in_val}-{i}") for i in range(128)]
        return "dayXX 2"
