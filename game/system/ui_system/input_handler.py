class InputHandler:
    def __init__(self, message=""):
        self.message = message or []

    def entry(self):
        prompt = "┃ ➤ "

        if self.message:
            prompt = f"┃ ({self.message}) ➤ "

        x = "_".join(input(prompt).lower().split())

        if x.isnumeric():
            return int(x)

        else:
             return x