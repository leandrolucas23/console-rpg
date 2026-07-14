from core.events.event_management import EventManager
from core.events.action_events import (
    DamageEvent,
    ShieldAbsorbedEvent
)

class Entity:
    def __init__(self, name, attributes):
        self.name = name

        self.hp = attributes["hp"]
        self.max_hp = attributes["hp"]
        self.mp = attributes["mp"]
        self.max_mp = attributes["mp"]

        self.strength = attributes["str"]
        self.dexterity = attributes["dex"]
        self.constitution = attributes["con"]
        self.intelligence = attributes["int"]
        self.wisdom = attributes["wis"]
        self.charisma = attributes["cha"]

        self.shield = 0
        self.status_effects = []

    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, damage):

        if self.shield > 0:
            absorbed = min(self.shield, damage)

            self.shield -= absorbed
            damage -= absorbed

            EventManager.emit(
                ShieldAbsorbedEvent(
                    self.name,
                    absorbed,
                )
            )

        if damage > 0:
            self.hp = max(0, self.hp - damage)

            EventManager.emit(
                DamageEvent(
                    self.name,
                    damage,
                )
            )

    def process_status_effects(self):
        messages = []

        for effect in self.status_effects[:]:
            messages.extend(effect.on_turn_start(self))

            if effect.duration <= 0:
                self.status_effects.remove(effect)
                messages.append("O efeito acabou.")

        return messages
