from .day import Day
from dataclasses import dataclass, field


@dataclass
class Program:
    name: str
    weight: int
    sub_programs: list["Program"] = field(default_factory=list)

    def full_weight(self) -> int:
        return self.weight + sum(p.full_weight() for p in self.sub_programs)


class Day07(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        programs = self.parse()
        pointed_to = set()
        for p in programs.values():
            for r in p.sub_programs:
                pointed_to.add(r.name)
        root = set(programs.keys()) - pointed_to
        return str(root)

    def part2(self) -> str:
        programs = self.parse()
        culprits = set()
        delta = 0
        for p in programs.values():
            if len(p.sub_programs) > 0:
                vals = sorted([(sp.full_weight(), sp.name) for sp in p.sub_programs])
                if len(vals) > 2 and vals[0][0] != vals[-1][0]:
                    if vals[0][0] == vals[1][0]:
                        # in this case, vals[-1] has the wrong weight
                        bad_prog = programs[vals[-1][1]]
                    else:
                        # in this case, vals[0] has the wrong weight
                        bad_prog = programs[vals[0][1]]
                    target_weight = vals[1][0]
                    actual_weight = bad_prog.full_weight()
                    if delta == 0:
                        delta = target_weight - actual_weight
                    else:
                        assert delta == target_weight - actual_weight
                    culprits.add(bad_prog.name)
        for c in culprits:
            prog = programs[c]
            if not any(sp.name in culprits for sp in prog.sub_programs):
                print(f"bad program = {prog.name}")
                return str(prog.weight + delta)

    def parse(self) -> dict[str, Program]:
        programs = {}
        prights = {}
        for line in self.data_lines():
            parts = line.split(' -> ')
            name, weight = parts[0].split()
            weight = int(weight.strip('()'))
            p = Program(name, weight)
            programs[name] = p
            if len(parts) > 1:
                prights[name] = parts[1].split(', ')
        for name, rights in prights.items():
            programs[name].sub_programs = [programs[n] for n in rights]
        return programs
