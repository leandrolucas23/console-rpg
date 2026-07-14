from system.ui_system.screens_system.screen import Screen

class TextField:
    def __init__(self, label):
        self.label = label

    def get_value(self):
        return Screen.text(
            self.label
        )

        #return InputHandler(self.label).entry()

class ChoiceField:
    def __init__(self, label, options):
        self.label = label
        self.options = options

    def get_value(self):
        return Screen.menu(
            [self.label], self.options
        )