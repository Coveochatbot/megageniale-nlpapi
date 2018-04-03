from flask import Flask,jsonify, json, request
from model.intent import Intent
from model.entity import Entity
from model.NLPAnalysis import NLPAnalysis
from NLPJSONEncoder import NLPJSONEncoder
from dialogflow_service import DialogFlowService
app = Flask(__name__)
app.json_encoder = NLPJSONEncoder
dialogflowservice = DialogFlowService()


@app.route('/NLP/Analyse',  methods=['POST'])
def hello_world():
    content = request.get_json()
    nlp_analysis = NLPAnalysis()
    intent = dialogflowservice.detect_intent(content['sentence'])
    entity = Entity("test")
    nlp_analysis.add_entity(entity)
    nlp_analysis.add_intent(intent)
    return jsonify(nlp_analysis)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
