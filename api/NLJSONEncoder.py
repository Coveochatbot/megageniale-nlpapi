from flask.json import JSONEncoder
from model.intent import Intent
from model.entity import Entity
from model.NLPAnalysis import NLPAnalysis

class NLJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, NLPAnalysis):
            return {
                'intents': obj.intents,
                'entities': obj.entities,
            }
        elif isinstance(obj, Intent):
            return {
                'name': obj.name,
            }
        elif isinstance(obj, Entity):
            return {
                'name': obj.name,
                'confidence': obj.confidence,
            }
        return super(NLJSONEncoder, obj).default(obj)
