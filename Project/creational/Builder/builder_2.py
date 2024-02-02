from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class BookBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    def buildTitle(self) -> None:
        pass
    
    def buildAuthor(self) -> None:
        pass

    def buildISBN(self) -> None:
        pass
    

class FictionBuilder(BookBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Book()

    @property
    def product(self) -> Book:
        product = self._product
        self.reset()
        return product

    def buildTitle(self, title) -> None:
        self._product.add("Title : " + title)
    
    def buildAuthor(self, author) -> None:
        self._product.add("Author : " + author)

    def buildISBN(self, isbn) -> None:
        self._product.add("ISBN : " + isbn)
        
class NonFictionBuilder(BookBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Book()

    @property
    def product(self) -> Book:
        product = self._product
        self.reset()
        return product

    def buildTitle(self, title) -> None:
        self._product.add("Title : " + title)
    
    def buildAuthor(self, author) -> None:
        self._product.add("Author : " + author)

    def buildISBN(self, isbn) -> None:
        self._product.add("ISBN : " + isbn)
        
# Product
class Book:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def getResult(self) :
        for index in range(len(self.parts)):
            print(self.parts[index])

# Editor
class Director:
   def makeBook(self, builder : BookBuilder) : 
       builder.buildTitle("Title")
       builder.buildAuthor("author")
       return builder.product 
   
   def makeBookWithISBN(self, builder : BookBuilder) : 
       builder.buildTitle("Title with ISBN book")
       builder.buildAuthor("author")
       builder.buildISBN("X" * 16)
       return builder.product 

if __name__ == "__main__":
    director = Director()
    
    print(f'{'='*10} Fiction {'='*10}')
    FictionBuilder = FictionBuilder()
    print(f'{'-' * 5} Fiction')
    fiction : Book() = director.makeBook(FictionBuilder)
    fiction.getResult()
    
    print(f'{'-' * 5} Fiction with ISBN')
    fictionWithISBN : Book() = director.makeBookWithISBN(FictionBuilder)
    fictionWithISBN.getResult()
    
    print(f'\n\n{'='*10} Non Fiction {'='*10}')
    NonFictionBuilder = NonFictionBuilder()
    print(f'{'-' * 5} Non Fiction ')
    nonfiction : Book() = director.makeBook(NonFictionBuilder)
    nonfiction.getResult()
    
    print(f'{'-' * 5} Non Fiction  with ISBN')
    nonfictionWithISBN : Book() = director.makeBookWithISBN(NonFictionBuilder)
    nonfictionWithISBN.getResult()
    
    FictionBuilder.buildTitle("Title test")
    