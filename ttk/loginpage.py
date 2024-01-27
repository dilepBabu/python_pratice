from tkinter import *
from tkinter import messagebox



window = Tk()
window.title("Registration Form")
window.geometry("700x685")
def backs():
    import gsg

def submit1():
    if firstnameentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your First Name')

    elif lastnameentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your Last Name')
    elif emailentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your Email')
    elif gender.get() == '':
        messagebox.showerror('Alert!', 'Please select your gender')
    elif om.get() == '':
        messagebox.showerror('Alert!', 'Please seect your country')
    elif usernameentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your username')
    elif passwordentry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your password')
    elif cpasswordentry.get() == '':
        messagebox.showerror('Alert!', 'Please confirm your password')
    else:
        import gsg


def show1():
    passwordentry.config(show='*')
    check.config(command=hide1)


def hide1():
    passwordentry.config(show='')
    check.config(command=show1)


def show2():
    cpasswordentry.config(show='*')
    check1.config(command=hide2)


def hide2():
    cpasswordentry.config(show='')
    check1.config(command=show1)


firstname = StringVar()
lastname = StringVar()
email = StringVar()
gender = StringVar()
om = StringVar()
username = StringVar()
password = StringVar()
cpassword = StringVar()

frame = Frame(window, width=1270, height=685, bg="light sky blue", bd=8)
frame.pack()

om.set('Select Country')


country = ['Australia', 'Germany', 'Canada', 'Afghanistan', 'Belgium', 'Angola', 'Cameroon', 'France', 'Argentina',
           'Algeria', 'China', 'Egypt', 'Austria', 'India', 'Brazil']

heading = Label(frame, text="Registration Form", font=("arial", 20, "bold"))
heading.place(x=100, y=3)

firstnamelbl = Label(frame, text="First Name:", font=('arial', 15, 'bold'))
firstnamelbl.place(x=10, y=70)
firstnameentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
firstnameentry.place(x=240, y=70)
lastnamelbl = Label(frame, text="Last Name:", font=('arial', 15, 'bold'))
lastnamelbl.place(x=10, y=110)
lastnameentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
lastnameentry.place(x=240, y=110)
emaillbl = Label(frame, text="Email:", font=('arial', 15, 'bold'))
emaillbl.place(x=10, y=150)
emailentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
emailentry.place(x=240, y=150)
genderlbl = Label(frame, text="Select Gender:", font=('arial', 15, 'bold'))
genderlbl.place(x=10, y=190)
gender.set(0)
genderentry1 = Radiobutton(frame, text='Male', variable=gender, value='Male', font=('arial', 15, 'bold'), width=5)
genderentry1.place(x=240, y=190)
genderentry2 = Radiobutton(frame, text='Female', variable=gender, value='Female', font=('arial', 15, 'bold'), width=5)
genderentry2.place(x=340, y=190)
genderentry2 = Radiobutton(frame, text='Others', variable=gender, value='Others', font=('arial', 15, 'bold'), width=5)
genderentry2.place(x=440, y=190)
countrylabel = Label(frame, text="Select Country:", font=('arial', 15, 'bold'))
countrylabel.place(x=10, y=240)
countrylabelo = OptionMenu(frame, om, *country)
countrylabelo.place(x=240, y=240)
countrylabelo.config(width=18, font=('arial', 15, 'bold'))
usernamelbl = Label(frame, text="User Name:", font=('arial', 15, 'bold'))
usernamelbl.place(x=10, y=290)
usernameentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
usernameentry.place(x=240, y=290)
passwordlbl = Label(frame, text="Password:", font=('arial', 15, 'bold'))
passwordlbl.place(x=10, y=330)
passwordentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
passwordentry.place(x=240, y=330)
cpasswordlbl = Label(frame, text="Confirm Password:", font=('arial', 15, 'bold'))
cpasswordlbl.place(x=10, y=370)
cpasswordentry = Entry(frame, font=('arial', 15, 'bold'), width=30, borderwidth=2)
cpasswordentry.place(x=240, y=370)

submitbtn = Button(frame, text='Submit', width=15, borderwidth=5, height=2, cursor='hand2', bd=2,
                   font=('arial', 15, 'bold'), command=submit1)
submitbtn.place(x=300, y=490)
back = Button(frame, text='Back', width=15, borderwidth=5, height=2, cursor='hand2', bd=2, font=('arial', 15, 'bold'),command=backs)
back.place(x=50, y=490)

check = Checkbutton(frame, bg="light sky blue", width=5, command=show1)
check.place(x=580, y=330)
check1 = Checkbutton(frame, bg="light sky blue", width=5, command=show2)
check1.place(x=580, y=370)

window.mainloop()