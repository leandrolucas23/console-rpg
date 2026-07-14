from system.message_system.messages import MessageFormatter
from system.initialization_system.game_localization import GameLocalization

class MessageManager:

    @classmethod
    def manage(cls, event):

        params = MessageFormatter.format_event(event)

        template = GameLocalization.translate(
            event.message_keys
        )

        return template.format(**params)