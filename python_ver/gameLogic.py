from controllers.user import Player
from tkinter import *

window = Tk(screenName='Forever Maze')
window.title("Forever Maze")
window.minsize(width=1200, height=720)
window.config(padx=100, pady=100)





window.mainloop()










player = Player(name='cool guy', health=100, weapon=1, armour=0)

response = ''



while response != 'exit':
    response = input("What is your choice? (forward, left, right) or leave? (exit): ")
    player.movement()
    
    print(player.location)
         
        
    
