# Chunker

This is a Python API powered by Flask which should be seen as a template for testing your own text chunking methods for *retrieval augmented generation* (RAG) applications.

## Installation and execution

We recommend creating a virtual environment for running this project:

```bash
python -m venv venv
./venv/bin/activate
```

Now you can upgrade pip:

```bash
python -m pip install --upgrade pip
```

and install the project dependencies:
```bash
python -m pip install -r requirements.txt
```

Once you've created the python script for your application (``app.py``), run it by executing:

```bash
python -m flask --app ./app.py run
```

### NLKT

In order to use the NLTK library you should run the following python commands in your environment:

```python3
import nltk
nltk.download('punkt')
```