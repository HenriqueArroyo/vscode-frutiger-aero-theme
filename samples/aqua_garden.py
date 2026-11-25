"""Jardim aquático de exemplo para conferir as cores em Python."""

from dataclasses import dataclass, field
import re

WATER_LEVEL = 0.62
LEAF = re.compile(r"^leaf-(\d+)$")


@dataclass
class Plant:
    name: str
    height_cm: float = 12.5
    tags: list[str] = field(default_factory=list)

    def grow(self, sunlight: float, *, boost: bool = False) -> float:
        rate = 1.4 if boost else 1.0
        self.height_cm += sunlight * rate * WATER_LEVEL
        return self.height_cm


def bloom(plants: list[Plant]) -> dict[str, float]:
    return {p.name: round(p.height_cm, 1) for p in plants if p.height_cm > 10}


if __name__ == "__main__":
    lotus = Plant("lotus", tags=["aqua", "glossy"])
    print(f"{lotus.name} -> {lotus.grow(3.2, boost=True):.2f} cm")
    print(bloom([lotus]), True, None)
