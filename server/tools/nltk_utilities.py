from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import nltk


def chunk_by_tokens(text, max_words_per_chunk=100, overlap = 0, language="english"):
    soup = BeautifulSoup(text)
    tokens = nltk.word_tokenize(soup.get_text(), language=language)

    chunks = []

    print(tokens)

    current_chunk = []
    for i in range(len(tokens)):
        if len(current_chunk) > max_words_per_chunk:
            chunks.append(' '.join(current_chunk))
            if i > 0 and overlap > 0:
                current_chunk = current_chunk[-min(i, overlap):]
            else:
                current_chunk = []

        current_chunk.append(tokens[i])

    if len(current_chunk) > overlap:
        chunks.append(' '.join(current_chunk))

    return chunks


def chunk_by_sentences(source_text: str, sentences_per_chunk: int, overlap: int, language="english") -> list[str]:
    if sentences_per_chunk < 1:
        raise ValueError("The number of sentences per chunk must be 1 or more.")
    if overlap < 0 or overlap >= sentences_per_chunk - 1:
        raise ValueError("Overlap must be 0 or more and less than the number of sentences per chunk.")

    sentences = sent_tokenize(source_text, language=language)
    if not sentences:
        return []

    chunks = []
    i = 0
    while i < len(sentences):
        end = min(i + sentences_per_chunk, len(sentences))
        chunk = ' '.join(sentences[i:end])

        if overlap > 0 and i > 1:
            overlap_start = max(0, i - overlap)
            overlap_end = i
            overlap_chunk = ' '.join(sentences[overlap_start:overlap_end])
            chunk = overlap_chunk + ' ' + chunk

        chunks.append(chunk.strip())
        i += sentences_per_chunk

    return chunks
