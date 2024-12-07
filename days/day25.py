from .day import Day
from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    write: int
    move: int
    state: str


@dataclass(frozen=True)
class State:
    name: str
    action_0: Action
    action_1: Action


class Day25(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        begin, diag, states = self.parse()

        state = states[begin]
        tape: set[int] = set()
        pos = 0
        for _ in range(diag):
            if pos in tape:
                action = state.action_1
            else:
                action = state.action_0

            if action.write:
                tape.add(pos)
            else:
                tape.discard(pos)

            pos += action.move
            state = states[action.state]

        return str(len(tape))

    def part2(self) -> str:
        return "dayXX 2"

    def parse(self) -> tuple[str, int, dict[str, State]]:
        states: dict[str, State] = {}
        begin: str = ""
        diag: int = 0
        lines = self.data_lines()

        i = 0
        while i < len(lines):
            line = lines[i]
            i += 1

            if line.startswith("Begin in state"):
                begin = line.rstrip('.')[-1]
            elif line.startswith("Perform a diagnostic checksum after"):
                words = line.split()
                diag = int(words[-2])
            elif line.startswith("In state"):
                state = line.rstrip(':').split()[-1]
                write_0 = int(lines[i+1].rstrip('.').split()[-1])
                move_0 = 1 if 'right' in lines[i+2] else -1
                state_0 = lines[i+3].rstrip('.').split()[-1]
                i += 4
                write_1 = int(lines[i+1].rstrip('.').split()[-1])
                move_1 = 1 if 'right' in lines[i+2] else -1
                state_1 = lines[i+3].rstrip('.').split()[-1]
                i += 4
                states[state] = State(
                    name=state,
                    action_0=Action(write_0, move_0, state_0),
                    action_1=Action(write_1, move_1, state_1),
                )

        return begin, diag, states