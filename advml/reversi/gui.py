import tkinter as tk


class Gui(tk.Frame):
    def __init__(self, master=None, width=512, height=512, title="Reversi"):
        super(Gui, self).__init__(master)

        self.title = title
        self.width = width
        self.height = height

        self.master.title(self.title)
        self.master.geometry(f"{self.width:d}x{self.height:d}")

        canvas = tk.Canvas(
            self.master, width=self.width, height=self.height, bg="white"
        )
        canvas.pack()
