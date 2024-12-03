from typing import Optional

from .day import Day
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Optional["Node"] = None


class Day17(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        fwd = int(self.data_lines()[0])
        arr = [0]
        pos = 0
        for i in range(1, 2018):
            pos += fwd
            pos %= len(arr)
            pos += 1
            arr[pos:pos] = [i]
        return str(arr[(pos+1)%len(arr)])

    def part2(self) -> str:
        fwd = int(self.data_lines()[0])
        after_zero = 0
        pos = 0
        size = 1
        for i in range(1, 50_000_001):
            pos += fwd
            pos %= size
            if pos == 0:
                after_zero = i
            pos += 1
            size += 1
        return str(after_zero)

    def part2_slow(self) -> str:
        fwd = int(self.data_lines()[0])
        curr = Node(val=0)
        zero = curr
        curr.next = curr
        for i in range(1, 50_000_001):
            if i % 1_000_000 == 0:
                print(i)
            for _ in range(fwd):
                curr = curr.next
            new_node = Node(val=i, next=curr.next)
            curr.next = new_node
            curr = new_node
        return str(zero.next.val)