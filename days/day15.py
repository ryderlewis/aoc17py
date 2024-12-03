from .day import Day


class Day15(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        gen_a, gen_b = self.generators()
        count = 0
        for _ in range(40_000_000):
            if gen_a & 0xffff == gen_b & 0xffff:
                count += 1
            gen_a = (gen_a * 16807) % 2147483647
            gen_b = (gen_b * 48271) % 2147483647
        return str(count)

    def part2(self) -> str:
        a, b = self.generators()

        def gen_a():
            nonlocal a
            while True:
                if a % 4 == 0:
                    yield a
                a = (a * 16807) % 2147483647

        def gen_b():
            nonlocal b
            while True:
                if b % 8 == 0:
                    yield b
                b = (b * 48271) % 2147483647

        count = 0
        for i, a_val, b_val in zip(range(5_000_000), gen_a(), gen_b()):
            if a_val & 0xffff == b_val & 0xffff:
                count += 1
        return str(count)

    def generators(self) -> tuple[int, int]:
        gen_a, gen_b = self.data_lines()
        gen_a = int(gen_a.split()[-1])
        gen_b = int(gen_b.split()[-1])
        return gen_a, gen_b
