import os
import json

class GameMonster:

    monsters = {}

    @classmethod
    def load(cls):
        if cls.monsters:
            return

        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            base_path,
            "..",
            "..",
            "data",
            "entities",
            "monsters.json"
        )

        with open(file_path) as monsters_file:
            cls.monsters = json.load(monsters_file)

    @classmethod
    def get(cls, monster_id=None):
        if not cls.monsters:
            cls.load()

        if monster_id is None:
            return cls.monsters

        return cls.monsters[monster_id]