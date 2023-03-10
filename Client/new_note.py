from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import heading
from tkinter import messagebox
from turtle import left
import tkinter.filedialog as filedialog
import os
import shutil
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

root=Tk()
root.title('E-Note')
root.geometry('680x700')
root.configure(bg="white")
root.resizable(False, False)

####################################################################
# page name

heading= Label(root, text="A NEW NOTE",fg="#154f3c", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 18, 'bold'))
heading.place(x=270,y=10)

back_button = Button(root,
                 width=5, pady=2, text='Back', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14)).place(x=600,y=0)
####################################################################
# title Note name 


heading1= Label(root, text="Note title : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'))
heading1.place(x=30,y=40)

def on_enter(e):
    titleNote.delete(0,'end')
    
def on_leave(e):
    name=titleNote.get()
    if name=='':
        titleNote.insert(0,'type here')
    

titleNote= Entry(root, width=25, fg='#048a49', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 14))
titleNote.place(x=140,y=42)
titleNote.insert(0,'type here')
titleNote.bind('<FocusIn>', on_enter)
titleNote.bind('<FocusOut>', on_leave)

Frame(root, width=290, height=2, bg='black').place(x=140,y=72)


####################################################################
# type of note 
services = []

heading2= Label(root, text="Type of note : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'),)
heading2.place(x=30,y=115)


def showInfo():
    for i in range(len(services)):
        selected=""
        #Get services variable
        if services[i].get()>=1:
            selected = str(i)
            if selected == '0':
                    link_path.config(state=DISABLED)
                    file_button.config(state=DISABLED)
            if selected == '1':
                    text.config(state=DISABLED)
            if selected == '2':            
                text.config(state=DISABLED)

for i in range(3):
    option = IntVar()
    option.set(0)
    services.append(option)
                       
check1 = Checkbutton(root, text= "Text", cursor='hand2',fg="#048a49",
                 font=('Bahnschrift SemiLight SemiConde',14), variable=services[0])
check1.place(x=180, y =110)

check2 = Checkbutton(root, text= "Image", cursor='hand2', fg="#048a49",
                 font=('Bahnschrift SemiLight SemiConde',14), variable=services[1])
check2.place(x=290, y =110)

check3 = Checkbutton(root, text= "File", cursor='hand2', fg="#048a49",
                 font=('Bahnschrift SemiLight SemiConde',14), variable=services[2])
check3.place(x=400, y =110)

checkbutton = Button(root, text="Choose",cursor='hand2', fg="#048a49",
                 font=('Bahnschrift SemiLight SemiConde',14), 
                 command=showInfo)
checkbutton.place(x= 500, y=108)

####################################################################
# txt area

text = Text(root , height= 15, width= 67,
            bg=('#b3f2dd'), font=('Bahnschrift SemiLight SemiConde', 14),
            padx = 10, pady = 10)
text.place(x=30, y = 170)
 

####################################################################
# file area

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')])
   if file:
      filepath = os.path.abspath(file.name)
      link_path.delete(1, END)  # Remove current text in entry
      link_path.insert(0,filepath)  # Insert the 'path'

heading3= Label(root, text="File link : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'))
heading3.place(x=30,y=570)

link_path = Entry(root, width = 47, fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14))
link_path.place(x=128, y=571,width=428,height=35.5)

file_button = Button(root, text='Choose file', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14),
                 command=open_file
               )
file_button.place(x=561,y=571)


####################################################################
# submit button_object

def submit_button():
    inputTXT = text.get("1.0",END)
    titleName = titleNote.get()
    titleNote.config(state=DISABLED)
    text.config(state=DISABLED)
    link_path.config(state=DISABLED)

submit_button = Button(root,
                 width=20, pady=3, text='Submit', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), 
                 command = submit_button)
submit_button.place(x=250,y=640)
#submit_button.pack()

root.mainloop()