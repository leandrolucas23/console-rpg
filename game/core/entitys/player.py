from core.entitys.entity import Entity

class Player(Entity):
    def __init__(self, name, entity_class, attributes):
        super().__init__(name, attributes)

        self.player_class = entity_class
        self.spells = []

        self.xp = 0
        self.level = 1
        self.inventory = []

    def learn_spells(self, all_spells):
        self.spells = [
            spell for spell in all_spells
            if self.player_class in spell.allowed_class
        ]