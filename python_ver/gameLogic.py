from controllers.user import Player
from tkinter import *

window = Tk()
window.title("Forever Maze")
window.minsize(width=480, height=240)
window.config(padx=10, pady=10, bg="black")


player = Player(name='cool guy', health=100, weapon=1, armour=0)

response = ''


def startGame():
    global response
    
    question = Entry(width=100)
    question.grid(column=0, row=3)
    question.config()

    # while response != 'exit':
    #     response = input("What is your choice? (forward, left, right) or leave? (exit): ")
    #     player.movement()
    #     print(player.location)
    
    
    


     
startGame()      
window.mainloop()