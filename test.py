from tkinter import *

window = Tk()

label = Label(window, text="Hello World!", fg="white", bg="black")
label.pack()

button = Button(
    text="click me?",
    width=25,
    height=5,
    bg="black",
    fg="white"
)
button.pack()

entry = tk.Entry(fg="white", bg="black", width=50)

window.mainloop()
