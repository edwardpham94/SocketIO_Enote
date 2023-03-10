from tkinter import *
from turtle import left

def click():
    print("u clicked the button")

def submit():
    username = entry.get()
    print("Hello, " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
    
def display():
    if (x.get()==1):
        print("u agree")
    else:
        print("u dont agree")

win= Tk()
    

x=IntVar()

win.title("Server")  
win.geometry('600x300') # window size
#win['bg']= 'gray'  # backgound color
win.attributes('-topmost', True) # take the win to top most
win.config(background="#98c6d4")

#photo = PhotoImage(file="photo.png")


name=Label(win, 
           text = 'WELCOME!', 
           font=('Times New Roman',14, "bold"), 
           bg = "#98c6d4",
           fg = "white") 
            # bg= backgound chu, fg= mau chu
name.place(x=260,y=5)

but = Button(win, 
             text = 'Click vao day', 
             width = 12, 
             height = 5, 
             bg= 'yellow', 
             font = ('Times New Roman', 14), 
             fg = 'red')
but.place(x=60, y=60)

# but = Button(win, 
#              text = 'Click me', 
#              command =click,
#              font=("Comic Sans", 30), 
#              bg= 'yellow',  # initial color
#              fg= 'green',
#              image=photo, 
#              compound="bottom")
# but.pack()


entry = Entry(win, 
              font=('Times New Roman',20),
              fg="yellow",
              show="*",
              )
entry.pack(side=LEFT)

submit_button = Button(win, 
                       text = 'Submit', 
                       command =submit)
submit_button.pack(side=RIGHT)

delete_button = Button(win,
                       text = 'Delete', 
                       command =delete)
delete_button.pack(side=RIGHT)

check_button= Checkbutton(win,
                          text="you agree to st",
                          variable= x,
                          onvalue=1,
                          offvalue=0,
                          command=display
                          )
check_button.pack()

win.mainloop()