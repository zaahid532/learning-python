import tkinter as tk
window = tk.Tk()
window.title("odd or even")
def checkNumber():
    number = int(ent_number.get())
    if number % 2 == 0:
        lbl_result['text'] = f"{number}"
        lbl_result['text'] += "is an even number"
        ent_number.delete(0, tk.END)
    else:
        lbl_result['text'] = f"{number}"
        lbl_result['text'] += "is an odd number"
        ent_number.delete(0, tk.END)
lbl_title = tk.Label(
    text = "odd or even number checker"
)
ent_number = tk.Entry(font = ('Arial', 18))
btn_check = tk.Button(
    text = "check",
    command = checkNumber
)
lbl_result = tk.Label(font = ('Arial', 18))
lbl_title.pack()
ent_number.pack()
btn_check.pack()
lbl_result.pack()
window.mainloop()