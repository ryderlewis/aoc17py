from .day import Day


class Day06(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        banks = list(map(int, self.data_lines()[0].split()))
        seen = {tuple(banks)}
        while True:
            v = max(banks)
            i = banks.index(v)
            next_banks = banks.copy()
            next_banks[i] = 0
            dist = v//(len(banks)-1)
            for j in range(len(banks)):
                if j != i:
                    next_banks[j] += dist
            remain = v % (len(banks)-1)
            for j in range(1, remain+1):
                next_banks[(i+j) % len(banks)] += 1
            banks, t = next_banks, tuple(next_banks)

            if t in seen:
                return str(len(seen))
            seen.add(t)

    def part2(self) -> str:
        banks = list(map(int, self.data_lines()[0].split()))
        seen = {tuple(banks)}
        inf = False
        while True:
            v = max(banks)
            i = banks.index(v)
            next_banks = banks.copy()
            next_banks[i] = 0
            dist = v//(len(banks)-1)
            for j in range(len(banks)):
                if j != i:
                    next_banks[j] += dist
            remain = v % (len(banks)-1)
            for j in range(1, remain+1):
                next_banks[(i+j) % len(banks)] += 1
            banks, t = next_banks, tuple(next_banks)

            if t in seen:
                if inf:
                    return str(len(seen))
                else:
                    inf = True
                    seen = set()
            seen.add(t)
