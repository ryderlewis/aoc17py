from .day import Day


class Day13(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scanners = self.parse()

    def severity(self, start_time: int) -> int:
        severity = 0
        scanners = self.scanners
        for pico in range(max(scanners.keys())+1):
            if pico in scanners:
                depth = scanners[pico]
                caught = (pico+start_time) % ((depth-1)*2) == 0
                if caught:
                    severity += pico * depth
        return severity

    def any_caught(self, start_time: int) -> bool:
        return any((pico+start_time) % ((depth-1)*2) == 0
                   for pico, depth in self.scanners.items())

    def part1(self) -> str:
        return str(self.severity(0))

    def part2(self) -> str:
        i = 0
        while True:
            if self.any_caught(i):
                i += 1
            else:
                return str(i)

    def parse(self) -> dict[int, int]:
        scanners: dict[int, int] = {}
        for line in self.data_lines():
            pos, depth = map(int, line.split(': '))
            scanners[pos] = depth
        return scanners
