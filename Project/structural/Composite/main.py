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
        
    def addComponent (self, parent : FileSystemComponent) -> None :
        pass
    
    def removeComponent (self, parent : FileSystemComponent) -> None :
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
        self.__folder : List[FileSystemComponent] = []
    
    # Add component
    def addComponent(self, component) :
        self.__folder.append(component)
        
    # remove component
    def removeComponent (self, component):
        self.__folder.remove(component)
        
    def is_composite(self) -> bool:
        return True
    
    def display(self):
        print(f"Folder : {self.__name}")
        for file in self.__folder :
            file.display()
    
def client1 (fileComponent : FileSystemComponent) :
    fileComponent.display()
    
def client2 (f1 : FileSystemComponent, f2 : FileSystemComponent) :
    if f1.is_composite() :
        f1.addComponent(f2)
    f1.display()
    
if __name__ == "__main__" :
    file_swift1 = File("TheBasics.swift")
    client1(file_swift1)
    
    folder1 = Folder("Swift_HomeWork")
    
    folder2 = Folder("textFiles")
    file_text2 = File("Collection_Types.txt")
    file_text3 = File("Functions.txt")
    file_text4 = File("Closures.txt")
    #  add files to folder
    folder2.addComponent(file_text2)
    folder2.addComponent(file_text3)
    folder2.addComponent(file_text4)
    
    folder3 = Folder("swift_files")
    file_swift2 = File("Collection_Types.txt")
    file_swift3 = File("Functions.txt")
    folder3.addComponent(file_swift2)
    folder3.addComponent(file_swift3)
    
    file_swift4 = File("Closures.txt")
    
    print('-' * 50)
    client1(folder3)
    print('-' * 50)
    client2(folder3, file_swift1)
    print('-' * 50)
    client2(folder1, folder2)
    print('-' * 50)
    client2(folder1, folder3)
    
    print("+" * 20)
    floder9 = Folder("Floder 9")
    floder9.addComponent(file_swift1)
    floder8 = Folder("Floder 8")
    floder8.addComponent(file_swift2)
    floder7 = Folder("Floder 7")
    floder7.addComponent(file_swift3)
    
    floder9.addComponent(floder8)
    # print("+" * 20)
    floder8.addComponent(floder7)
    print("+" * 20)
    client1(floder9)
    
    print("+" * 20)
    client1(floder8)
    
    
    