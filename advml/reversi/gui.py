import tkinter as tk


class Gui(tk.Frame):
    def __init__(self, master=None, width=512, height=512, title="Reversi"):
        super(Gui, self).__init__(master)

        self.title = title
        self.width = width
        self.height = height

        self.master.title(self.title)
        self.master.geometry(f"{self.width:d}x{self.height:d}")

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

    def draw(self, board):
        dx = self.width // 8
        dy = self.height // 8
        r = int(min(dx, dy) * 0.4)
        for x in range(8):
            for y in range(8):
                cx = x * dx + dx // 2
                cy = y * dy + dy // 2
                if board[x, y] == 1:
                    self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="white")
                elif board[x, y] == -1:
                    self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="black")

        self.canvas.update()
