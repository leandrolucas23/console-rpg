from core.entitys.player import Player
from system.initialization_system.game_classes import GameClasses
from system.initialization_system.game_localization import GameLocalization
from system.ui_system.fields_system.fields import (
    TextField,
    ChoiceField
)

class CreationStep:
    def execute(self):
        pass

class NameStep(CreationStep):
    def execute(self):

        name_field = TextField(
            ["What is your character's name?"]
        )

        return name_field.get_value()

class ClassStep(CreationStep):
    def execute(self):

        class_options = []
        translated_options = []

        for class_key in GameClasses.get():
            class_data = GameClasses.get(class_key)

            class_options.append(class_key)
            translated_options.append(
                GameLocalization.get(class_data["meta"]["name_key"])
            )

        class_field = ChoiceField(
            "What is your character's class?",
            translated_options
        )

        return  class_options[
            class_field.get_value()
        ]

class AttributesStep(CreationStep):
    def __init__(self, player_class):
        self.player_class = player_class

    def execute(self):

        choised_class = GameClasses.get(self.player_class)

        return choised_class["attributes"]

class CharacterCreation:

    def __init__(self):
        self.data = {}

    def start(self):

        self.data["name"] = NameStep().execute()
        self.data["class"] = ClassStep().execute()
        self.data["attributes"] = AttributesStep(
            self.data["class"]
        ).execute()

        return Player (
                self.data["name"],
                self.data["class"],
                self.data["attributes"]
        )