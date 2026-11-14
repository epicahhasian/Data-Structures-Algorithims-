class People():
    def __init__(self,value):
        self.y = []
        self.value = value 

    def sizecheck(self):
        return len(self.y)

    def add (self,person):
        if self.sizecheck()< self.value: 
            self.y.append(person)
        else:
            print("Queue is full")

    def remove(self):
        if self.sizecheck() == 0:
            print ("Queue is empty")
        else:
            self.y.pop(0)

    def showqueue(self):
        print (self.y)



abaan= People(5)

abaan.add(2)
abaan.showqueue()
abaan.add(3)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add (4)
abaan.showqueue()
abaan.remove()
abaan.showqueue()
abaan.remove()
abaan.showqueue()
abaan.remove()
abaan.showqueue()
abaan.remove()
abaan.showqueue()
abaan.remove()
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()
abaan.add(1)
abaan.showqueue()



    