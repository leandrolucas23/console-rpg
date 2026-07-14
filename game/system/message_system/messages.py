from system.initialization_system.game_localization import GameLocalization
from core.entitys.entity import Entity

class Messages:

    def __init__(self, event):
        self.event = event

    def build(self, key):
        template = GameLocalization.get(key)

        return template.format(
            **vars(self.event)
        )

class MessageFormatter:

    @staticmethod
    def format_value(value):

        if isinstance(value, Entity):
            return GameLocalization.translate(value.name)

        return value

    @classmethod
    def format_event(cls, event):

        return {
            key: cls.format_value(value)
            for key, value in vars(event).items()
        }