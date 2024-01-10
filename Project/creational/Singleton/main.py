class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Pointer(metaclass = SingletonMeta):
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
    if id(pointer1) == id(pointer2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")