from .day import Day
from collections import Counter


class Day04(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        c = 0
        for line in self.data_lines():
            words = line.split()
            ct = Counter(words)
            if ct.most_common(1)[0][1] == 1:
                c += 1
        return str(c)

    def part2(self) -> str:
        c = 0
        for line in self.data_lines():
            words = [''.join(sorted(w)) for w in line.split()]
            ct = Counter(words)
            if ct.most_common(1)[0][1] == 1:
                c += 1
        return str(c)
