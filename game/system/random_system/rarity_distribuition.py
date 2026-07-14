from dataclasses import dataclass
from math import exp

@dataclass
class RarityTier:
    name: str
    weight: float

class RarityDistribution:

    def __init__(self, tiers: list[RarityTier]):
        self._tiers = tuple(tiers)

    def probabilities(self, luck: float = 0.0) -> dict[str, float]:

        luck = max(-100, min(100, luck))

        pivot = (len(self._tiers) - 1) / 2
        strength = luck / 100

        adjusted = []

        for rank, tier in enumerate(self._tiers):

            multiplier = exp((rank - pivot) * strength)

            adjusted.append(tier.weight * multiplier)

        total = sum(adjusted)

        return {
            tier.name: weight / total
            for tier, weight in zip(self._tiers, adjusted)
        }