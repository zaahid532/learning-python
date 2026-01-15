import tkinter as Tk
window = Tk.Tk()
window.title("About me")
window.geometry("1280x720")
window['bg'] = 'white'
icon = Tk.PhotoImage(file='emoji.png')
window.tk.call('wm', 'iconphoto', window._w, icon,)
frame_title = Tk.Frame()
frame_disc = Tk.Frame()
label_title = Tk.Label(
    master = frame_title,
    text = "About Me",
    font = ("Arial", 25),
)


frame_title.pack()
frame_disc.pack()
# label = Tk.Label(
#     text = "About Me",
#     foreground = "white",
#     background = "black",
#     height = 5,
#     width = 25,
#     font = ("Arial", 24),)
label_title.pack()
label_disc = Tk.Label(
    master = frame_disc,
    text = "'hallo nama ku Zaahid umur Aku 13 Tahun aku kelas 7 di sekolah EMIISC jakarta hobi aku adalah menservis barang elektronik dan bermain game"
)

# label.pack()
label_disc.pack()
window.mainloop()
