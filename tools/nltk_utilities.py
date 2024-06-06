from nltk.tokenize import sent_tokenize, word_tokenize


def chunk_by_tokens(text, max_words_per_chunk=100, language="english"):
    sentences = sent_tokenize(text, language=language)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        words = word_tokenize(sentence, language=language)

        if len(current_chunk) + len(words) <= max_words_per_chunk:
            current_chunk.extend(words)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = words

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    overlapping_chunks = []
    for i in range(len(chunks)):
        chunk_start = max(0, i - 1)
        chunk_end = i + 1
        overlapping_chunk = ' '.join(chunks[chunk_start:chunk_end])
        overlapping_chunks.append(overlapping_chunk)

    return overlapping_chunks


def chunk_by_sentences(source_text: str, sentences_per_chunk: int, overlap: int, language="english") -> list[str]:
    if sentences_per_chunk < 2:
        raise ValueError("The number of sentences per chunk must be 2 or more.")
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
