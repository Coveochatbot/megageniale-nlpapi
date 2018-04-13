from flask import Flask,jsonify, request
from api.NLPJSONEncoder import NLPJSONEncoder
from api.dialogflow_service import DialogFlowService
from api.logger.logger_factory import LoggerFactory
app = Flask(__name__)
app.json_encoder = NLPJSONEncoder
dialogflowservice = DialogFlowService()


@app.route('/NLP/Analyze',  methods=['POST'])
def nlp_analyze():
    content = request.get_json()
    nlp_analysis = dialogflowservice.analyse_sentence(content['sentence'])
    return jsonify(nlp_analysis)


if __name__ == '__main__':
    LoggerFactory.get_logger(__name__).info("API started")
    app.run(host='0.0.0.0')
