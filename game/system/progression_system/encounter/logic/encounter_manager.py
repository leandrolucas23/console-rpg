from core.config.rarity import default_rarity
from system.progression_system.encounter.logic.encounter_amount import EncounterAmount

class EncounterManager:

    def __init__(self, pool, distribution = default_rarity):

        self.pool = pool
        self.distribution = distribution

    def execute(self):

        amount = EncounterAmount.roll_encounter_amount()

        encounters = []

        for _ in range(amount):

            rarity = self.pool.roll_rarity(
                self.distribution
            )

            monster = self.pool.random_by_rarity(rarity)

            encounters.append(monster)

        return encounters