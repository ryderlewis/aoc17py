from typing import Any

from .day import Day


SPIN = 's'
EXCHANGE = 'x'
PARTNER = 'p'


class Day16(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def dance(programs: tuple[str, ...], moves: list[tuple[str, Any, ...]]) -> tuple[str, ...]:
        programs = list(programs)
        for move in moves:
            if move[0] == EXCHANGE:
                programs[move[1]], programs[move[2]] = programs[move[2]], programs[move[1]]
            elif move[0] == PARTNER:
                p1 = programs.index(move[1])
                p2 = programs.index(move[2])
                programs[p1], programs[p2] = programs[p2], programs[p1]
            elif move[0] == SPIN:
                x = move[1]
                assert 0 < x < len(programs)
                programs = programs[-x:] + programs[:-x]
        return tuple(programs)

    def part1(self) -> str:
        programs = tuple('abcdefghijklmnop')
        return ''.join(self.dance(programs, self.dance_moves()))

    def part2(self) -> str:
        programs = tuple('abcdefghijklmnop')
        seen = {programs: 0}
        moves = self.dance_moves()

        cycle_size = 0
        i = 1
        while True:
            programs = self.dance(programs, moves)
            if programs in seen:
                cycle_size = i
                break
            else:
                seen[programs] = i
                i += 1

        remaining = 1_000_000_000 % cycle_size
        for _ in range(remaining):
            programs = self.dance(programs, moves)
        return ''.join(programs)

    def dance_moves(self) -> list[tuple[str, Any, ...]]:
        ret = []
        for val in self.data_lines()[0].split(','):
            move, val = val[:1], val[1:]
            if move == SPIN:
                ret.append((move, int(val)))
            elif move == EXCHANGE:
                p1, p2 = map(int, val.split('/'))
                ret.append((move, p1, p2))
            elif move == PARTNER:
                p1, p2 = val.split('/')
                ret.append((move, p1, p2))
            else:
                raise ValueError(move)

        return ret
