from system.combat_system.combat_controller import CombatController

class Combat:

    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    @property
    def combatants(self):
        return [self.player, *self.enemies]

    def start(self):
        controller = CombatController(self)

        while True:
            controller.run_round()
