from tkinter import Tk, Label, Button
from game import game
from Modes import Modes

class mainMenu:
        def __init__(self, root):
            self.root = root
            self.game = game()
            self.init_gui()

        def init_gui(self):
            self.root.title("mainMenu")
            self.create_label("choose mode")
            self.add_buttons()

        def add_buttons(self):
            self.lower_case_button()
            self.upper_case_button()
            self.abc_case_button()

        def create_label(self, text):
            label = Label(self.root, text=text)
            label.pack()

        def lower_case_button(self):
            self.lower_button = Button(self.root, text="lowerCase", command=self.lower_case_game)
            self.lower_button.pack()
            self.root.bind('1', lambda event: self.lower_case_game())

        def upper_case_button(self):
            self.upper_button = Button(self.root, text="upperCase", command=self.upper_case_game)
            self.upper_button.pack()
            self.root.bind('2', lambda event: self.upper_case_game())

        def abc_case_button(self):
            self.abc_button = Button(self.root, text="abc", command=self.abc_game)
            self.abc_button.pack()
            self.root.bind('3', lambda event: self.abc_game())

        def all_case_button(self):
            self.all_button = Button(self.root, text="allKeys", command=self.all_game)
            self.all_button.pack()
            self.root.bind('4', lambda event: self.lower_case_game())

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
