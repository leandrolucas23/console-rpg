from core.entitys.enemy import Enemy
from system.initialization_system.game_monsters import GameMonster

class CreateEnimie:

    @staticmethod
    def mont(enimie_id):

        enimie = GameMonster.get(enimie_id)

        return Enemy(
            enimie["meta"]["name_key"],
            enimie["meta"]["description_key"],
            enimie["meta"]["category_key"],
            enimie["base_attributes"]
        )