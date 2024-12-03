from .day import Day
from collections import namedtuple

Pos = namedtuple('Pos', ('row', 'col'))


class Day19(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def packet_run(self) -> tuple[str, int]:
        grid = self.parse()
        pos = Pos(row=0, col=grid[0].index('|'))
        direction = (1, 0)
        letters = []
        space_count = 0
        step_count = 0

        while True:
            step_count += 1
            # print(f"{pos=}, {direction=}, {grid[pos.row][pos.col]=}, {"".join(letters)=}")
            if grid[pos.row][pos.col] == ' ':
                space_count += 1
                if space_count == 2:
                    break
            else:
                space_count = 0

            if direction[0] == 0:
                # moving horizontally
                if grid[pos.row][pos.col] == '-':
                    # keep going
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                elif grid[pos.row][pos.col] == '+':
                    # time to turn - figure out which way
                    if grid[pos.row-1][pos.col] != ' ':
                        direction = (-1, 0)
                    elif grid[pos.row+1][pos.col] != ' ':
                        direction = (1, 0)
                    else:
                        raise RuntimeError("WUT")
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                elif grid[pos.row][pos.col].isalpha():
                    # hit a letter - record it and keep going
                    letters.append(grid[pos.row][pos.col])
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                else:
                    # keep going
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
            else:
                # moving vertically
                if grid[pos.row][pos.col] == '|':
                    # keep going
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                elif grid[pos.row][pos.col] == '+':
                    # time to turn - figure out which way
                    if grid[pos.row][pos.col-1] != ' ':
                        direction = (0, -1)
                    elif grid[pos.row][pos.col+1] != ' ':
                        direction = (0, 1)
                    else:
                        raise RuntimeError("WUT")
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                elif grid[pos.row][pos.col].isalpha():
                    # hit a letter - record it and keep going
                    letters.append(grid[pos.row][pos.col])
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
                else:
                    # keep going
                    pos = Pos(row=pos.row + direction[0], col=pos.col + direction[1])
        return ''.join(letters), step_count - space_count

    def part1(self) -> str:
        return self.packet_run()[0]

    def part2(self) -> str:
        return str(self.packet_run()[1])

    def parse(self) -> tuple[tuple[str, ...], ...]:
        ret = []
        lines = self.data_lines()
        cols = max(len(l) for l in lines)
        for line in lines:
            row = [' ' for _ in range(cols)]
            for i, c in enumerate(line):
                row[i] = c
            ret.append(tuple(row))
        return tuple(ret)
