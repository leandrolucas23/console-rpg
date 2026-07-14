from system.ui_system.renderer import Renderer, Window
from system.ui_system.input_handler import InputHandler
from os import system

def clear():
    system("clear||cls")

def format_options(options=None):
    if options:
        options = [
                f"({i}) {op}"
                for i, op in enumerate(options, start=1)
            ]
    else:
        options = []

    return options

class BasicFrame:
    def __init__(
        self,
        messages=None,
        options=None,
        input_message=None
    ):
        self.messages = messages or []
        self.options = format_options(options)
        self.input_message = input_message

        self.window_height = len(self.messages) + 2
        self.options_height = len(self.options) + 2
        self.interest_height = (self.options_height + self.window_height)

        self.renderer = Renderer(
            60, min((self.interest_height + 2), 22)
        )

    def show(self):
        self.render()
        return self.get_input()

    def render(self):
        clear()

        self.renderer.add(
            Window(
                0, 0,
                60, min(self.window_height, 10),
                "Menu",
                self.messages
            )
        )

        if self.options:
            self.renderer.add(
                Window(
                    0, min(self.window_height, 10),
                    60,
                    min(len(self.options)+2, 10),
                    "Options",
                    self.options
                )
            )

        self.renderer.render()

    def get_input(self):

        if self.input_message:
            return InputHandler(self.input_message).entry()

        elif self.options:
            return int(InputHandler().entry() - 1)

        return InputHandler(
            "press any key to continue."
        ).entry()

class TextFrame:
    def __init__(
        self,
        messages=None,
        input_message=None
    ):
        self.messages = messages or []
        self.input_message = input_message

        self.interest_height = len(self.messages) + 2

        self.renderer = Renderer(
            60, self.interest_height + 2,
        )


    def show(self):
        self.render()
        return InputHandler(
            self.input_message
        ).entry()

    def render(self):
        clear()

        self.renderer.add(
            Window(
                0, 0,
                60, self.interest_height,
                "Menu",
                self.messages
            )
        )

        self.renderer.render()

class CombatFrame:
    def __init__(
        self,
        player,
        enemys,
        messages=None,
        options=None,
        input_message=None,
    ):
        self.player = player
        self.enemys = enemys

        self.messages = messages or []
        self.options = format_options(options)
        self.input_message = input_message

        self.window_height = len(self.messages) + 2
        self.options_height = len(self.options) + 2
        self.interest_height = (self.options_height + self.window_height)

        self.renderer = Renderer(
            120, min((self.interest_height + 2), 22)
        )

