from system.ui_system.screens_system.screen import Screen
from system.progression_system.encounter.combat_encounter import CombatEncounter
from system.combat_system.combat import Combat
class DirectionPoint:

    def __init__(self, player):
        self.player = player

    def run(self):
        while True:
            self.move(self.choice_destiny())

    def move(self, direction):
        actions = {
            0: self.camping,
            1: self.combat,
            2: self.exit_game
        }

        action = actions.get(direction)

        if action:
            action()

    def camping(self):
        old_hp = self.player.hp
        old_mp = self.player.mp

        self.player.hp = self.player.max_hp
        self.player.mp = self.player.max_mp

        Screen.message([
            f"{old_hp}/{self.player.max_hp} -> {self.player.hp}/{self.player.max_hp}",
            f"{old_mp}/{self.player.max_mp} -> {self.player.mp}/{self.player.max_mp}"
        ])

    def combat(self):
        enemies = CombatEncounter().generate()

        print(self.player.name)

        Combat(self.player, enemies).start()

    @staticmethod
    def exit_game():
        raise SystemExit

    @staticmethod
    def choice_destiny():
        return Screen.menu(
            "system.ui.question.move",
            options=[
                "camping",
                "combat",
                "exit"
            ]
        )