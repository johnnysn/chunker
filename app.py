from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from splitters import SimpleParagraphMethod

# import time


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello world, this is Chunker!"


methods = [
    {"id": "paragraphs", "name": "Split by paragraph", "description": "Split text by paragraphs"},
    {"id": "characters_count", "name": "Character count split", "description": "Split text by character count"},
    {"id": "sentences", "name": "Sentences split", "description": "Split text by groups of sentences"},
]

splitters = {
    "paragraphs": SimpleParagraphMethod()
}


@app.route("/methods", methods=['GET'])
def get_methods():
    return jsonify(methods)


@app.route("/chunks/raw", methods=['POST'])
def chunks_raw():
    method_id = request.json['methodId']
    text = request.json['text']
    chunk_size = request.json['chunkSize']

    splitter = splitters[method_id]

    # time.sleep(5)
    return jsonify({
        "chunks": splitter.split(text, chunk_size),
    })


if __name__ == '__main__':
    app.run(debug=True)
