import random
from tkinter import *


class Keygenerator():

	def __init__(self):
		self.number = list(range(ord('a'), ord('z')))

	def getNumbers(self):
		return self.number

	def fixNumbers(self):
		random.shuffle(self.number)



class Gui():
    
  
    def __init__(self):
        self.root = Tk()
        self.heigth = 500
        self.width = 500
        self.root.geometry(f"{self.heigth}x{self.width}")
        self.keygenerator = Keygenerator()
        

    def guiRunning(self):
        self.root.mainloop()

    def addNums(self):
        self.keygenerator.fixNumbers()
        nums = self.keygenerator.getNumbers()
        
        label = Label(self.root, text="{0}".format(chr(nums[0])))
        label.pack()
        

    def addEntry(self):
        entry = Entry(self.root)
        entry.pack()
        return entry

        


gui = Gui()

gui.addNums()
entry = gui.addEntry()
print(entry.get())
gui.guiRunning()

