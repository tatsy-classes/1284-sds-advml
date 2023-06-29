import tkinter as tk

from advml.reversi.gui import Gui
from advml.reversi.state import State

if __name__ == "__main__":
    state = State()
    print(state)

    root = tk.Tk()
    gui = Gui(master=root)
    gui.mainloop()
