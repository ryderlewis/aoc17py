from .day import Day
from dataclasses import dataclass
import re


@dataclass
class Instruction:
    reg_a: str
    act_a: str
    val_a: int
    reg_b: str
    cmp_b: str
    val_b: int

    def run(self, registers: dict[str, int]) -> bool:
        condition_pass = False
        if self.cmp_b == "!=":
            condition_pass = registers.get(self.reg_b, 0) != self.val_b
        elif self.cmp_b == "<=":
            condition_pass = registers.get(self.reg_b, 0) <= self.val_b
        elif self.cmp_b == "<":
            condition_pass = registers.get(self.reg_b, 0) < self.val_b
        elif self.cmp_b == ">":
            condition_pass = registers.get(self.reg_b, 0) > self.val_b
        elif self.cmp_b == ">=":
            condition_pass = registers.get(self.reg_b, 0) >= self.val_b
        elif self.cmp_b == "==":
            condition_pass = registers.get(self.reg_b, 0) == self.val_b

        if condition_pass:
            if self.act_a == 'inc':
                registers[self.reg_a] = registers.get(self.reg_a, 0) + self.val_a
            elif self.act_a == 'dec':
                registers[self.reg_a] = registers.get(self.reg_a, 0) - self.val_a
            return True
        else:
            return False

class Day08(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        instructions = self.parse()
        registers = {}
        for i in instructions:
            i.run(registers)
        return str(max(registers.values()))

    def part2(self) -> str:
        instructions = self.parse()
        registers = {}
        max_val = 0
        for i in instructions:
            i.run(registers)
            max_val = max(max_val, max(registers.values()))
        return str(max_val)

    def parse(self) -> list[Instruction]:
        ret = []
        for line in self.data_lines():
            if m := re.match(r'^(\w+) (\w+) (-?\d+) if (\w+) (\S+) (-?\d+)$', line):
                ra, aa, va, rb, cb, vb = m.groups()
                ret.append(Instruction(
                    reg_a=ra,
                    act_a=aa,
                    val_a=int(va),
                    reg_b=rb,
                    cmp_b=cb,
                    val_b=int(vb),
                ))
            else:
                raise RuntimeError(line)
        return ret
