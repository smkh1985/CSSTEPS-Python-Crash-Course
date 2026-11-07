from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    
p = Point(1, 2)
print(p)
p.x = 10
