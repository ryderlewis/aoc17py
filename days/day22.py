from .day import Day
from collections import namedtuple


Pos = namedtuple('Pos', 'x y')
DIRS = (Pos(0, 1), Pos(1, 0), Pos(0, -1), Pos(-1, 0))
CLEAN = '.'
WEAKENED = 'w'
INFECTED = '#'
FLAGGED = 'f'


class Day22(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        infected = self.parse()
        count = 0
        pos = Pos(0, 0)
        direction = 0
        for _ in range(10_000):
            if pos in infected:
                direction += 1
                infected.discard(pos)
            else:
                direction -= 1
                infected.add(pos)
                count += 1
            direction %= len(DIRS)
            pos = Pos(pos.x + DIRS[direction].x, pos.y + DIRS[direction].y)
        return str(count)

    def part2(self) -> str:
        state = {pos: INFECTED for pos in self.parse()}
        count = 0
        pos = Pos(0, 0)
        direction = 0
        for _ in range(10_000_000):
            s = state.get(pos, CLEAN)
            if s == CLEAN:
                direction -= 1
                state[pos] = WEAKENED
            elif s == WEAKENED:
                state[pos] = INFECTED
                count += 1
            elif s == INFECTED:
                state[pos] = FLAGGED
                direction += 1
            elif s == FLAGGED:
                del state[pos] # clean
                direction += 2
            direction %= len(DIRS)
            pos = Pos(pos.x + DIRS[direction].x, pos.y + DIRS[direction].y)
        return str(count)

    def parse(self) -> set[Pos]:
        ret = set()
        lines = self.data_lines()
        w, h = len(lines[0]), len(lines)
        mid_x, mid_y = w//2, h//2
        for y in range (-mid_y, mid_y+1):
            for x in range(-mid_x, mid_x+1):
                if lines[mid_y-y][mid_x+x] == '#':
                    ret.add(Pos(x, y))
        return ret
