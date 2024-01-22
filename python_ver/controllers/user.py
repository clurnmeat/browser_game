class Player:
    def __init__(self, health, weapon, armour):
        self.location = [0,0]
        self.health = health
        self.weapon = weapon
        self.armour = armour
        
    def forward(self):
        self.location[1] += 1
     
    def left(self):
        self.location    