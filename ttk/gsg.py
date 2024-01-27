import tkinter 
from tkinter import messagebox


win=tkinter.Tk()
win.title("LOGIN")
win.geometry('1270x685')
win.resizable(False,False)
win.configure(bg='slategray1')

    

def forget():
    
    import forget


def login():
    global win
    global usere
    global passworde
    username = "john"
    passw = "12345"
    if usere.get()==username and passworde.get()==passw:
       
       import firstpage
    else:
        messagebox.showerror(title='ERROR',message="Invalid")

def create():
    import loginpage
    


def window():
    global win
    global usere
    global passworde
    
    

    frame=tkinter.Frame(win,bg='slategray2')


    signin=tkinter.Label(frame,text="Login",font=('Arial',30))
    user=tkinter.Label(frame,text='Username:',font=('Arial',16))
    usere=tkinter.Entry(frame,font=('Arial',16),width=20)
    password=tkinter.Label(frame,text='Password',font=('Arial',16))
    passworde=tkinter.Entry(frame,show='*',font=('Arial',16),width=20)
    signb=tkinter.Button(frame,text='Login',font=('Arial',16),command=login)
    oor=tkinter.Label(frame,text="OR",font=('Arial',16))
    forgets=tkinter.Button(frame,text="Forget Password",font=('Arial',13),command=forget)
    new=tkinter.Button(frame,text='CREATE ACCOUNT',font=('Arial',13),width=20,command=create)
    

    signin.grid(row=0,column=0,columnspan=2,pady=30)
    user.grid(row=1,column=0)
    usere.grid(row=1,column=1,pady=20,padx=10)
    password.grid(row=2,column=0)
    passworde.grid(row=2,column=1,pady=20)
    signb.grid(row=3,column=0,columnspan=2,pady=30)
    oor.grid(row=4,column=0,columnspan=2,pady=5)
    forgets.grid(row=5,column=0,columnspan=1,pady=5,padx=20)
    new.grid(row=5,column=1,columnspan=2,padx=20)




    frame.pack()


    win.mainloop()
window()
