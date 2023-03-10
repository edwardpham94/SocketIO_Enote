from tkinter import *
from tkinter import messagebox
from turtle import heading

import socket
import threading
import pickle

PORT = 5550
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.124.2.128"
ADDR = (SERVER, PORT)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except:
    print("Sever not found")


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def sendCommand(client, cmd):
    client.sendall(cmd.encode(FORMAT))


def sendList(client, lst):
    data = pickle.dumps(lst)
    client.sendall(data)


def reciveMessage(client):
    return str(client.recv(2048).decode(FORMAT))


root = Tk()
root.title('Login')
root.geometry('680x350')
root.configure(bg="white")
root.resizable(False, False)


img = PhotoImage(file='photo_note_2.png')
Label(root, image=img, bg="white").place(x=20, y=10)

frame = Frame(root, width=300, height=350, bg="white")
frame.place(x=350, y=10)

heading = Label(frame, text="Log in", fg="#86d9cf", bg="white",
                font=('Bahnschrift SemiLight SemiConde', 23, 'bold'))
heading.place(x=0, y=40)


####################################################################
# username_part

def on_enter(e):
    username.delete(0, 'end')


def on_leave(e):
    name = username.get()
    if name == '':
        username.insert(0, 'Username')


username = Entry(frame, width=25, fg='black', border=0, bg="white",
                 font=('Bahnschrift SemiLight SemiConde', 11))
username.place(x=0, y=110)
username.insert(0, 'username')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame, width=290, height=2, bg='black').place(x=0, y=140)


####################################################################
# password_part

def on_enter(e):
    password.delete(0, 'end')
    # password.Entry(frame, show='*')


def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')


def login():
    _username = str(username.get())
    _password = str(password.get())
    cmd = "login"
    sendCommand(client, cmd)
    sendList(client, [_username, _password])

    messagebox.showinfo("showinfo", reciveMessage(client))


password = Entry(frame, width=25, fg='black', border=0, bg="white",
                 font=('Bahnschrift SemiLight SemiConde', 11))
password.place(x=0, y=160)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width=290, height=2, bg='black').place(x=0, y=190)
####################################################################

Button(frame,
       width=35, pady=7, text='Log in', fg='white', bg="#12756a", border=0,
       font=('Bahnschrift SemiLight SemiConde', 12), command=login).place(x=2, y=220)

label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Bahnschrift SemiLight SemiConde', 12))
label.place(x=50, y=270)

sign_up = Button(frame, width=6, text='Sign up', bg="white", fg='#12756a', border=0, cursor='hand2',
                 font=('Bahnschrift SemiLight SemiConde', 12))
sign_up.place(x=220, y=270)

root.mainloop()
