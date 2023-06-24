from tkinter.filedialog import *
import tkinter as tk

def openFile():
    file = askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content = file.read()
    entry.delete(1.0, "end")
    entry.insert("insert",content)

def clearFile():
    entry.delete(1.0,"end")

def saveFile():
    new_file = asksaveasfile(mode='w',filetype=[('text files','.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0,"end"))
    new_file.write(text)
    new_file.close()

canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Notepad")
canvas.config(bg="black")

top = tk.Frame(canvas)
top.pack(padx=10,pady=10,anchor = "nw")

open_Button = tk.Button(canvas,text="Open",fg="white",bg="black",width=10,font=("",10),command= openFile)
open_Button.pack(side="left",in_=top)

save_Button = tk.Button(canvas,text="Save",fg="white",bg="black",width=10,font=("",10),command=saveFile)
save_Button.pack(side="left",in_=top)

clear_Button = tk.Button(canvas,text="Clear",fg="white",bg="black",width=10,font=("",10),command=clearFile)
clear_Button.pack(side="left",in_=top)

exit_Button = tk.Button(canvas,text="Exit",fg="white",bg="black",width=10,font=("",10),command=exit)
exit_Button.pack(side="left",in_=top)

entry = tk.Text(canvas,bg="cyan",font = ("poppins",14),wrap="word")
entry.pack(padx=5,pady=5,expand=True,fill="both")

canvas.mainloop()
