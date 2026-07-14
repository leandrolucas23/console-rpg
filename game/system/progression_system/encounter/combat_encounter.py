from dataclasses import dataclass
from system.initialization_system.game_localization import GameLocalization
from system.initialization_system.game_monsters import GameMonster
from system.entity_system.enimie_system.create_enimie import CreateEnimie
from system.progression_system.encounter.logic.encounter_factory import EncounterFactory

@dataclass
class Monster:
    id: str
    name: str
    rarity: str

def localize(key: str) -> str:
    return GameLocalization.get(key)

def load_monsters() -> list[Monster]:

    monster = []

    for monster_id, monster_data in GameMonster.get().items():

        monster.append(
            Monster(
                id=monster_id,
                name=localize(
                    monster_data["meta"]["name_key"]
                ),
                rarity=localize(
                    monster_data["meta"]["rarity_key"]
                )
            )
        )

    return monster

class CombatEncounter:

    def __init__(self):
        self.monsters = load_monsters()

    def generate(self) -> list[Monster]:

        manager = EncounterFactory.create(self.monsters)

        content = []

        for k in manager.execute():

            content.append(
                CreateEnimie.mont(k.id)
            )

        return content