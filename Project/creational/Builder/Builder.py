from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class DocumentBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def buildHeader(self) -> None:
        pass

    @abstractmethod
    def buildParagraph(self) -> None:
        pass

    @abstractmethod
    def buildImage(self) -> None:
        pass

class SimpleDocumentBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Document()

    @property
    def product(self) -> Document:
        product = self._product
        self.reset()
        return product

    def buildHeader(self) -> None:
        self._product.add("Simple Header")

    def buildParagraph(self) -> None:
        self._product.add("Simple Paragraph")

    def buildImage(self) -> None:
        self._product.add("Simple Image")
        
class FancyDocumentBuilder(DocumentBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Document()

    @property
    def product(self) -> Document:
        product = self._product
        self.reset()
        return product

    def buildHeader(self) -> None:
        self._product.add("Fancy Header")

    def buildParagraph(self) -> None:
        self._product.add("Fancy Paragraph")

    def buildImage(self) -> None:
        self._product.add("Fancy Image")

class Document:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

# Editor
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> DocumentBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: DocumentBuilder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.buildHeader()

    def build_full_featured_product(self) -> None:
        self.builder.buildHeader()
        self.builder.buildParagraph()
        self.builder.buildImage()

if __name__ == "__main__":
    print('----- Simple Document ----')
    director = Director()
    builder = SimpleDocumentBuilder()
    director.builder = builder
    
    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full-featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.buildHeader()
    builder.buildParagraph()
    builder.product.list_parts()
    
    print("\n\n")
    
    print('----- Fancy Document ----')
    director = Director()
    builder = FancyDocumentBuilder()
    director.builder = builder
    
    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full-featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.buildHeader()
    builder.buildParagraph()
    builder.product.list_parts()
    print("\n")