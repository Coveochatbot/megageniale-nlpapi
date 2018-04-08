import os
import uuid
import dialogflow
from model.intent import Intent
from model.entity import Entity
from config import config
from model.NLPAnalysis import NLPAnalysis
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.get('dialogflow_secret')


class DialogFlowService:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.project_id = config.get('project_id')
        self.parent = 'projects/{}/agent'.format(self.project_id)

    def analyse_sentence(self, sentence):
        nlp_analysis = NLPAnalysis()
        query_result = self.detect_intent(sentence)
        nlp_analysis.add_intent(self.retrieve_intent(query_result))
        self.retrieve_entities(nlp_analysis, query_result)
        return nlp_analysis

    def detect_intent(self, sentence):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)
        text_input = dialogflow.types.TextInput(text=sentence, language_code=config.get('language'))
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result

    def retrieve_intent(self, query_result):
        return Intent(query_result.intent.display_name, query_result.intent_detection_confidence)

    def retrieve_entities(self, nlp_analysis, query_result):
        for i, entity in query_result.parameters.items():
            nlp_analysis.add_entity(Entity(entity))


