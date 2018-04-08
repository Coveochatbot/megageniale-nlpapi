from flask import Flask,jsonify, request
from NLPJSONEncoder import NLPJSONEncoder
from dialogflow_service import DialogFlowService
app = Flask(__name__)
app.json_encoder = NLPJSONEncoder
dialogflowservice = DialogFlowService()


@app.route('/NLP/Analyse',  methods=['POST'])
def hello_world():
    content = request.get_json()
    nlp_analysis = dialogflowservice.analyse_sentence(content['sentence'])
    return jsonify(nlp_analysis)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
