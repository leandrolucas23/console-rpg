from system.random_system.weighted_picker import WeightedPicker
import random

class EncounterPool:

    def __init__(self, monsters):
        self.monsters = monsters

    def available_rarities(self):

        return {
            monster.rarity
            for monster in self.monsters
        }

    def get_by_rarity(self, rarity):

        return [
            monster
            for monster in self.monsters
            if monster.rarity == rarity
        ]


    def random_by_rarity(self, rarity):

        candidates = self.get_by_rarity(rarity)

        return random.choice(candidates)

    def roll_rarity(self, distribution, luck=0):

        probabilities = distribution.probabilities(luck)
        available_rarities = self.available_rarities()

        available_probabilities = {}

        for rarity_name, probability in probabilities.items():

            if rarity_name in available_rarities:

                available_probabilities[rarity_name] = probability

        total_probability = 0

        for probability in available_probabilities.values():

            total_probability += probability

        normalized_probabilities = {}

        for rarity_name, probability in available_probabilities.items():

            normalized_probabilities[rarity_name] = (
                probability / total_probability
            )

        return WeightedPicker.choose(normalized_probabilities)