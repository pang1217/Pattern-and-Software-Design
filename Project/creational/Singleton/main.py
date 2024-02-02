class Pointer:
    __instance = None
    
    @classmethod
    #  cls ; It stands for "class" and is used to refer to the class itself within the method
    def getInstance(self):
        if self.__instance is None:
            self.__instance = self()
        return self.__instance
    
    def move (self):
        return "Pointer move."
    
    def leftClick (self):
        return "Pointer left click."
    
    def rightClick (self):
        return "Pointer right click."
    
    
if __name__ == "__main__":
    # The client code.
    pointer1 = Pointer()
    pointer2 = Pointer()

    print("===== Pointer 1 =====")    
    print(pointer1.move())
    print(pointer1.leftClick())
    print(pointer1.rightClick())
    
    print("===== Pointer 2 =====")
    print(pointer2.move())
    print(pointer2.leftClick())
    print(pointer2.rightClick())
    
    print('=' * 20)
    if pointer1.getInstance() == pointer2.getInstance():
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")