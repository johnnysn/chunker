from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import time
from splitters import (
    LCCharacterSplitter,
    LCTokenSplitter,
    SimpleParagraphSplitter,
    LCRecursiveCharSplitter,
    NltkTokenSplitter,
    NltkSentenceSplitter,
)
from semantic_splitters import AurelioLabsStatisticalSplitter


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello world, this is Chunker!"


splitters_list = [
    LCRecursiveCharSplitter(),
    LCCharacterSplitter(),
    LCTokenSplitter(),
    SimpleParagraphSplitter(),
    NltkTokenSplitter(),
    NltkSentenceSplitter(),
    AurelioLabsStatisticalSplitter(),
]

splitters = {splitter.desc()["id"]: splitter for splitter in splitters_list}

descriptors = [splitter.desc() for splitter in splitters.values()]


@app.route("/methods", methods=["GET"])
def get_methods():
    return jsonify(descriptors)


@app.route("/chunks/raw", methods=["POST"])
def chunks_raw():
    method_id = request.json["methodId"]
    text = request.json["text"]
    chunk_size = request.json["chunkSize"]
    chunk_overlap = request.json["chunkOverlap"]

    splitter = splitters[method_id]

    # time.sleep(5)

    return jsonify(
        {
            "chunks": splitter.split(
                text=text, chunk_size=chunk_size, chunk_overlap=chunk_overlap
            ),
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
