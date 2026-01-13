import tkinter as Tk
window = Tk.Tk()
window.title("my application")
window.geometry("1280x720")
window['bg'] = 'gray'
icon = Tk.PhotoImage(file='emoji.png')
window.tk.call('wm', 'iconphoto', window._w, icon,)
frame_title = Tk.Frame()
frame_disc = Tk.Frame()
label_title = Tk.Label(
    master = frame_title,
    text = "My application",
    font = ("Arial", 25),
)
label_title.pack()
label_desc = Tk.Label(
    master = frame_disc,
    text = "'Descriptions here"
)
label_desc.pack()
frame_title.pack()
frame_disc.pack()
label = Tk.Label(
    text = "Hello World",
    foreground = "white",
    background = "black",
    height = 5,
    width = 25,
    font = ("Arial", 24),)
button = Tk.Button(
    text = "Button",
    bg = "Blue", fg = "White",
    font = ("Arial", 18),
    height = 5, width = 15
)
entry = Tk.Entry(
    font = ("Arial", 17)
)
text_box = Tk.Text(
    font = ("Arial", 17),
    width = 25,
    height = 8
)
entry.pack()
button.pack()
label.pack()
text_box.pack()
window.mainloop()