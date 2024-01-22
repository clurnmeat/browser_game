from controllers.user import Player
import random

player = Player(name='cool guy', health=100, weapon=1, armour=0)

response = ''



while response != 'exit':
    response = input("What is your choice? (forward, left, right) or leave? (exit): ")
    player.movement()
    
    print(player.location)
         
        
    
