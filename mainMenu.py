from tkinter import Tk, Label, Button
from game import game
from Modes import Modes

class mainMenu:
        def __init__(self, root):
            self.root = root
            root.title("mainMenu")
            self.game = game()

            self.label = Label(root, text="Choose mode")
            self.label.pack()

            self.lower_button = Button(root, text="lowerCase", command=self.lower_case_game)
            self.lower_button.pack()
            self.root.bind('1', lambda event: self.lower_case_game())

            self.upper_button = Button(root, text="upperCase", command=self.upper_case_game)
            self.upper_button.pack()
            self.root.bind('2', lambda event: self.upper_case_game())

            self.abc_button = Button(root, text="abc", command=self.abc_game)
            self.abc_button.pack()
            self.root.bind('3', lambda event: self.abc_game())

            # self.all_button = Button(root, text="allKeys", command=self.all_game)
            # self.all_button.pack()
            # self.root.bind('4', lambda event: self.lower_case_game())

        def lower_case_game(self):
            self.root.destroy()
            self.game.create_game(Modes.lower)

        def upper_case_game(self):
            self.root.destroy()
            self.game.create_game(Modes.upper)

        def abc_game(self):
            self.root.destroy()
            self.game.create_game(Modes.abc)

        def all_game(self):
            # doesn't work atm, need to fix so u can check shift
            self.root.destroy()
            self.game.create_game(Modes.all_keys)

def main():

    root = Tk()
    mainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
