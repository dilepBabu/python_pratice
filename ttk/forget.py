from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Create New Password')
root.geometry('1270x685')
root.config(bg='sky blue')
productframe=Frame(root)
productframe.pack()


def clear():
        newentry.delete(0,END)
        oldentry.delete(0,END)
        reentry.delete(0,END)
        





def submit():
            if oldentry.get() == '':
                messagebox.showerror('Alert!', 'Please enter your Old Password')

            elif newentry.get() == '':
                messagebox.showerror('Alert!', 'Please enter your New password')

            elif reentry.get() == '':
                messagebox.showerror('Alert!', 'Please re-enter your password')
            else:
                import gsg
        


def show1():
            oldentry.config(show='*')
            check1.config(command=hide1)


def hide1():
            oldentry.config(show='')
            check1.config(command=show1)


def show2():
            newentry.config(show='*')
            check2.config(command=hide2)


def hide2():
            reentry.config(show='')
            check3.config(command=show1)
def show3():
            reentry.config(show='*')
            check3.config(command=hide3)


def hide3():
            newentry.config(show='')
            check2.config(command=show3)           

global oldentry
global reentry
global newentry


toolsframe=LabelFrame(productframe,text="CREATE NEW PASSWORD",font=('times new romen',15,'bold')
                                    ,bg='lavender',bd=8,relief=GROOVE)
toolsframe.grid(row=0,column=0)


oldlabel=Label(toolsframe,text="Old Password",font=('times new romen',15,'bold'),bg='sky blue')
oldlabel.grid(row=5,column=0,pady=10,padx=20)
oldentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
oldentry.grid(row=5,column=1,padx=20,pady=10)


newlabel=Label(toolsframe,text="New Password",font=('times new romen',15,'bold'),bg='sky blue')
newlabel.grid(row=8,column=0,pady=10,padx=20)
newentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
newentry.grid(row=8,column=1,padx=20,pady=10)



relabel=Label(toolsframe,text="RE-Enter Password",font=('times new romen',15,'bold'),bg='sky blue')
relabel.grid(row=12,column=0,pady=10,padx=20)
reentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
reentry.grid(row=12,column=1,padx=20,pady=10)

submitbtn=Button(toolsframe,text='Submit',font=('times new romen',15,'bold'),bg='sky blue',width=10,command=submit)
submitbtn.grid(row=16,column=1,padx=30,pady=30)

clearbtn=Button(toolsframe,text='Clear',font=('times new romen',15,'bold'),bg='sky blue',width=10,command=clear)
clearbtn.grid(row=16,column=0,padx=30,pady=30)




check1 = Checkbutton(toolsframe, bg="lavender", width=5, command=show1)
check1.grid(row=5,column=3,padx=20,pady=10)


check2 = Checkbutton(toolsframe, bg="lavender", width=5, command=show2)
check2.grid(row=8,column=3,padx=20,pady=10)

check3 = Checkbutton(toolsframe, bg="lavender", width=5, command=show3)
check3.grid(row=12,column=3,padx=20,pady=10)

root.mainloop()
