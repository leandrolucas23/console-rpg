import random

class WeightedPicker:

    @staticmethod
    def choose(weights: dict[str, float]):

        r = random.random()

        cumulative = 0

        for key, weight in weights.items():

            cumulative += weight

            if r <= cumulative:
                return key

        raise ValueError(
            "Weights must sum to at least 1.0"
        )