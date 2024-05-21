from abc import ABC, abstractmethod
import re


class Method(ABC):
    @abstractmethod
    def split(self, text: str, chunk_size: int) -> list[dict]:
        pass


class SimpleParagraphMethod(Method):
    def split(self, text: str, chunk_size: int) -> list[dict]:
        text_chunks = re.split(r'\n\s*', text)
        chunks = [
            {
                "number": i + 1,
                "text": text,
            } for i, text in enumerate(text_chunks)
        ]

        return chunks

