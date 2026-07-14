class EventManager:
    events = []

    @classmethod
    def emit(cls, event):
        cls.events.append(event)

    @classmethod
    def consume(cls):
        events = cls.events.copy()
        cls.events.clear()
        return events
    