from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class FileSystemComponent (ABC) :
    @property
    def parent (self) -> FileSystemComponent :
        return self._parent 
    
    @parent.setter
    def parent (self, parent : FileSystemComponent) :
        self._parent = parent
        
    def add (self, parent : FileSystemComponent) -> None :
        pass
    
    def remove (self, parent : FileSystemComponent) -> None :
        pass
    
    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def display(self) -> str :
        pass
    
class File (FileSystemComponent) :
    def __init__(self, name) -> None :
        self.__name = name
    
    def display(self) -> str :
        print(f"file : {self.__name}")
    
class Folder (FileSystemComponent) :
    def __init__(self, name) -> None:
        self.__name = name
        self.__folder = []
    
    # Add component
    def add(self, file) :
        self.__folder.append(file)
        
    # remove component
    def remove (self, file):
        self.components.remove(file)
        
    def display(self):
        print(f"Folder : {self.__name}")
        for file in self.__folder :
            file.display()
    
if __name__ == "__main__" :
    file1 = File("Document.txt")
    file2 = File("Image.jpg")

    file1.display()
    file2.display()
    
    folder1 = Folder("Document")
    folder1.add(file1)
    folder1.add(file2)
    folder1.display()
    
    folder2 = Folder("Pictures")
    folder1.add(folder2)

    
    folder2.display()
    folder2.add(file2)
    folder1.display()