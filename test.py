import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack(fill=tk.X)
frame_b.pack()

button_a = tk.Button(master=frame_a, text="I'm a button")
button_a.pack(fill=tk.X)

window.mainloop()
