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
        set_bits = set()
        for row, h in enumerate(hashes):
            for col, b in enumerate(self.bits(h)):
                if b:
                    set_bits.add((row, col))
        group_count = 0
        while set_bits:
            group_count += 1
            group = self.in_group(set_bits.pop(), set_bits)
            set_bits -= group
        return str(group_count)

    @staticmethod
    def bits(h: str) -> list[int]:
        ret = []
        for c in h:
            v = int(c, 16)
            ret.append((v >> 3) & 1)
            ret.append((v >> 2) & 1)
            ret.append((v >> 1) & 1)
            ret.append((v >> 0) & 1)
        return ret

    @staticmethod
    def in_group(val: tuple[int, int], all_vals: set[tuple[int, int]]) -> set[tuple[int, int]]:
        seen = {val}
        work = [val]
        while work:
            pos = work.pop()
            neighbors = [
                (pos[0]+1, pos[1]),
                (pos[0]-1, pos[1]),
                (pos[0], pos[1]-1),
                (pos[0], pos[1]+1),
            ]
            for neighbor in neighbors:
                if neighbor in all_vals and neighbor not in seen:
                    seen.add(neighbor)
                    work.append(neighbor)
        return seen
