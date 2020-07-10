from tkinter import Tk, Label, Button
from game import game


class mainMenu:
        def __init__(self, root):
            self.root = root
            root.title("mainMenu")
            self.game = game()

            self.label = Label(root, text="Choose mode")
            self.label.pack()

            self.greet_button = Button(root, text="lowerCase", command=self.lowercasegame)
            self.greet_button.pack()

            self.close_button = Button(root, text="upperCase", command=self.uppercasegame)
            self.close_button.pack()

            self.close_button = Button(root, text="abc", command=self.abcgame)
            self.close_button.pack()

        def lowercasegame(self):
            root.destroy()
            self.game.createGame("lowerCase")

        def uppercasegame(self):
            root.destroy()
            self.game.createGame("upperCase")

        def abcgame(self):
            root.destroy()
            self.game.createGame("abc")

root = Tk()
gui = mainMenu(root)
root.mainloop()