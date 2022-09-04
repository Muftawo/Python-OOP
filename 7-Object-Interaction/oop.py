
# aggregation
class Car:
    def __init__(self,model,year,is_manual,max_passengers,speed,rotation):
        self.model:str = model
        self.year:int = year
        self.is_manual:bool = is_manual
        self.max_passengers:int = max_passengers
        self.speed:float = speed
        self.rotation:float = rotation
     
    def accelerate(self):
        return f"{self.model} {self.year} accelerating at {self.speed} Km/h " 
     
     
    def decelerate(self):
        return f"{self.model} {self.year} decelerating at {self.speed} Km/h "
    
    
    def _break(self):
        return f"{self.model} {self.year} on break"
    
    def steer(self):
        return f"{self.model} {self.year} steering at angle {self.rotation}"
    
    
        
    def __str__(self):
        return f"{self.model}-{self.year}"
        



class Driver:
    def __init__(self,id,name ):
        self.id = id
        self.name = name
        
    def drive(self,car):
        print(f"Driver {self.name} is driving {car.model}")
        print(f"Driver {self.name} is accelerating the car")
        print(f"The car's speed is {car.accelerate()}")
        
        
sports_car = Car("Porsche GT2", 2006, True, 4, 5.0,4.0)

driver = Driver("F123", "Michael Schumacher")

driver.drive(sports_car)