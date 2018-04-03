import os
import uuid
import dialogflow
from model.intent import Intent
from config import config
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.get('dialogflow_secret')


class DialogFlowService:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.project_id = config.get('project_id')
        self.parent = 'projects/{}/agent'.format(self.project_id)

    def detect_intent(self, text):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)
        text_input = dialogflow.types.TextInput(text=text, language_code=config.get('language'))
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return Intent(response.query_result.intent.display_name, response.query_result.intent_detection_confidence)
