from core.events.event_management import EventManager
from system.message_system.message_management import MessageManager
from system.ui_system.screens_system.frames import (
    BasicFrame,
    TextFrame
)

def charge_content():

    events = EventManager.consume()

    messages = []

    for event in events:
        messages.append(
            MessageManager.manage(event)
        )

    return messages

class Screen:

    @staticmethod
    def menu(message=None, options=None, input_message=None):
        messages = []

        if message:
            if isinstance(message, str):
                messages.append(message)
            else:
                messages.extend(message)

        messages.extend(charge_content())

        return BasicFrame(
            messages,
            options,
            input_message
        ).show()

    @staticmethod
    def message(message=None):

        messages = message or []

        if isinstance(message, str):
            messages = [message]

        messages.extend(charge_content())

        return BasicFrame(messages).show()

    @staticmethod
    def text(messages=None, input_message=None):
        messages = messages or []

        return TextFrame(
            messages,
            input_message
        ).show()