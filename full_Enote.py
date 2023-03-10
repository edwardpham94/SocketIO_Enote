from cgitb import text
from telnetlib import NOP
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

def show_frame(frame):
    frame.tkraise()

root=Tk()
root.title('E-Note')
root.geometry('680x700')
root.configure(bg="white")
root.resizable(False, False)

frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame3 = ttk.Frame(root)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0,column=0,sticky='nsew')
#####################################################################################################################################
# menu 

frame1 = Frame(root, width=680, height=700, bg=('white'), padx = 5, pady = 5)
frame1.place(x=0,y=0)

heading= Label(frame1, text="E-NOTE",fg="#154f3c", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 18, 'bold'))
heading.place(x=300,y=10)


signout_button = Button(frame1,
                 width=10, pady=2, text='Log out', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), command=lambda:show_frame(frame2)).place(x=555,y=0)
####################################################################

frame_menu = Frame(frame1, width=620, height=500, bg=('#c9f5e8'))
frame_menu.place(x=30,y=130)

menu_heading= Label(frame_menu, text="Your notes",fg="#154f3c", bg="#c9f5e8", 
               font=('Bahnschrift SemiLight SemiConde', 18, 'bold'))
menu_heading.place(x=250,y=5)

####################################################################
# button 

def getit():
    print("gud")

textScroll = Text(frame_menu,  bg="#12756a", width=72, height=30)
textScroll.place(x=20,y=50)

sb = Scrollbar(frame_menu, command=textScroll.yview)
sb.place(x=582,y=50, height=450)

textScroll.configure(yscrollcommand=sb.set)

for i in range(20):
    button = Button(textScroll, text="Hello", command=lambda:show_frame(frame5), width=78, height=2)
    textScroll.window_create(END, window=button)
    textScroll.insert(END, "\n")
    
textScroll.configure(state="disabled")



####################################################################
# submit button_object
newnote_button = Button(frame1,
                 width=20, pady=3, text='Add new note', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), command=lambda:show_frame(frame4))
newnote_button.place(x=30,y=60)

#####################################################################################################################################
# login form

frame2 = Frame(root, width=680, height=700, bg=('white'))
frame2.place(x=0,y=0)

####################################################################################
frame_slogan = Frame(frame2, width=680, height=320, bg="#98ebdc")
frame_slogan.place(x=00,y=000)

appname= Label(frame_slogan, text="E-NOTE",fg="white", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 40, 'bold'))
appname.place(x=60,y=30)

slogan= Label(frame_slogan, text="creating your own Emotional Note",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 30, "italic"))
slogan.place(x=60,y=100)

intro1= Label(frame_slogan, text="A product from Group ...",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 20))
intro1.place(x=375,y=200)

intro2= Label(frame_slogan, text="Computer Network-21CLC07",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 20))
intro2.place(x=350,y=250)
####################################################################################
frame_login = Frame(frame2, width=630, height=300, bg="white")
frame_login.place(x=10,y=330)

img1 = PhotoImage(file='photo_note_2.png')
Label(frame_login, image=img1, bg="white").place(x=10,y=15)



heading= Label(frame_login, text="Log in",fg="#86d9cf", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 23,  'bold'))
heading.place(x=320,y=40)


####################################################################
# username_part

def on_enter1(e):
    user2.delete(0,'end')
    
def on_leave1(e):
    name=user.get()
    if name=='':
        user2.insert(0,'Username')
    

user2= Entry(frame_login, width=25, fg='black', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 11))
user2.place(x=320,y=110)
user2.insert(0,'Username')
user2.bind('<FocusIn>', on_enter1)
user2.bind('<FocusOut>', on_leave1)

Frame(frame_login, width=290, height=2, bg='black').place(x=320,y=140)


####################################################################
# password_part

def on_enter2(e):
    code2.delete(0,'end')
    
def on_leave2(e):
    name=code2.get()
    if name=='':
        code2.insert(0,'Password')
        
