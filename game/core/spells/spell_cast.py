from core.events.action_events import SpellEvent
from core.events.event_management import EventManager

class Spell:
    def __init__(self, name, allowed_class, mana_cost, damage=0, effects=None):
        self.name = name
        self.allowed_class = allowed_class
        self.mana_cost = mana_cost
        self.damage = damage
        self.effects = effects or []

    def cast(self, caster, target):

        validation = self.can_cast(caster)

        if not validation.success:
            return validation

        caster.mp -= self.mana_cost
        self.apply_spell(caster, target)

        return validation

    def can_cast(self, caster):

        result = ActionResult()

        if caster.entity_class not in self.allowed_class:
            result.add_error(
                "action.invalid_class"
            )

        if caster.mp < self.mana_cost:
            result.add_error(
                "action.not_enough_mana"
            )

        return result

    def apply_spell(self, caster, target):

        EventManager.emit(
            SpellEvent(
                caster,
                target,
                self.name
            )
        )

        if self.damage > 0:
            damage = int(
                self.damage *
                (1 + caster.intelligence * 0.05)
            )

            target.receive_damage(damage)

        for effect in self.effects:
            effect.apply(caster, target)

class ActionResult:

    def __init__(self):
        self.success = True
        self.errors = []

    def add_error(self, message):
        self.success = False
        self.errors.append(message)
