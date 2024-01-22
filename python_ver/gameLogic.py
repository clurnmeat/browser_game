from controllers.user import Player
import random

person = Player(name='cool guy', health=100, weapon=1, armour=0)





for n in range(10):
    person.move_forward()
    while(person.location[0] < 3):
        if(person.location[1] > 3):
            person.location[1] = random.randint(0, 3)
           
        elif(person.location[0] <= 3):
            person.location[0] += 1
        print(person.location)
         
        
    
