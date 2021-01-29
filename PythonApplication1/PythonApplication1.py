from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput

root = Tk()
root.geometry("600x400")
root.title("Element in TKinter")

def function(a):
    tabs.select(a)

def open_():
    file = askopenfilename()#название файла
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file = asksaveasfile(mode="w", defaultextension=((".txt"),(".docx")),filetypes = (("Notepad",".txt"),("Word",".docx")))
    t = txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

def imgChange(name, sample):
    tabs.select(1)
    global img
    img = PhotoImage(file=name).subsample(sample)
    can.create_image(10,10,image=img, anchor=NW)

tabs = ttk.Notebook(root)
text = ["First","Second","Third","Fourth"]
#for x in range(4):
#    tab = Frame(tabs)
#   tabs.add(tab, text=text[x])

tabs1 = Frame(tabs)
tabs2 = Frame(tabs)
tabs3 = Frame(tabs)
tabs4 = Frame(tabs)
tabs.add(tabs1, text="First")
tabs.add(tabs2, text="Second")
tabs.add(tabs3, text="Third")
tabs.add(tabs4, text="Fourth")
tabs.pack()

M = Menu(root)
root.config(menu=M)
m1 = Menu(M, tearoff=0)#Пунктир
M.add_cascade(label="Menu", menu=m1)
m1.add_command(label="tab1",accelerator="Command+V", command=lambda:funktion(0))
m1.add_separator()#Линия
m1.add_command(label="Tab2", command=lambda:funktion(1))
m1.add_command(label="Tab3", command=lambda:funktion(2))
m1.add_command(label="Tab4", command=lambda:funktion(3))
m1.add_separator()

m2 = Menu(M, tearoff=0)
M.add_cascade(label="Color", menu=m2)
m2.add_command(label="Yellow",accelerator="Command+V", command=lambda:root.config(bg="yellow"))
m2.add_separator()#Линия
m2.add_command(label="Green", command=lambda:root.config(bg="green"))
m2.add_command(label="Blue", command=lambda:root.config(bg="blue"))
m2.add_command(label="Violet", command=lambda:root.config(bg="violet"))
m2.add_separator()

can = Canvas(tabs2, width=300, height=200)
can.pack()

m3 = Menu(M, tearoff=0)
M.add_cascade(label="Picture", menu=m3)
m3.add_command(label="Car", command=lambda:imgChange("mercedes.png",3))
m3.add_command(label="Raccoon", command=lambda:imgChange("Pet-Raccoons.png",3))

btn_open = Button(tabs1, text="Open", command=open_)
btn_save = Button(tabs1, text="Save", command=save_)
btn_exit = Button(tabs1, text="Exit", command=exit_)
txt_box = scrolledtext.ScrolledText(tabs1, width=40, height=5)

txt_box.grid(row=0, column=0, columnspan=3)
btn_open.grid(row=1, column=0)
btn_save.grid(row=1, column=1)
btn_exit.grid(row=1, column=2)

tabs.pack(fill="both")

root.mainloop()