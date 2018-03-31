class NLPAnalysis:
    def __init__(self):
        self.intents = []
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_intent(self, intent):
        self.intents.append(intent)
