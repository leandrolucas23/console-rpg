from core.config.rarity import default_rarity
from system.random_system.rarity_distribuition import RarityDistribution
from system.progression_system.encounter.logic.encounter_pool import EncounterPool
from system.progression_system.encounter.logic.encounter_manager import EncounterManager


class EncounterFactory:

    @staticmethod
    def create(monsters):

        pool = EncounterPool(monsters)

        distribution = RarityDistribution(
            default_rarity
        )

        return EncounterManager(
            pool,
            distribution
        )
