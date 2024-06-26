from splitters import Chunk, Splitter
from semantic_chunkers import StatisticalChunker
from semantic_router.encoders import HuggingFaceEncoder


class AurelioLabsStatisticalSplitter(Splitter):
    def desc(self):
        return {
            "id": "aulabs_statistical",
            "name": "Aurelio Labs statistical chunker",
            "description": "Split using statistical semantic chunker from Aurelio Labs.",
        }

    def split(
        self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = ""
    ) -> list[Chunk]:
        chunker = StatisticalChunker(
            encoder=HuggingFaceEncoder(), max_split_tokens=chunk_size
        )
        texts = []

        chunks = chunker(docs=[text])[0]
        if not chunks:
            return []

        for chunk in chunks:
            text = ""
            for split in chunk.splits:
                text += split + "\n"

            texts.append(text)

        return [{"number": i + 1, "text": text} for i, text in enumerate(texts)]
