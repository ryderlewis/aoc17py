from typing import Any, Optional

from .day import Day
from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    SET = "set"
    SUB = "sub"
    MUL = "mul"
    JNZ = "jnz"


@dataclass
class Instruction:
    idx: int
    action: Action
    op1: Any
    op2: Any = None


class Machine:
    def __init__(self, instructions: list[Instruction], reg_a: int = 0):
        self.instructions = instructions
        self.reg_a = reg_a
        self._reset()

    def __iter__(self):
        self._reset()
        return self

    def __next__(self) -> Optional[Instruction]:
        if self.pos < 0 or self.pos >= len(self.instructions):
            raise StopIteration()

        executed = True
        inst = self.instructions[self.pos]
        self.pos += 1

        if isinstance(inst.op1, str):
            op1_val = self.registers.setdefault(inst.op1, 0)
        else:
            op1_val = inst.op1

        if isinstance(inst.op2, str):
            op2_val = self.registers.setdefault(inst.op2, 0)
        else:
            op2_val = inst.op2

        if inst.action == Action.SET:
            self.registers[inst.op1] = op2_val
        elif inst.action == Action.SUB:
            self.registers[inst.op1] -= op2_val
        elif inst.action == Action.MUL:
            self.registers[inst.op1] *= op2_val
        elif inst.action == Action.JNZ:
            if op1_val == 0:
                executed = False
            else:
                self.pos -= 1  # undo the default add
                self.pos += op2_val
        else:
            raise ValueError(inst)

        if executed:
            return inst
        else:
            return None

    def _reset(self) -> None:
        self.registers: dict[str, int] = {'a': self.reg_a}
        self.pos: int = 0

class Day23(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        instructions = self.parse()
        machine = Machine(instructions)
        count = 0
        for inst in machine:
            if inst and inst.action == Action.MUL:
                count += 1
        return str(count)

    def part2(self) -> str:
        instructions = self.parse()
        # print(instructions)
        machine = Machine(instructions, reg_a=1)
        for ct, inst in enumerate(machine):
            if inst and inst.idx in (32,):
                if inst.idx == 24 and machine.registers['g'] < -100_000:
                    to_add = abs(machine.registers['g']) - 1
                    machine.registers['g'] += to_add
                    machine.registers['d'] += to_add
                if inst.idx == 32:
                    print(f"{ct=}, {inst=}, {machine.registers=}")
        return str(machine.registers['h'])

    def parse(self) -> list[Instruction]:
        ret = []
        for line in self.data_lines():
            action, *ops = line.split()
            if len(ops) == 1:
                op1, op2 = ops[0], None
            else:
                op1, op2 = ops
            if op1.lstrip('-').isdigit():
                op1 = int(op1)
            if op2 and op2.lstrip('-').isdigit():
                op2 = int(op2)
            ret.append(Instruction(len(ret)+1, Action(action), op1, op2))
        return ret

"""
01: a=1                 # implied in part 2
01: b=81                # set b 81
02: c=b                 # set c b
03: if a != 0; goto 05  # jnz a 2
04: goto 09             # jnz 1 5
05: b *= 100            # mul b 100
06: b += 100_000        # sub b -100000
07: c = b               # set c b
08: c += 17_000         # sub c -17000
09: f = 1               # set f 1
10: d = 2               # set d 2
11: e = 2               # set e 2
12: g = d               # set g d
13: g *= e              # mul g e
14: g -= b              # sub g b
15: if g != 0; goto 17  # jnz g 2
16: f = 0               # set f 0
17: e += 1              # sub e -1
18: g = e               # set g e
19: g -= b              # sub g b
20: if g != 0; goto 12  # jnz g -8
21: d += 1              # sub d -1
22: g = d               # set g d
23: g -= b              # sub g b
24: if g != 0; goto 11  # jnz g -13
25: if f != 0; goto 27  # jnz f 2
26: h += 1              # sub h -1
27: g = b               # set g b
28: g -= c              # sub g c
29: if g != 0; goto 31  # jnz g 2
30: return h            # jnz 1 3
31: b += 17             # sub b -17
32: goto 09             # jnz 1 -23
"""