from flask import Flask, request, jsonify
from getCompoundWordList import generateCompoundWordList
from flask_cors import CORS
import logging

# Configure the logging
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return "Hello, Flask API!"

@app.route('/generate')
def generate():
    length = int(request.args.get('length'))
    starting_word = request.args.get('startingWord')

    generated_text = generateCompoundWordList(starting_word, length)
    logger.info(f"Returned Compound Words: {generated_text}")
    logger.info(f"Jsonify Compound Words: {jsonify({'compoundWords': generated_text})}")
 #   return jsonify({'compoundWords': generated_text})
    return generated_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)