from .day import Day
from collections import Counter, namedtuple


Pos = namedtuple('Pos', ('x', 'y'))


class Day11(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        steps = Counter(['ne','ne','ne'])
        steps = Counter(['ne','ne','sw','sw'])
        steps = Counter(['ne','ne','s','s'])
        steps = Counter(['se','sw','se','sw','sw'] * 1)
        steps = Counter(self.data_lines()[0].split(','))
        dirs: dict[str, Pos] = dict(
            se=Pos(1, -1),
            ne=Pos(1, 1),
            sw=Pos(-1, -1),
            nw=Pos(-1, 1),
            n=Pos(0, 2),
            s=Pos(0, -2),
        )
        pos = Pos(0, 0)
        for direction, count in steps.items():
            delta = dirs[direction]
            pos = Pos(pos.x + delta.x * count, pos.y + delta.y * count)
        print(pos)
        return str((abs(pos.x) + abs(pos.y))//2)

    def part2(self) -> str:
        return "dayXX 2"
