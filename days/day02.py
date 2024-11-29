from .day import Day


class Day02(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        s = 0
        for vals in self.parse():
            v = sorted(vals)
            s += v[-1] - v[0]
        return str(s)

    def part2(self) -> str:
        s = 0
        for vals in self.parse():
            v = sorted(vals)
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    if v[j] % v[i] == 0:
                        s += v[j]//v[i]
        return str(s)

    def parse(self) -> list[list[int]]:
        return [
            list(map(int, line.split()))
            for line in self.data_lines()
        ]