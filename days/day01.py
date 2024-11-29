from .day import Day


class Day01(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        line = self.data_lines()[0]
        return str(sum(int(c) for i, c in enumerate(line)
                   if c == line[(i+1)%len(line)]))

    def part2(self) -> str:
        line = self.data_lines()[0]
        return str(sum(int(c) for i, c in enumerate(line)
                       if c == line[(i+len(line)//2)%len(line)]))
