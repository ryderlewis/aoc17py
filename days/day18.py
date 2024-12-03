from typing import Any, Optional

from .day import Day
from dataclasses import dataclass
from enum import Enum
from collections import deque


class Locked(StopIteration):
    pass


class Action(Enum):
    SND = "snd"
    RCV = "rcv"
    SET_REGISTER = "set"
    ADD = "add"
    MUL = "mul"
    MOD = "mod"
    JUMP_GT_ZERO = "jgz"


@dataclass
class Instruction:
    action: Action
    op1: Any
    op2: Any = None


class Machine:
    def __init__(self, instructions: list[Instruction], machine_id: int = 0, with_ipc: bool = False):
        self.instructions = instructions
        self.with_ipc = with_ipc
        self.machine_id = machine_id
        self._reset()

    def send(self, val: int):
        self.rx_queue.appendleft(val)

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

        if inst.action == Action.SND:
            self.last_snd_val = op1_val
        elif inst.action == Action.RCV:
            if self.with_ipc:
                if len(self.rx_queue) == 0:
                    raise Locked()
                self.registers[inst.op1] = self.rx_queue.pop()
            else:
                if op1_val == 0:
                    executed = False
        elif inst.action == Action.SET_REGISTER:
            self.registers[inst.op1] = op2_val
        elif inst.action == Action.ADD:
            self.registers[inst.op1] += op2_val
        elif inst.action == Action.MUL:
            self.registers[inst.op1] *= op2_val
        elif inst.action == Action.MOD:
            self.registers[inst.op1] %= op2_val
        elif inst.action == Action.JUMP_GT_ZERO:
            if op1_val <= 0:
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
        self.registers: dict[str, int] = {}
        self.pos: int = 0
        self.last_snd_val = None
        self.rx_queue = deque()
        if self.with_ipc:
            self.registers['p'] = self.machine_id
            print(f"{self.registers=}")

class Day18(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        instructions = self.parse()
        machine = Machine(instructions)
        for inst in machine:
            if inst and inst.action == Action.RCV:
                return str(machine.last_snd_val)

    def part2(self) -> str:
        instructions = self.parse()
        m0 = Machine(instructions, with_ipc=True, machine_id=0)
        m1 = Machine(instructions, with_ipc=True, machine_id=1)
        a, b = iter(m0), iter(m1)
        am, bm = m0, m1
        m1_send_count = 0
        locked_count = 0
        swap = False

        while True:
            if swap:
                a, b = b, a
                am, bm = bm, am
                swap = False
                print(f"Swapping: {'m0' if am is m0 else 'm1'} now active. {m1_send_count=}")

            try:
                i = next(a)
                # print(f"executed, {'m0' if am is m0 else 'm1'}, {i=}")
                locked_count = 0
                if i and i.action == Action.SND:
                    if am is m1:
                        m1_send_count += 1
                    bm.send(am.last_snd_val)
            except Locked:
                swap = True
                locked_count += 1
                if locked_count >= 3:
                    break
            except StopIteration:
                break

        return str(m1_send_count)

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
