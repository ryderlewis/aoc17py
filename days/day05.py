from .day import Day


class Day05(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        jumps = list(map(int, self.data_lines()))
        idx = 0
        ct = 0
        while 0 <= idx < len(jumps):
            jump = jumps[idx]
            jumps[idx] += 1
            idx += jump
            ct += 1
        return str(ct)

    def part2(self) -> str:
        jumps = list(map(int, self.data_lines()))
        idx = 0
        ct = 0
        while 0 <= idx < len(jumps):
            jump = jumps[idx]
            if jump >= 3:
                jumps[idx] -= 1
            else:
                jumps[idx] += 1
            idx += jump
            ct += 1
        return str(ct)
