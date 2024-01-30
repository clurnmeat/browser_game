from controllers.user import Player
from tkinter import *

window = Tk()
window.title("Forever Maze")
window.minsize(width=480, height=480)
window.config(bg="black")
window.geometry = ('300x300')



gameMap = Canvas()
gameMap.config(bg='blue', width=250)
gameMap.grid(row=0, column=1, padx=10, pady=10, columnspan=1, sticky=N)



itemText = Canvas()
itemText.config(bg='white', width=200, height=200)
itemText.grid(row=0, column=0, padx=40, pady=40, columnspan=2, sticky='w')



player = Player(name='cool guy', health=100, weapon=1, armour=0)

response = ''


def startGame():
    global response
    question = Entry(width=100)
    question.config(textvariable='What is your choice?')
    question.grid(row=1, column=0, columnspan=3, padx=20, sticky=S, pady=20)
    
    


     
startGame()      
window.mainloop()