from .day import Day
from collections import Counter
from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int

    def dist(self) -> int:
        # calc distance
        x, y = abs(self.x), abs(self.y)
        if x > y:
            return x
        return x + (y-x)//2


class Day11(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dirs: dict[str, Pos] = dict(
            se=Pos(1, -1),
            ne=Pos(1, 1),
            sw=Pos(-1, -1),
            nw=Pos(-1, 1),
            n=Pos(0, 2),
            s=Pos(0, -2),
        )

    def part1(self) -> str:
        steps = Counter(self.data_lines()[0].split(','))
        pos = Pos(0, 0)
        for direction, count in steps.items():
            delta = self.dirs[direction]
            pos.x += delta.x * count
            pos.y += delta.y * count
        # calc distance
        return str(pos.dist())

    def part2(self) -> str:
        steps = self.data_lines()[0].split(',')
        pos = Pos(0, 0)
        max_dist = 0
        for direction in steps:
            delta = self.dirs[direction]
            pos.x += delta.x
            pos.y += delta.y
            max_dist = max(max_dist, pos.dist())
        # calc distance
        return str(max_dist)