code2= Entry(frame_login, width=25, fg='black', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 11))
code2.place(x=320,y=160)
code2.insert(0,'Password')
code2.bind('<FocusIn>', on_enter2)
code2.bind('<FocusOut>', on_leave2)

Frame(frame_login, width=290, height=2, bg='black').place(x=320,y=190)
####################################################################

Button(frame_login,
       width=35, pady=7, text='Log in', fg='white', bg="#12756a", border=0, 
       font=('Bahnschrift SemiLight SemiConde',12), command=lambda:show_frame(frame1)).place(x=320,y=220)
label= Label(frame_login, text="Don't have an account?", fg='black', bg='white', font=('Bahnschrift SemiLight SemiConde',12))
label.place(x=370,y=270)

sign_up= Button(frame_login,width=6, text='Sign up', bg="white", fg='#12756a', border=0, cursor='hand2',
                font=('Bahnschrift SemiLight SemiConde',12), command=lambda:show_frame(frame3))
sign_up.place(x=520,y=268)

#####################################################################################################################################
# sign up form

frame3 = Frame(root, width=680, height=700, bg=('white'))
frame3.place(x=0,y=0)


frame_slogan = Frame(frame3, width=680, height=320, bg="#98ebdc")
frame_slogan.place(x=00,y=000)

appname= Label(frame_slogan, text="E-NOTE",fg="white", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 40, 'bold'))
appname.place(x=60,y=30)

slogan= Label(frame_slogan, text="creating your own Emotional Note",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 30, "italic"))
slogan.place(x=60,y=100)

intro1= Label(frame_slogan, text="A product from Group ...",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 20))
intro1.place(x=375,y=200)

intro2= Label(frame_slogan, text="Computer Network-21CLC07",fg="#145243", bg="#98ebdc", 
               font=('Bahnschrift SemiLight SemiConde', 20))
intro2.place(x=350,y=250)


####################################################################################
frame_signup1 = Frame(frame3, width=630, height=300, bg="white")
frame_signup1.place(x=10,y=330)

img = PhotoImage(file='photo_note_2.png')
Label(frame_signup1, image=img, bg="white").place(x=10,y=20)

frame_signup = Frame(frame_signup1, width=300, height=390, bg="white")
frame_signup.place(x=350,y=10)

heading= Label(frame_signup, text="Sign up",fg="#86d9cf", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 23, 'bold'))
heading.place(x=0,y=0)

####################################################################
# name_part

def on_enter3(e):
    full_name.delete(0,'end')
    
def on_leave3(e):
    name=full_name.get()
    if name=='':
        full_name.insert(0,'Fullname')
    

full_name= Entry(frame_signup, width=25, fg='black', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 11))
full_name.place(x=0,y=60)
full_name.insert(0,'Fullname')
full_name.bind('<FocusIn>', on_enter3)
full_name.bind('<FocusOut>', on_leave3)


Frame(frame_signup, width=290, height=2, bg='black').place(x=0,y=90)

####################################################################
# username_part

def on_enter4(e):
    user.delete(0,'end')
    
    
def on_leave4(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
    

user= Entry(frame_signup, width=25, fg='black', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 11))
user.place(x=0,y=110)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter4)
user.bind('<FocusOut>', on_leave4)

Frame(frame_signup, width=290, height=2, bg='black').place(x=0,y=140)


####################################################################
# password_part

def on_enter5(e):
    code.delete(0,'end')
    
def on_leave5(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
code= Entry(frame_signup, width=25, fg='black', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 11))
code.place(x=0,y=160)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter5)
code.bind('<FocusOut>', on_leave5)

Frame(frame_signup, width=290, height=2, bg='black').place(x=0,y=190)
####################################################################

Button(frame_signup,
       width=35, pady=7, text='Sign in', fg='white', bg="#12756a", border=0, 
       font=('Bahnschrift SemiLight SemiConde',12)).place(x=2,y=210)
