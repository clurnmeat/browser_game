class Player:
    def __init__(self, name, health, weapon, armour):
        self.name = name
        
        self.x = 0
        self.y = 0
        self.location = [self.x,self.y]
        
        self.health = health
        self.weapon = weapon
        self.armour = armour
        
    def move_forward(self):
        self.y += 1
        self.location = [self.x, self.y]
    
    def move_left(self):
        self.x += 1
        self.location = [self.x, self.y]
        
    def move_right(self):
        self.x += 1
        self.location = [self.x, self.y]
    
    def move_back(self):
        self.y -= 1
        self.location = [self.x, self.y]   
        
    
            
