import tkinter


global win
global usere
global passworde
winc=tkinter.Tk()
winc.title("CREATE ACCOUNT") 
winc.geometry('1000x1000')
winc.configure(bg='black')
    
f=tkinter.Frame(winc,bg='#336334')

detail=tkinter.Label(f,text="CREATE ACCOUNT",font=('Arial',30))
fname=tkinter.Label(f,text="FirstName",font=('Arial',16))
fnamee=tkinter.Entry(f,font=('Arial',16))
lname=tkinter.Label(f,text="LastName",font=('Arial',16))
lnamee=tkinter.Entry(f,font=('Arial',16))
email=tkinter.Label(f,text="Email ID",font=('Arial',16))
emaile=tkinter.Entry(f,font=('Arial',16))
address=tkinter.Label(f,text="ADDRESS",font=('Arial',16))
addresse=tkinter.Text(f,font=('Arial',16),width=40,height=5)






detail.grid(row=1,column=0,columnspan=2,sticky="news",pady=15)
fname.grid(row=2,column=0)
fnamee.grid(row=2,column=1,pady=20)
lname.grid(row=3,column=0)
lnamee.grid(row=3,column=1,pady=20)
email.grid(row=4,column=0)
emaile.grid(row=4,column=1,pady=20)
address.grid(row=5,column=0)
addresse.grid(row=5,column=1,pady=20)
f.pack()
winc.mainloop()