class Animal: 
    def __init__ (self, movement, favfood, predator, domestic):
        self.movement = movement 
        self.favfood = favfood 
        self.predator = predator 
        self.domestic = domestic 

    def getmovement (self):
        return self.movement

    def setmovement(self,newvalue):
        self.movement = newvalue 

    def display(self):
        print ("I am an animal whose main movement is " +self.movement + "  ,my favourite food is " + self.favfood+  "i am scared of " +self.predator+ " and am i domestic? " +self.domestic )



class Monkey(Animal):
    def __init__(self,movement,favfood,predator,domestic,sound):
        Animal.__init__(self,movement,favfood,predator,domestic)
        self.sound = sound 

    def display(self):
        print("I am a monkey and my main movement is "+self.movement+ " ,my favourite food is " +self.favfood+ " and I make a "  +self.sound+  " sound. " + " i am scared of "  +self.predator+  " and am i domestic? " +self.domestic )


monkey = Monkey("swinging","banana","tigers","sometimes","OO OO AA AA")

print(monkey.getmovement())
print(monkey.display())