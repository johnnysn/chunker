from abc import ABC, abstractmethod
import re
from typing import TypedDict
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter, TokenTextSplitter
from tools.nltk_utilities import chunk_by_tokens, chunk_by_sentences


class Chunk(TypedDict):
    number: int
    text: str


class SplitterDesc(TypedDict):
    id: str
    name: str
    description: str


class Splitter(ABC):
    @abstractmethod
    def split(self, text: str, chunk_size: int, chunk_overlap: int, separator: str) -> list[Chunk]:
        pass

    @abstractmethod
    def desc(self) -> SplitterDesc:
        pass


class SimpleParagraphSplitter(Splitter):
    def desc(self):
        return {
            "id": "paragraphs", "name": "Split by paragraph", 
            "description": "Split text by paragraphs"
        }

    def split(self, text: str, chunk_size: int = 0, chunk_overlap: int = 0, separator: str = r'\n\s*') -> list[Chunk]:
        text_chunks = re.split(separator, text)
        chunks = [
            {
                "number": i + 1,
                "text": text,
            } for i, text in enumerate(text_chunks)
        ]

        return chunks


class LCRecursiveCharSplitter(Splitter):
    def desc(self):
        return {
            "id": "lc_rec_char", 
            "name": "LangChain Rec. Char. Splitter", 
            "description": "Split recursively by characters using langchain"
        }

    def split(self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = "\n\n") -> list[Chunk]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        texts = text_splitter.split_text(text)
        return [
            {
                "number": i + 1,
                "text": text
            } for i, text in enumerate(texts) 
        ]


class LCCharacterSplitter(Splitter):
    def desc(self):
        return {
            "id": "lc_char", 
            "name": "LangChain Character Splitter", 
            "description": "Split by a specific separator using langchain"
        }

    def split(self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = "\n\n") -> list[Chunk]:
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
            separator=separator
        )
        texts = text_splitter.split_text(text)
        return [
            {
                "number": i + 1,
                "text": text
            } for i, text in enumerate(texts) 
        ]
        
        
class LCTokenSplitter(Splitter):
    def desc(self):
        return {
            "id": "lc_token", 
            "name": "LangChain Token Splitter", 
            "description": "Split by tokens using tiktoken tokenizer and langchain token splitter"
        }

    def split(self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = "") -> list[Chunk]:
        text_splitter = TokenTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
        texts = text_splitter.split_text(text)
        return [
            {
                "number": i + 1,
                "text": text
            } for i, text in enumerate(texts) 
        ]


class NltkTokenSplitter(Splitter):
    def desc(self):
        return {
            "id": "nltk_token",
            "name": "NLTK Token Splitter",
            "description": "Split by tokens using NLTK"
        }

    def split(self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = "") -> list[Chunk]:
        texts = chunk_by_tokens(text, chunk_size, chunk_overlap)
        return [
            {
                "number": i + 1,
                "text": text
            } for i, text in enumerate(texts)
        ]


class NltkSentenceSplitter(Splitter):
    def desc(self):
        return {
            "id": "nltk_sentence",
            "name": "NLTK Sentence Splitter",
            "description": "Split by sentences using NLTK"
        }

    def split(self, text: str, chunk_size: int, chunk_overlap: int = 0, separator: str = "") -> list[Chunk]:
        texts = chunk_by_sentences(text, chunk_size, chunk_overlap)
        return [
            {
                "number": i + 1,
                "text": text
            } for i, text in enumerate(texts)
        ]