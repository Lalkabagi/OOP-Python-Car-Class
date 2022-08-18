class AllCar:
    def __init__ (self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return '{} is going'.format(self.name)
    def stop(self):
        return '{} is stoped'.format(self.name)
    def turn(self,direction):
        return '{} returned({})'.format(self.name,direction)

class TownCar(AllCar):
    def name(self):
        return self.name

class SportCar(AllCar):
    def name(self):
        return self.name
    
class WorkCar(AllCar):
   def name(self):
        return self.name
class PoliceCar(AllCar):
    def name(self):
        return self.name

car1 = TownCar(60,"red","Toyota",False)
car2 = SportCar(200,"Light Grey","Ferrari",False)
car3 = WorkCar(40,"Yeloww","Chevrolet",False)
car4 = PoliceCar(160,"White","Skoda",True)

print(car2.stop())