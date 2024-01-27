from controllers.user import Player
from tkinter import *

window = Tk()
window.title("Forever Maze")
window.minsize(width=480, height=480)
window.config(padx=10, pady=10, bg="black")




gameMap = Canvas()
gameMap.config(bg='black', )
gameMap.grid(row=0, column=1)

player = Player(name='cool guy', health=100, weapon=1, armour=0)

response = ''


def startGame():
    global response
    question = Entry(width=100)
    question.config(textvariable='What is your choice?')
    question.grid(row=1, column=1)
    
    


     
startGame()      
window.mainloop()