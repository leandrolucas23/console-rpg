from collections import Counter
from dataclasses import dataclass

from core.config.rarity import default_rarity

from progression_system.encounter.logic.encounter_factory import EncounterFactory
from system.initialization_system.game_monsters import GameMonster
from system.initialization_system.game_localization import GameLocalization


@dataclass
class Monster:
    name: str
    rarity: str

def localize(key: str) -> str:
    return GameLocalization.get(key)


def load_monsters() -> list[Monster]:

    GameMonster.load()
    GameLocalization.load()

    monster = []

    for _, monster_data in GameMonster.get().items():

        monster.append(
            Monster(
                name=localize(
                    monster_data["meta"]["name_key"]
                ),
                rarity=localize(
                    monster_data["meta"]["rarity_key"]
                )
            )
        )

    return monster


def simulate_encounters(
    enemies: list[Monster],
    executions: int = 10000
):

    manager = EncounterFactory.create(enemies)

    rarity_counter = Counter()
    monster_counter = Counter()

    total_monsters = 0

    for _ in range(executions):

        encounters = manager.execute()

        total_monsters += len(encounters)

        for monster in encounters:

            rarity_counter[monster.rarity] += 1

            monster_counter[
                (monster.name, monster.rarity)
            ] += 1

    print()
    print("=" * 60)
    print(f"Simulação: {executions} execuções")
    print("=" * 60)

    print(f"\nTotal de monstros gerados: {total_monsters}")

    print("\nDistribuição por raridade:\n")

    for tier in default_rarity:

        count = rarity_counter[tier.name]

        percentage = (
            count / total_monsters * 100
            if total_monsters
            else 0
        )

        print(
            f"{tier.name:<12} "
            f"-> {count:>8} "
            f"({percentage:>6.2f}%)"
        )

    print("\nMonstros encontrados:\n")

    for (name, rarity), count in sorted(
        monster_counter.items(),
        key=lambda item: item[1],
        reverse=True
    ):

        percentage = count / total_monsters * 100

        print(
            f"{name:<20}"
            f"{rarity:<12}"
            f"-> {count:>8}"
            f" ({percentage:>6.2f}%)"
        )


if __name__ == "__main__":

    monsters = load_monsters()

    simulate_encounters(
        monsters,
        executions=30
    )