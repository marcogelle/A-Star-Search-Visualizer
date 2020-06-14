import tkinter as tk

from constants import *

class App:
    def __init__(self, parent):
        self.root = parent
        self.frames = []
        self.draw_btn()
        self.draw_frames()

    def draw_frames(self):
        for i in range(3):
            self.frames.append(tk.Frame(
                master=self.root,
                relief=tk.RIDGE,
                borderwidth=1,
                bg=GRID_COLOR,
                width=SPOT_SIZE,
                height=SPOT_SIZE
                ))
            self.frames[i].pack()

    def draw_btn(self):
        def color():
            for f in self.frames:
                self.root.after(500)
                f['bg'] = "red"

        btn = tk.Button(master=self.root, text="press me", command=color)
        btn.pack()


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
