from system.initialization_system.game_localization import GameLocalization
from system.initialization_system.game_classes import GameClasses
from system.initialization_system.game_monsters import GameMonster

class LoadGameContent:

    load_steps = [
        GameLocalization().load,
        GameClasses().load,
        GameMonster().load,
    ]

    @classmethod
    def start(cls):
        for step in cls.load_steps:
            step()

LoadGameContent().start()

classes = GameMonster.get()