label= Label(frame_signup, text="Already have an account?", fg='black', bg='white', font=('Bahnschrift SemiLight SemiConde',12))
label.place(x=40,y=260)

sign_up= Button(frame_signup,width=6, text='Log in', bg="white", fg='#12756a', border=0, cursor='hand2',
                font=('Bahnschrift SemiLight SemiConde',12) , command=lambda:show_frame(frame2))
sign_up.place(x=205,y=258)

#####################################################################################################################################
# new note form

frame4 = Frame(root, width=680, height=700, bg=('white'), padx = 5, pady = 5)
frame4.place(x=0,y=0)

####################################################################
# page name

heading= Label(frame4, text="A NEW NOTE",fg="#154f3c", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 18, 'bold'))
heading.place(x=270,y=10)

back_button = Button(frame4,
                 width=5, pady=2, text='Back', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), command=lambda:show_frame(frame1)).place(x=600,y=0)
####################################################################
# title Note name 


heading1= Label(frame4, text="Note title : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'))
heading1.place(x=30,y=40)

def enter_type(e):
    titleNote1.delete(0,'end')
    
def leave_type(e):
    name=titleNote1.get()
    if name=='':
        titleNote1.insert(0,'type here')
    

titleNote1= Entry(frame4, width=30, fg='#048a49', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 14))
titleNote1.place(x=140,y=42)
titleNote1.insert(0,'type here')
titleNote1.bind('<FocusIn>', enter_type)
titleNote1.bind('<FocusOut>', leave_type)

Frame(frame4, width=290, height=2, bg='black').place(x=140,y=72)


####################################################################
# type of note 
# services1 = []

# def showInfor():
#     for i in range(3):
#         selected=""
#         if services1[i].get() >= 1:
#             selected1 = str(i)
#             if selected1 == '0':
#                 link_path1.config(state=DISABLED)
#                 file_button1.config(state=DISABLED)
#                 print('option 1')
#             if selected == '1':
#                 print('option 2')
#                 textInput.config(state=DISABLED)
#             if selected == '2':            
#                 textInput.config(state=DISABLED)
#                 print('option 3')
                
                
                
heading2= Label(frame4, text="Type of note : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'),)
heading2.place(x=30,y=115)


# for i in range(3):
#     option = IntVar()
#     option.set(0)
#     services1.append(option)
                       
# check1 = Checkbutton(frame4, text= "Text", cursor='hand2',fg="#048a49",
#                  font=('Bahnschrift SemiLight SemiConde',14), variable=services1[0])
# check1.place(x=180, y =110)

# check2 = Checkbutton(frame4, text= "Image", cursor='hand2', fg="#048a49",
#                  font=('Bahnschrift SemiLight SemiConde',14), variable=services1[1])
# check2.place(x=290, y =110)

# check3 = Checkbutton(frame4, text= "File", cursor='hand2', fg="#048a49",
#                  font=('Bahnschrift SemiLight SemiConde',14), variable=services1[2])
# check3.place(x=400, y =110)

# checkbutton1 = Button(frame4, text="Choose",cursor='hand2', fg="#048a49",
#                  font=('Bahnschrift SemiLight SemiConde',14), 
#                  command=showInfor)
# checkbutton1.place(x= 500, y=108)


def selection():
    selected = int(radio.get())
    if selected > 1:
        textInput.config(state=DISABLED)
    else:                
        link_path1.config(state=DISABLED)
        file_button1.config(state=DISABLED)
        


radio = IntVar()
check1 = Radiobutton(frame4, text="Text", cursor='hand2', fg="#048a49",
                     font=('Bahnschrift SemiLight SemiConde', 14), variable=radio,
                     value=1, command=selection)
check1.place(x=180, y=114)

check2 = Radiobutton(frame4, text="Image", cursor='hand2', fg="#048a49",
                     font=('Bahnschrift SemiLight SemiConde', 14),  variable=radio,
                     value=2, command=selection)
check2.place(x=290, y=114)

check3 = Radiobutton(frame4, text="File", cursor='hand2', fg="#048a49",
                     font=('Bahnschrift SemiLight SemiConde', 14),  variable=radio,
                     value=3, command=selection)
check3.place(x=400, y=114)

####################################################################
# txt area

textInput = Text(frame4 , height= 15, width= 67,
            bg=('#b3f2dd'), font=('Bahnschrift SemiLight SemiConde', 14),
            padx = 10, pady = 10)
textInput.place(x=30, y = 170)
 

####################################################################
# file area

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')])
   if file:
      filepath = os.path.abspath(file.name)
      link_path1.delete(1, END)  # Remove current text in entry
      link_path1.insert(0,filepath)  # Insert the 'path'

heading3= Label(frame4, text="File link : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'))
heading3.place(x=30,y=570)

link_path1 = Entry(frame4, width = 47, fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14))
link_path1.place(x=128, y=571,width=428,height=35.5)

file_button1 = Button(frame4, text='Choose file', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14),
                 command=open_file
               )
