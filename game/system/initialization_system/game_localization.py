import os
import json

class GameLocalization:

    texts: dict[str, str] = {}

    @classmethod
    def load(cls, language="pt_br"):
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, "..", "..", "data", "lang", f"{language}.json")

        with open(file_path, encoding="utf-8") as file:
            cls.texts = json.load(file)

    @classmethod
    def get(cls, key: str, **kwargs) -> str:
        text = cls.texts.get(key, key)

        if kwargs:
            return text.format(**kwargs)

        return text

    @classmethod
    def translate(cls, content, **kwargs):
        if isinstance(content, str):
            return cls.get(content, **kwargs)

        return [cls.get(text) for text in content]