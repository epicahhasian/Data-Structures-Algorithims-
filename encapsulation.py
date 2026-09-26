class House:
    __address = "8yjt87n3"
    def __init__ (self, association, price, location):
        self.association = association
        self.price = price 
        self.location = location 

    def getaddress(self):
        return self.__address

    def setaddress(self,newaddress):
        self.__address = newaddress 
        print(self.__address)


house1 = House("abaanhouse","456,000,000,000,000,000,000,000,000,000,000,000,000,000,000", "quiet")


print(house1.getaddress())
print(house1.setaddress("9euhy03"))