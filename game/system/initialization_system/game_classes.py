import os
import json

class GameClasses:

    classes = {}

    @classmethod
    def load(cls):
        if cls.classes:
            return

        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            base_path,
            "..",
            "..",
            "data",
            "progression",
            "classes",
            "classes.json"
        )

        with open(file_path) as file:
            cls.classes = json.load(file)

    @classmethod
    def get(cls, class_key=None):

        if class_key:
            return cls.classes[class_key]

        else:
            return cls.classes