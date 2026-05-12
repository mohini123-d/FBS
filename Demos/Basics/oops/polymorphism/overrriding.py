class Vehicle:
    def brake(self):
        return 'Vehicle stopped'
    
class car(Vehicle):
    def brake(self):
        return 'Car stopped.'

   
c1 = car()
print(c1.brake())
     