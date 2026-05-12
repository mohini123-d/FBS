from singer import Singer
from dancer import Dancer

class performer(Singer,Dancer):
    def __init__(self, songs,steps,exp):
        Singer.__init__(self,songs)
        Dancer.__init__(self,steps)
        self.exp = exp
    def skill1(self):
        
        print("She or he Performer....")

 
p1 = performer('Classical','Bharatnatyam',50)
p1.skill() 
p1.skill1()