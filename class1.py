class Cars ():
    def __init__(self,engine,brand,material,horsepower):
        self.engine = engine 
        self.brand = brand 
        self.material = material 
        self.horsepower = horsepower 


    def getdata(self): 
        return self.engine,self.brand,self.material,self.horsepower

    def updatevalue(self,new_engine):
        self.engine = new_engine 

    def displaycars(self):
        print("I am a car with", self.engine, self.brand,self.material,self.horsepower)


bmw = Cars ("bmw engine","bmw","carbon fibre", "200")


bmw.displaycars()
bmw.getdata()
bmw.updatevalue("bmw engine 2" )
bmw.displaycars()

