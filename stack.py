class Books ():
    def __init__(self,value):
        self.x = [] 
        self.value = value 

    def size(self):
        return len (self.x)

    def push(self,elements):
        if self.size() < self.value: 
            self.x.append(elements)
        else:
            print ("Stack is full")

    def remove(self):
        if self.size() == 0: 
            print ("Stack is empty")
        else: 
            self.x.pop(-1)

    def display(self):
        print(self.x)


mathsbook = Books(4)
mathsbook.display() 
mathsbook.push(2)
mathsbook.display()
mathsbook.remove()
mathsbook.display()
mathsbook.push(4)
mathsbook.display()
mathsbook.push(1)
mathsbook.display()
mathsbook.push(3)
mathsbook.push(1)
mathsbook.push(5)
mathsbook.display()
mathsbook.remove()
mathsbook.display()
mathsbook.remove()
mathsbook.display()
mathsbook.remove()
mathsbook.display()
mathsbook.remove()
mathsbook.display()
mathsbook.remove()
mathsbook.display()



        
        

