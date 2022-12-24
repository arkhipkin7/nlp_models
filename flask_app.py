import json
import configparser

from model import PipeLine
from flask import Flask, request

CONFIG_FILE: str = 'config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

model_file = config['MODEL']['model_file']
tfidf_file = config['MODEL']['tfidf_file']

app = Flask(__name__)
app.config['DEBUG'] = True

pipeline = PipeLine(
    model_file=model_file,
    tfidf_file=tfidf_file
)
model = pipeline.load_model(model_file)
tfidf = pipeline.load_model(tfidf_file)


@app.route('/predict', methods=['POST'])
def predict():
    args = request.json
    X = pipeline.featurize([args['text']])
    labels = pipeline.predict(X)
    return json.dumps({'predictions': labels})


app.run()
