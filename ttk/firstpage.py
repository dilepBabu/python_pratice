from tkinter import *
from tkinter import messagebox
import sqlite3


        
def nextp():
    import bill
def calculate_cost():
    
    if firstentry.get()=='' or addressentry.get()=='' and phnoentry.get()=='' and emailentry.get()=='':
           messagebox.showerror('Error','Please Fill The Details')
    elif entry_meter_footage.get()=='' and entry_labour_footage.get()=='' and entry_square_footage.get()=='':
          messagebox.showerror('Error','please mention the feets')   
    else:
            area.delete(1.0,END)
            area.insert(END,f'\n-------------------------------------------------')
            area.insert(END,'   \n\t\t**PC CONSTRUCTION**\n')
            area.insert(END,f'\n-------------------------------------------------')
            area.insert(END,f'\nNAME: {firstentry.get()}\n')
            area.insert(END,f'\nADDRESS: {addressentry.get()}\n')
            area.insert(END,f'\nPHONE: {phnoentry.get()}\n')
            area.insert(END,f'\nEMAIL ID: {emailentry.get()}\n')
            area.insert(END,f'\nNO OF DAYS: {dayentry_labour_footage.get()}\n')
            area.insert(END,f'\nNO OF LABOUR: {entry_labour_footage.get()}\n')
            area.insert(END,f'\nMETER: {entry_meter_footage.get()}\n')
            area.insert(END,f'\nSQUARE FT: {entry_square_footage.get()}\n')
            
    global result_label
    data= sqlite3.connect("pubudget.db")
    c=data.cursor()
    # c.execute("""CREATE TABLE pcdetails(
    #           name TEXT,
    #           address TEXT,
    #           phoneno int,
    #           email TEXT,
    #           feet int,
    #           meter int,
    #           charge int
    # )""")
    name=firstentry.get()
    add=addressentry.get()
    phno=phnoentry.get()
    email=emailentry.get()
    lentry=entry_labour_footage.get()
    mentry=entry_meter_footage.get()
    sentry=entry_square_footage.get()
    


    if name!="" and add!="" and phno!="" and email!="" and lentry!="" and mentry!="" and sentry!="":
        c.execute("INSERT INTO pcdetails VALUES(:name,:address,:email,:feet,:meter,:charge,:phone) ",{
                'name': name,
                'address' :add,
                'feet' :sentry,
                'meter' :mentry,
                'charge' :lentry,
                'phone': phno,
                'email':email
        })
        c.execute("SELECT * FROM pcdetails")
        MYDATAS=c.fetchall()
        print(f'all datas= {MYDATAS}')

        firstentry.delete(0,END)
        addressentry.delete(0,END)
        emailentry.delete(0,END)
        phnoentry.delete(0,END)
    else:
        messagebox.showerror("Error","check data you entered")
    square_footage = int(entry_square_footage.get())
    material_cost = int(entry_meter_footage .get())
    days=int(dayentry_labour_footage.get())
    labor_cost = int(entry_labour_footage .get())* days

    total_cost = square_footage * (material_cost + labor_cost*700)

    result_label.config(text=f"Estimated Cost: Rs {total_cost:,.2f}",font=('times new romen',15,'bold'),bg="white")
    data.commit()
    data.close()


root=Tk()
root.title("PC CONSTRUCTION ")
root.geometry('1270x685')
root.config(bg='lavender')
heading=Label(root,text='PC CONSTRUCTION',font=('times new romen',30,'bold')
              ,bg='cyan2',bd=12,relief=RIDGE)
heading.pack(fill=X)
om = StringVar()
productframe=Frame(root)
productframe.pack()
om.set('Area Of Land')
country = ['Square Feet','Meter']

toolsframe=LabelFrame(productframe,text="",font=('times new romen',15,'bold')
                                    ,bg='thistle',bd=8,relief=GROOVE)
toolsframe.grid(row=0,column=0)


firstlabel=Label(toolsframe,text="NAME :",font=('times new romen',15,'bold'),bg='thistle')
firstlabel.grid(row=0,column=0,pady=10,padx=10)
firstentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
firstentry.grid(row=0,column=1,padx=10,pady=10)


addresslabel=Label(toolsframe,text="ADDRESS :",font=('times new romen',15,'bold'),bg='thistle')
addresslabel.grid(row=1,column=0,pady=10,padx=10)
addressentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
addressentry.grid(row=1,column=1,padx=10,pady=10)

phnolabel=Label(toolsframe,text="PHONE NO :",font=('times new romen',15,'bold'),bg='thistle')
phnolabel.grid(row=2,column=0,pady=10,padx=10)
phnoentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
phnoentry.grid(row=2,column=1,padx=10,pady=10)


emaillabel=Label(toolsframe,text="EMAIL ID :",font=('times new romen',15,'bold'),bg='thistle')
emaillabel.grid(row=3,column=0,pady=8,padx=10)
emailentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=30,bd=5)
emailentry.grid(row=3,column=1,padx=10,pady=10)

label_square_footage = Label(toolsframe, text="SQUARE FEET :",font=('times new romen',15,'bold'),bg='thistle')
label_square_footage.grid(row=4, column=0, padx=5, pady=5)

entry_square_footage = Entry(toolsframe,font=('times new romen',15,'bold'),bd=5,width=13)
entry_square_footage.grid(row=4, column=1, padx=10, pady=10)

label_meter_footage = Label(toolsframe, text="METER PER SQ :",font=('times new romen',15,'bold'),bg='thistle')
label_meter_footage.grid(row=5, column=0, padx=5, pady=5)

entry_meter_footage = Entry(toolsframe,font=('times new romen',15,'bold'),bd=5,width=13)
entry_meter_footage.grid(row=5, column=1, padx=10, pady=10)

daylabel_labour_footage = Label(toolsframe, text="NO OF DAYS :",font=('times new romen',15,'bold'),bg='thistle')
daylabel_labour_footage.grid(row=6, column=0, padx=5, pady=5)

dayentry_labour_footage = Entry(toolsframe,font=('times new romen',15,'bold'),bd=5,width=13)
dayentry_labour_footage.grid(row=6, column=1, padx=10, pady=20)
label_labour_footage = Label(toolsframe, text="NO OF LABOUR :",font=('times new romen',15,'bold'),bg='thistle')
label_labour_footage.grid(row=7, column=0, padx=5, pady=5)

entry_labour_footage = Entry(toolsframe,font=('times new romen',15,'bold'),bd=5,width=13)
entry_labour_footage.grid(row=7, column=1, padx=10, pady=20)



billframe=Frame(productframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)


billarealabel=Label(billframe,text="PRICE AREA",font=('times new romen',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
area=Text(billframe,width=63,height=30,yscrollcommand=scrollbar.set)
area.pack()
scrollbar.config(command=area.yview)





calculate_button = Button(toolsframe, text="Calculate Cost",font=('times new romen',15,'bold'),bg='thistle', command=calculate_cost)
calculate_button.grid(row=8, pady=10,padx=10)

result_label = Label(toolsframe, text="",bg='thistle')
result_label.grid(row=9, pady=10,padx=35, columnspan=3)

next_button = Button(toolsframe, text="NEXT",font=('times new romen',15,'bold'),bg='thistle', command=nextp)
next_button.grid(row=8,column=2, pady=10,padx=35)

root.mainloop()