from typing import AnyStr, Any

from .day import Day
from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    PLAY_SOUND = "snd"
    SET_REGISTER = "set"
    ADD = "add"
    MUL = "mul"
    MOD = "mod"
    RECOVER = "rcv"
    JUMP_GT_ZERO = "jgz"


@dataclass
class Instruction:
    action: Action
    op1: Any
    op2: Any = None


class Day18(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        instructions = self.parse()
        registers: dict[str, int] = {}
        pos = 0
        last_frequency = None

        while 0 <= pos < len(instructions):
            inst = instructions[pos]
            pos += 1

            if isinstance(inst.op1, str):
                op1_val = registers.setdefault(inst.op1, 0)
            else:
                op1_val = inst.op1

            if isinstance(inst.op2, str):
                op2_val = registers.setdefault(inst.op2, 0)
            else:
                op2_val = inst.op2

            if inst.action == Action.PLAY_SOUND:
                last_frequency = op1_val
            elif inst.action == Action.SET_REGISTER:
                registers[inst.op1] = op2_val
            elif inst.action == Action.ADD:
                registers[inst.op1] += op2_val
            elif inst.action == Action.MUL:
                registers[inst.op1] *= op2_val
            elif inst.action == Action.MOD:
                registers[inst.op1] %= op2_val
            elif inst.action == Action.RECOVER:
                if op1_val != 0:
                    return str(last_frequency)
            elif inst.action == Action.JUMP_GT_ZERO:
                if op1_val > 0:
                    pos -= 1  # undo the default add
                    pos += op2_val
            else:
                raise ValueError(inst)

    def part2(self) -> str:
        return "dayXX 2"

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
            ret.append(Instruction(Action(action), op1, op2))
        return ret
