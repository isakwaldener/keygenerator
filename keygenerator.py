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
        self.frame = Frame(self.root, width=1000, height=1000)
        self.Keygenerator = Keygenerator()

    def guiInit(self):
        heigth = 1000
        width = 1000
        self.root.geometry(f"{heigth}x{width}")

        self.addStartButton()
        self.addEntry()

    def guiRunning(self):
        self.frame.pack()
        self.root.mainloop()

    def addNums(self):
        self.Keygenerator.fixNumbers()
        nums = self.Keygenerator.getNumbers()

        label = Label(self.frame, text="{0}".format(chr(nums[0])))
        label.pack()

    def addStartButton(self):
        button = Button(self.frame)
        button.pack()

    def addEntry(self):
        entry = Entry(self.frame)
        entry.pack()

    """def addFrame(self):
        frame =
        return frame"""


gui = Gui()

gui.addNums()
gui.guiInit()
gui.guiRunning()
print(text.get())
