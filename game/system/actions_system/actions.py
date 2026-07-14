from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self, actor):
        self.actor = actor

    @abstractmethod
    def execute(self, target):
        pass

class AttackAction(Action):
    def execute(self, target):
        damage = self.actor.strength
        target.receive_damage(damage)

class SpellAction(Action):
    def __init__(self,actor, spell):
        super().__init__(actor)
        self.spell = spell

    def execute(self, target):
        self.spell.cast( self.actor, target)