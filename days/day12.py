from .day import Day


class Day12(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connections: dict[int, set[int]] = self.parse()

    def in_group(self, val: int) -> set[int]:
        seen = {val}
        work = [val]
        while work:
            pos = work.pop()
            for next_pos in self.connections[pos]:
                if next_pos not in seen:
                    seen.add(next_pos)
                    work.append(next_pos)
        return seen

    def part1(self) -> str:
        return str(len(self.in_group(0)))

    def part2(self) -> str:
        unvisited = set(self.connections.keys())
        groups = 0
        while unvisited:
            groups += 1
            unvisited -= self.in_group(unvisited.pop())
        return str(groups)

    def parse(self) -> dict[int, set[int]]:
        connections = {}
        for line in self.data_lines():
            left, rights = line.split(' <-> ')
            left = int(left)
            for right in rights.split(', '):
                right = int(right)
                left_set = connections.setdefault(left, set())
                right_set = connections.setdefault(right, set())
                left_set.add(right)
                right_set.add(left)
        return connections
