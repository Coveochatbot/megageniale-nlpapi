from flask import Flask,jsonify
from model.intent import Intent
from model.entity import Entity
from model.NLPAnalysis import NLPAnalysis
from NLPJSONEncoder import NLPJSONEncoder

app = Flask(__name__)
app.json_encoder = NLPJSONEncoder


@app.route('/')
def hello_world():
    nlp_analysis = NLPAnalysis()
    intent = Intent("test", 2)
    entity = Entity("test")
    nlp_analysis.add_entity(entity)
    nlp_analysis.add_intent(intent)
    return jsonify(nlp_analysis)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
