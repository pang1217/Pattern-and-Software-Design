# Interface
class IPub:
    def order(self, info, age):
        pass

# ProxyPub class
class ProxyPub(IPub):
    def __init__(self, pub):
        self.pub = pub

    def order(self, info, age):
        result = "Promotion! : "
        if age > 20:
            result += "Free 1 alcohol drink\n"
        else:
            result += "Free 1 Juice\n"
        result += self.pub.order(info, age)
        return result

# Pub class
class Pub(IPub):
    def order(self, info, age):
        return f"Hello {info}\nMenu:\n- snack\n- food"

if __name__ == '__main__':
    rPub = Pub()
    print(rPub.order("Alice", 15))

    print()
    pPub = ProxyPub(Pub())
    print(pPub.order("Alice", 45))

    print()
    pPub = ProxyPub(Pub())
    print(pPub.order("Alice", 5))