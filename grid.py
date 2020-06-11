from tkinter import *

window = Tk()

for r in range(20):
    for c in range(35):
        frm = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1,
            width=30,
            height=30
        )
        frm.grid(row=r, column=c)
        btn = Button(master=frm)
        btn.pack(fill="both")


window.mainloop()
