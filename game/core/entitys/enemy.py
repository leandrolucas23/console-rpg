from core.entitys.entity import Entity

class Enemy(Entity):
    def __init__(self, name, description, category, attributes):
        super().__init__(name, attributes)

        self.description = description
        self.category = category
