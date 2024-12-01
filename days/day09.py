from .day import Day


class Day09(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        line = self.data_lines()[0]
        score = 0
        nest = 0
        garbage = False

        i = 0
        while i < len(line):
            c = line[i]
            i += 1
            if c == '!':
                i += 1
            elif garbage:
                if c == '>':
                    garbage = False
            elif c == '<':
                garbage = True
            elif c == '{':
                # new group starting
                nest += 1
                score += nest
            elif c == '}':
                nest -= 1
            else:
                # character within a group, but not garbage
                pass

        return str(score)

    def part2(self) -> str:
        line = self.data_lines()[0]
        score = 0
        garbage = False

        i = 0
        while i < len(line):
            c = line[i]
            i += 1
            if c == '!':
                i += 1
            elif garbage:
                if c == '>':
                    garbage = False
                else:
                    score += 1
            elif c == '<':
                garbage = True
            else:
                # character within a group, but not garbage
                pass

        return str(score)
