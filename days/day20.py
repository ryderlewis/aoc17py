from .day import Day
from dataclasses import dataclass
from collections import namedtuple, defaultdict
import re


Coord = namedtuple('Coord', ('x','y','z'))

@dataclass
class Particle:
    idx: int
    pos: Coord
    vel: Coord
    acc: Coord

    def dist(self) -> int:
        return sum(map(abs, self.pos))

    def accel(self) -> int:
        return sum(map(abs, self.acc))

    def move(self):
        self.vel = Coord(self.vel.x + self.acc.x, self.vel.y + self.acc.y, self.vel.z + self.acc.z)
        self.pos = Coord(self.pos.x + self.vel.x, self.pos.y + self.vel.y, self.pos.z + self.vel.z)


class Day20(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        particles = self.parse()
        particles.sort(key=lambda x: x.accel())
        return str(particles[0].idx)

    def part2(self) -> str:
        particles = self.parse()
        for iteration in range(1000):
            positions = defaultdict(set)
            for i, p in enumerate(particles):
                positions[p.pos].add(i)
            eliminate = set()
            for v in positions.values():
                if len(v) > 1:
                    eliminate.update(v)
            if eliminate:
                print(f"{iteration=}, eliminating {len(eliminate)} particles")
                particles = [q for j, q in enumerate(particles) if j not in eliminate]
            for p in particles:
                p.move()
        return str(len(particles))

    def parse(self) -> list[Particle]:
        ret = []
        for idx, line in enumerate(self.data_lines()):
            m = re.match(r'p=<(\S+)>, v=<(\S+)>, a=<(\S+)>', line)
            p, v, a = m.groups()
            ret.append(Particle(
                idx=idx,
                pos=Coord(*map(int, p.split(','))),
                vel=Coord(*map(int, v.split(','))),
                acc=Coord(*map(int, a.split(','))),
            ))
        return ret
