class Computer:
    def __init__(self, __maxprice):
        self.__maxprice = __maxprice

    def sell(self):
        print("Selling price is: {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

    def getMaxprice(self):
        return self.__maxprice

x = int(input("Enter the price: "))
y = int(input("Enter the changed price: "))
c = Computer(x)
c.sell()
#print(c.__maxprice)
print(c.getMaxprice())
c.setMaxprice(y)
c.sell()