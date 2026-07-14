class AttackEvent:
    message_keys = "combat.attack"

    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

class DamageEvent:
    message_keys = "combat.damage"

    def __init__(self, target, amount):
        self.target = target
        self.amount = amount

class SpellEvent:
    message_keys = "combat.spell"

    def __init__(self, caster, target, spell):
        self.caster = caster
        self.target = target or None
        self.spell_name = spell.name

class ShieldAbsorbedEvent:
    message_keys = "combat.shield_absorbed"

    def __init__(self, target, amount):
        self.target = target
        self.amount = amount