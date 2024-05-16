from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello world, this is Chunker!"


methods = [
  {"id": "characters_count", "name": "Character count split", "description": "Split text by character count"},
  {"id": "sentences", "name": "Sentences split", "description": "Split text by groups of sentences"},
]


@app.route("/methods", methods=['GET'])
def get_methods():
  response = jsonify(methods)
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response


if __name__ == '__main__':
  app.run(debug=True)