from collections import namedtuple
from typing import Iterable
from .day import Day

Pos = namedtuple('Pos', ('x', 'y'))


class Day03(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        num = int(self.data_lines()[0])
        for v, d in self.dist_gen():
            if v == num:
                return str(d)

    def part2(self) -> str:
        num = int(self.data_lines()[0])
        for i, v in enumerate(self.num_gen()):
            if v > num:
                return str(v)

    @staticmethod
    def dist_gen() -> Iterable[tuple[int, int]]:
        # 0, 1,2,1,2,1,2,1,2, 3,2,3,4,3,2,3,4,3,2,3,4,3,2,3,4, 5,4,3,4,5,6,5,4,3,4,5,6,5,4,3,4,5,6,5,4,3,4,5,6
        # 1  9-1=8            25-9=16                          49-25=24
        val = 1
        yield val, 0

        square_width = 3
        while True:
            min_dist = (square_width-1)//2
            max_dist = 2 * min_dist
            dist = max_dist - 1
            ddist = -1
            for _ in range(square_width**2 - (square_width-2)**2):
                val += 1
                yield val, dist
                if dist == min_dist:
                    ddist = 1
                elif dist == max_dist:
                    ddist = -1
                dist += ddist
            square_width += 2

    @staticmethod
    def num_gen() -> Iterable[int]:
        pos = Pos(x=0, y=0)
        val = 1
        vals = {pos: 1}
        yield val

        square_width = 3
        while True:
            deltas = [(1, 0)]
            deltas.extend([(0, -1) for _ in range(square_width-2)])
            deltas.extend([(-1, 0) for _ in range(square_width-1)])
            deltas.extend([(0, 1) for _ in range(square_width-1)])
            deltas.extend([(1, 0) for _ in range(square_width-1)])
            for dx, dy in deltas:
                pos = Pos(x=pos.x+dx, y=pos.y+dy)
                val = sum(vals.get(p, 0) for p in (
                    (pos.x-1, pos.y-1),
                    (pos.x-1, pos.y),
                    (pos.x-1, pos.y+1),
                    (pos.x, pos.y-1),
                    (pos.x, pos.y+1),
                    (pos.x+1, pos.y-1),
                    (pos.x+1, pos.y),
                    (pos.x+1, pos.y+1),
                ))
                vals[pos] = val
                yield val
            square_width += 2
