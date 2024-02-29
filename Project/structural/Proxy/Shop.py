# Interface
class IShop:
    def shipping(self, price):
        pass

# ProxyShop class
class ProxyShop(IShop):
    def __init__(self, shop):
        self.shop = shop

    def shipping(self, price):
        result = self.shop.shipping(price)
        result += "Shipping Fee = "
        if price > 1500:
            result += f"Free Shipping!\nTotal Price : {price}"
        else:
            result += f"100\nTotal Price : {price + 100}"
        return result

# Shop class
class Shop(IShop):
    def shipping(self, price):
        return f"Price : {price}\n"

if __name__ == '__main__':
    rShop = Shop()
    print(rShop.shipping(100))

    print()
    pShop = ProxyShop(Shop())
    print(pShop.shipping(100))

    print()
    print(pShop.shipping(1600))