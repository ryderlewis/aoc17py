from .day import Day


class Day24(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        return str(self.strongest(self.parse(), 0))

    def part2(self) -> str:
        return str(self.longest(self.parse(), 0)[1])

    @staticmethod
    def strongest(components: list[tuple[int, int]], start: int) -> int:
        best = 0
        for i, component in enumerate(components):
            if component[0] == start:
                score = sum(component) + Day24.strongest(components[:i] + components[i+1:], component[1])
                best = max(best, score)
            elif component[1] == start:
                score = sum(component) + Day24.strongest(components[:i] + components[i+1:], component[0])
                best = max(best, score)
        return best

    @staticmethod
    def longest(comps: list[tuple[int, int]], start: int) -> tuple[int, int]:
        length = 0
        strength = 0

        for i, c in enumerate(comps):
            if c[0] == start:
                l, s = Day24.longest(comps[:i] + comps[i + 1:], c[1])
            elif c[1] == start:
                l, s = Day24.longest(comps[:i] + comps[i + 1:], c[0])
            else:
                l, s = None, None

            if l is not None:
                l += 1
                s += sum(c)

                if l > length:
                    length = l
                    strength = s
                elif l == length:
                    strength = max(s, strength)

        return length, strength

    def parse(self) -> list[tuple[int, ...]]:
        return sorted([tuple(sorted(map(int, line.split('/')))) for line in self.data_lines()])
