from tkinter import Tk, Label, Button
from game import game


class mainMenu:
        def __init__(self, root):
            self.root = root
            root.title("mainMenu")
            self.game = game()

            self.label = Label(root, text="Choose mode")
            self.label.pack()

            self.lower_button = Button(root, text="lowerCase", command=self.lowercasegame)
            self.lower_button.pack()

            self.upper_button = Button(root, text="upperCase", command=self.uppercasegame)
            self.upper_button.pack()

            self.abc_button = Button(root, text="abc", command=self.abcgame)
            self.abc_button.pack()

            # self.all_button = Button(root, text="allKeys", command=self.allgame)
            # self.all_button.pack()

        def lowercasegame(self):
            self.root.destroy()
            self.game.createGame("lowerCase")

        def uppercasegame(self):
            self.root.destroy()
            self.game.createGame("upperCase")

        def abcgame(self):
            self.root.destroy()
            self.game.createGame("abc")

        def allgame(self):
            # doesn't work atm, need to fix so u can check shift
            self.root.destroy()
            self.game.createGame("allKeys")

def main():

    root = Tk()
    mainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