file_button1.place(x=561,y=571)


####################################################################
# submit button_object

def submit_button():
    # inputTXT = text.get("1.0",END)
    # titleName = titleNote.get()
    titleNote.config(state=DISABLED)
    textInput.config(state=DISABLED)
    link_path1.config(state=DISABLED)
    file_button1.config(state=DISABLED)

submit_button = Button(frame4,
                 width=20, pady=3, text='Submit', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), 
                 command = submit_button)
submit_button.place(x=250,y=640)

#####################################################################################################################################
# old note form

frame5 = Frame(root, width=680, height=700, bg=('white'), padx = 5, pady = 5)
frame5.place(x=0,y=0)


####################################################################
# page name

heading= Label(frame5, text="E-NOTE",fg="#154f3c", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 18, 'bold'))
heading.place(x=300,y=10)

back_button = Button(frame5,
                 width=5, pady=2, text='Back', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14), command=lambda:show_frame(frame1)).place(x=600,y=0)

####################################################################
# title Note name 

heading1= Label(frame5, text="Note title : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'))
heading1.place(x=30,y=40)

def on_enter(e):
    titleNote.delete(0,'end')
    
def on_leave(e):
    name=titleNote.get()
    if name=='':
        titleNote.insert(0,'type here')
    

titleNote= Entry(frame5, width=25, fg='#048a49', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 14))
titleNote.place(x=140,y=42)
titleNote.bind('<FocusIn>', on_enter)
titleNote.bind('<FocusOut>', on_leave)

Frame(frame5, width=290, height=2, bg='black').place(x=140,y=72)

####################################################################
# type of note 
services = []

heading2= Label(frame5, text="Type : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'),)
heading2.place(x=30,y=115)

titletxt = Entry(frame5, width=15, fg='#048a49', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 14))
Frame(frame5, width=150, height=2, bg='black').place(x=90,y=142)
titletxt.bind('<FocusIn>', on_enter)
titletxt.bind('<FocusOut>', on_leave)



headingTime= Label(frame5, text="Time : ",fg="#048a49", bg="white", 
               font=('Bahnschrift SemiLight SemiConde', 14, 'bold'),)
headingTime.place(x=300,y=115)

time = Entry(frame5, width=15, fg='#048a49', border=0, bg="white", 
            font=('Bahnschrift SemiLight SemiConde', 14))
Frame(frame5, width=150, height=2, bg='black').place(x=360,y=142)

####################################################################
# txt area

text = Text(frame5 , height= 15, width= 67,
            bg=('#b3f2dd'), font=('Bahnschrift SemiLight SemiConde', 14),
            padx = 10, pady = 10)
text.place(x=30, y = 190)
 
####################################################################
# download button_object


download_button = Button(frame5,
                 width=20, pady=3, text='Download file', fg='white', bg="#12756a", border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde',14))
download_button.place(x=250,y=600)


show_frame(frame1)

root.mainloop()