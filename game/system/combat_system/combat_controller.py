from system.ui_system.screens_system.screen import Screen
from system.initialization_system.game_localization import GameLocalization
from core.events.event_management import EventManager
from core.events.action_events import AttackEvent
from core.events.ui_events import AttackQuestionEvent

class CombatController:
    def __init__(self, combat):
        self.combat = combat

    def run_round(self):

        for actor in self.combat.combatants:

            target = self.choose_target(actor)

            EventManager.emit(
                AttackEvent(actor, target)
            )

    def choose_target(self, actor):

        if actor == self.combat.player:

            translated_options = GameLocalization.translate(
                enemy.name for enemy in self.combat.enemies
            )

            EventManager.emit(
                AttackQuestionEvent
            )
            choice = Screen.menu(
                options=translated_options
            )

            return self.combat.enemies[choice]

        else:
            return self.combat.player

