from .day import Day


class Pattern:
    def __init__(self, search: str, replace: str):
        self.search = tuple(tuple(row) for row in search.split('/'))
        self.replace = tuple(tuple(row) for row in replace.split('/'))
        self.search_patterns = set()
        self._populate_search_patterns()

    def _populate_search_patterns(self):
        self.search_patterns = set()
        flipped = tuple(tuple(reversed(row)) for row in self.search)
        for grid in (self.search, flipped):
            self.search_patterns.add(grid)
            for _ in range(3):
                grid = self._rotate(grid)
                self.search_patterns.add(grid)

    @staticmethod
    def _rotate(grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
        rows = []
        for col in range(-1, -len(grid[0])-1, -1):
            rows.append(tuple(grid[row][col] for row in range(len(grid))))
        return tuple(rows)


class Day21(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.patterns = self.parse()

    def grow(self, grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
        if len(grid) % 2 == 0:
            tile = 2
        else:
            tile = 3

        replacements = []
        for row in range(0, len(grid), tile):
            for col in range(0, len(grid[0]), tile):
                search = []
                for r in range(tile):
                    search.append(tuple(grid[row+r][col:col+tile]))
                search = tuple(search)

                found = False
                for p in self.patterns:
                    if search in p.search_patterns:
                        replacements.append(p.replace)
                        found = True
                        break
                assert found

        size = len(grid) // tile
        new_grid = [[' ' for _ in range(size * (tile + 1))] for _ in range(size * (tile + 1))]
        for i, replacement in enumerate(replacements):
            row = (i//size) * (tile + 1)
            col = (i % size) * (tile + 1)
            for r in range(len(replacement)):
                for c in range(len(replacement[r])):
                    new_grid[row+r][col+c] = replacement[r][c]
        return tuple(tuple(row) for row in new_grid)

    def part1(self) -> str:
        grid = (tuple('.#.'), tuple('..#'), tuple('###'))
        for _ in range(5):
            grid = self.grow(grid)
        return str(sum(sum(1 for c in row if c == '#') for row in grid))

    def part2(self) -> str:
        grid = (tuple('.#.'), tuple('..#'), tuple('###'))
        for _ in range(18):
            grid = self.grow(grid)
        return str(sum(sum(1 for c in row if c == '#') for row in grid))

    def parse(self) -> list[Pattern]:
        ret = []
        for line in self.data_lines():
            search, replace = line.split(' => ')
            ret.append(Pattern(search, replace))
        return ret
