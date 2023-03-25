
from tkinter import *
import random
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD

root = Tk()
root.title("Capcha Generator")

label = LabelFrame(root, text = "capcha",bg = "light green")
label.pack()

list =  []
for i in range(65,91) :
    letter = chr(i)
    list.append(letter)

for j in range(97,123) :
    letter = chr(j)
    list.append(letter)

for m in range(0,10) :
    list.append(m)



capcha = random.choices(list,k = 6)
canvas= Canvas(root, width= 320, height= 320, bg="red")

canvas.create_text(0,0, text= capcha ,font=('Courier 20 bold'))

label1 =Label(label,text = capcha,bg = "light green",fg = "black",font = ("Courier",20,BOLD)).grid(row = 0,column = 0)

display = Label(label,text = "*This Capcha has 6 Characters*",bg = "light green").grid(row = 1,column = 0)


e = Entry(label, width = "30",fg = "Indigo" ,justify="center")
e.grid(row = 2,column = 0)

def check_capcha() :
    global main,capcha
    
    main = ""
    for i in capcha:
        main += str(i)

    if main == str(e.get()):
        messagebox.showinfo("Success","You entered correct Capcha!")
        
    else:
        messagebox.showinfo("Error","You entered incorrect Capcha!\n\nTry again")
        e.delete(0,END)
    reload()

button = Button(label,text = "Submit",command=check_capcha ,bg = "green",fg = "black").grid(row=3, column=0, columnspan=2)

def reload() :
    global capcha,e
    label1 =Label(label,text = capcha,bg = "light green",fg = "light green",font = ("Courier",20,BOLD)).grid(row = 0,column = 0)
    capcha = random.choices(list,k = 6)
    label1 =Label(label,text = capcha,bg = "light green",fg = "black",font = ("Courier",20,BOLD)).grid(row = 0,column = 0)
    e = Entry(label, width = "30",fg = "Indigo" ,justify="center")
    e.grid(row = 2,column = 0)

button1 = Button(label,text = "Reload",command=reload ,bg = "green",fg = "black").grid(row=2, column=1)

root.mainloop()


 