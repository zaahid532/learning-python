import tkinter as Tk
window = Tk.Tk()
window.title("my application")
window.geometry("1366x768")
frame_title = Tk.Frame(
    master = window,
    width = 250,
    bg = "blue"
)
frame_disc = Tk.Frame(
    master = window,
    width = 250,
    bg = "red"
)
# frame_title.pack(fill = Tk.Y, side = Tk.LEFT)
# frame_disc.pack(fill = Tk.Y, side = Tk.LEFT)
frame_title.pack(side="left", fill="both", expand=False)
frame_disc.pack(side="left", fill="both", expand=True)
window.mainloop()