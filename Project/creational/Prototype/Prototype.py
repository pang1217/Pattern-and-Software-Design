from copy import deepcopy

#  Prototype
class DocumentPrototype:
    def clone(self):
        pass
    
    def display(self):
        pass
    
    
class Resume(DocumentPrototype):
    def __init__ (self, name, experience):
        self.__name = name
        self.__experience = experience
        
    def clone(self) :
        return deepcopy(self)
    
    def setExperience(self, experience) :
        self.__experience = experience
    
    def display(self) :
        print(f"name : {self.__name} experience : {self.__experience} years")
        
class CoverLetter(DocumentPrototype):
    def __init__ (self, name, position) -> None :
        self.__name = name
        self.__position = position
        
    def clone(self) :
        return deepcopy(self)
    
    def setPosition(self, position) :
        self.__position = position
        
    def display(self) :
        print(f"name : {self.__name} experience : {self.__position} ")      

if __name__ == "__main__" :
    prototype = DocumentPrototype()
    
    resume_prototype = Resume("Tony", 3)
    resume1_clone = resume_prototype.clone()
    resume2_clone = resume_prototype.clone()
    resume3_clone = resume_prototype.clone()
    resume4_clone = resume_prototype.clone()
    resume5_clone = resume_prototype.clone()
    
    resume1_clone.setExperience(5)
    
    # display resume
    resume_prototype.display()
    resume1_clone.display() # modify experience
    resume2_clone.display()
    resume3_clone.display()
    resume4_clone.display()
    resume5_clone.display()
    
    print('=' * 20)
    
    coverLetter_prototype = CoverLetter("Jane", "Graphic Design")
    coverLetter_clone = coverLetter_prototype.clone()
    
    # # modify
    # coverLetter_clone.name = "John"
    # coverLetter_clone.position = "Full Stack developer"
    
    # display
    coverLetter_prototype.display()
    coverLetter_clone.display()