import random

class Player:
    def __init__(self, name, health, weapon, armour):
        self.name = name
        
        self.x = 0
        self.y = 0
        self.location = [self.x,self.y]
        
        self.health = health
        self.weapon = weapon
        self.armour = armour
    
    
    
    def movement(self):
        self.y =random.randint(0,3)
        self.x = random.randint(0,3)
        self.location = [self.x, self.y]  
        
    
            
