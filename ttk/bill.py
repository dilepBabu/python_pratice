from tkinter import *
from tkinter import messagebox
import random,os,tempfile

def clear():
    tapeentry.delete(0,END)
    testerentry.delete(0,END)
    screwdriversentry.delete(0,END)
    screwdriverentry.delete(0,END)
    wirestripperentry.delete(0,END)
    pilerentry.delete(0,END)

    junctionentry.delete(0,END)
    meterboardentry.delete(0,END)
    socketentry.delete(0,END)
    switchentry.delete(0,END)
    switchboardentry.delete(0,END)
    mcbentry.delete(0,END)


    reducerentry.delete(0,END)
    flexientry.delete(0,END)
    absentry.delete(0,END)
    copperentry.delete(0,END)
    pexentry.delete(0,END)
    pvcentry.delete(0,END)


    tapeentry.insert(0,0)
    testerentry.insert(0,0)
    screwdriversentry.insert(0,0)
    screwdriverentry.insert(0,0)
    wirestripperentry.insert(0,0)
    pilerentry.insert(0,0)

    junctionentry.insert(0,0)
    meterboardentry.insert(0,0)
    socketentry.insert(0,0)
    switchentry.insert(0,0)
    switchboardentry.insert(0,0)
    mcbentry.insert(0,0)


    reducerentry.insert(0,0)
    flexientry.insert(0,0)
    absentry.insert(0,0)
    copperentry.insert(0,0)
    pexentry.insert(0,0)
    pvcentry.insert(0,0)



    toolspriceentry.delete(0,END)
    electricpriceentry.delete(0,END)
    pipepriceentry.delete(0,END)

    toolstaxentry.delete(0,END)
    electrictaxentry.delete(0,END)
    pipetaxentry.delete(0,END)

    
    billnoentry.delete(0,END)

    area.delete(1.0,END)
    


def print_bill():
    if area.get(1.0,END)=='\n':
        messagebox.showerror("Error","Bill is empty")
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(area.get(1.0,END))
        os.startfile(file,'print')








def search():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnoentry.get():
            f=open(f'bills/{i}','r')  
            area.delete(1.0,END)
            for data in f:
                area.insert(END,data) 
            f.close() 
            break 
    else:
        
        messagebox.showerror('Error',"Invalid Bill number")
            





if not os.path.exists('bills'):
    os.mkdir('bills')

   

root=Tk()
root.title("PC CONSTRUCTION ")
root.geometry('1270x685')
heading=Label(root,text='PC CONSTRUCTION',font=('times new romen',30,'bold')
              ,bg='cyan2',bd=12,relief=RIDGE)
heading.pack(fill=X)



def save():
       global billno
       result=messagebox.askyesno('Comfirm','Do You Want Save The Bill?')
       if result:
              bill_content=area.get(1.0,END)
              file=open(f'bills/{billno}.txt','w')
              file.write(bill_content)
              file.close()
              messagebox.showinfo("sucesss",f'bill number:{billno} is saved sucessfully')
              billno=random.randint(500,1000)


billno=random.randint(500,1000)





def bill_area():
        global totalbill
     
        if toolspriceentry.get()=='' and electricpriceentry.get()=='' and pipepriceentry.get()=='':
          messagebox.showerror('Error','No Product are Selected')  
        elif toolspriceentry.get()=='0 Rs' and electricpriceentry.get()=='0 Rs' and pipepriceentry.get()=='0 Rs':
          messagebox.showerror('Error','No Product are Selected')  
        else:
            area.delete(1.0,END)
            area.insert(END,'\t\t   **PC CONSTRUCTION**\n')
            area.insert(END,f'\nBill Number: {billno}\n')
            area.insert(END,f'\n-------------------------------------------------')
            area.insert(END,'\nProduct\t\t\tQuantity\t\tPrice\n')
            area.insert(END,f'\n-------------------------------------------------')
            if wirestripperentry.get()!='0':
                area.insert(END,f'\nWire Stripper:\t\t\t{wirestripperentry.get()}\t\tRs{wirestrip}\n')
            if screwdriverentry.get()!='0':
                area.insert(END,f'\nScrewdriver:\t\t\t{screwdriverentry.get()}\t\tRs {screw}\n')
            if screwdriversentry.get()!='0':
                area.insert(END,f'\nTool Kit:\t\t\t{screwdriversentry.get()}\t\tRs {screws}\n')
            if testerentry.get()!='0':
                area.insert(END,f'\nTester:\t\t\t{testerentry.get()}\t\tRs {tester}\n')
            if pilerentry.get()!='0':
                area.insert(END,f'\nPiler:\t\t\t{pilerentry.get()}\t\tRs {piler}\n')
            if tapeentry.get()!='0':
                area.insert(END,f'\nTape Meter:\t\t\t{tapeentry.get()}\t\tRs {tape}\n')
            

            if switchboardentry.get()!='0':
                area.insert(END,f'\nSwitch Board:\t\t\t{switchboardentry.get()}\t\tRs {switchboard}\n')
            if switchentry.get()!='0':
                area.insert(END,f'\nSwitch:\t\t\t{switchentry.get()}\t\tRs {switch}\n')
            if socketentry.get()!='0':
                area.insert(END,f'\nSocket:\t\t\t{socketentry.get()}\t\tRs {socket}\n')

            if meterboardentry.get()!='0':
                area.insert(END,f'\nMeter Board:\t\t\t{meterboardentry.get()}\t\tRs {meter}\n')
            if junctionentry.get()!='0':
                area.insert(END,f'\nJunction Box:\t\t\t{junctionentry.get()}\t\tRs {junction}\n')
            if mcbentry.get()!='0':
                area.insert(END,f'\nMCB:\t\t\t{mcbentry.get()}\t\tRs {mcb}\n')
            if copperentry.get()!='0':
                area.insert(END,f'\nCoupler 50mm:\t\t\t{copperentry.get()}\t\tRs {copper}\n')
            if absentry.get()!='0':
                area.insert(END,f'\nBend 75mm:\t\t\t{absentry.get()}\t\tRs {abs}\n')
            if pvcentry.get()!='0':
                area.insert(END,f'\nPVC Pipe 1M:\t\t\t{pvcentry.get()}\t\tRs {pvc}\n')
            if pexentry.get()!='0':
                area.insert(END,f'\nCross Tee:\t\t\t{pexentry.get()}\t\tRs {pex}\n')
            if flexientry.get()!='0':
                area.insert(END,f'\nClamp 4Inch:\t\t\t{flexientry.get()}\t\tRs {flexi}\n')
            if reducerentry.get()!='0':
                    area.insert(END,f'\nReducer:\t\t\t{reducerentry.get()}\t\tRs {reduce}\n')
                
                
            area.insert(END,f'\n-------------------------------------------------\n')

            if toolstaxentry.get()!='0.0':
                area.insert(END,f'\nTools Tax:\t\t{toolstaxentry.get()}\n')

            if electrictaxentry.get()!='0.0':
                area.insert(END,f'\nElectric Tax:\t\t{electrictaxentry.get()}\n')
            if pipetaxentry.get()!='0.0':
                area.insert(END,f'\nPipe Tax:\t\t{pipetaxentry.get()}\n')
            area.insert(END,f'\n-------------------------------------------------')
            area.insert(END,f'\nTotal=\t\t\t\t Rs {totalbill}')
            area.insert(END,f'\n-------------------------------------------------')
            save()

def total():
        global wirestrip
        global screw
        global screws
        global tester
        global piler
        global tape,totalbill
        global totaltoolsprice
        global toolstax
        global pvc,pex,switchboard,switch,socket,meter,junction,mcb,totalelectricprice,totalpipeprice,copper,abs,reduce,flexi,pipetax
        #toolsprice
        wirestrip=int(wirestripperentry.get())*300
        screw=int(screwdriverentry.get())*270
        screws=int(screwdriversentry.get())*3000
        tester=int(testerentry.get())*180
        piler=int(pilerentry.get())*300
        tape=int(tapeentry.get())*500
        totaltoolsprice=wirestrip+screw+screws+tester+piler+tape
        toolspriceentry.delete(0,END)
        toolspriceentry.insert(0,f'{totaltoolsprice} Rs')
        toolstax=totaltoolsprice*0.12
        toolstaxentry.delete(0,END)
        toolstaxentry.insert(0,f'{toolstax} %')

    #electricprice
        switchboard=int(switchboardentry.get())*250
        switch=int(switchentry.get())*40
        socket=int(socketentry.get())*170
        meter=int(meterboardentry.get())*5000
        junction=int(junctionentry.get())*2050
        mcb=int(mcbentry.get())*200
        totalelectricprice=switchboard+switch+socket+meter+junction+mcb
        electricpriceentry.delete(0,END)
        electricpriceentry.insert(0,f'{totalelectricprice} Rs')
        electrictax=totalelectricprice*0.20
        electrictaxentry.delete(0,END)
        electrictaxentry.insert(0,f'{electrictax} %' )

    #pipeprice
        pvc=int(pvcentry.get())*150
        pex=int(pexentry.get())*80
        copper=int(copperentry.get())*200
        abs=int(absentry.get())*105
        reduce=int(reducerentry.get())*500
        flexi=int(flexientry.get())*200
        totalpipeprice=pvc+pex+copper+abs+reduce+flexi
        pipepriceentry.delete(0,END)
        pipepriceentry.insert(0,f'{totalpipeprice} Rs')
        pipetax=totalpipeprice*0.18
        pipetaxentry.delete(0,END)
        pipetaxentry.insert(0,f'{pipetax} %')
        totalbill=totalelectricprice+totalpipeprice+totaltoolsprice+pipetax+electrictax+toolstax


def window():
  
    global billnolabel
    global billnoentry
    global wirestripperlabel
    global wirestripperentry
    global screwdriverlabel
    global screwdriverentry
    global screwdriverslabel
    global screwdriversentry
    global testerlabel
    global testerentry
    global pilerlabel
    global pilerentry
    global tapelabel
    global tapeentry
    global switchboardlabel
    global switchboardentry
    global switchlabel
    global switchentry
    global socketlabel
    global socketentry
    global meterboardlabel
    global meterboardentry
    global mcblabel
    global mcbentry
    global junctionlabel
    global junctionentry
    global pvclabel
    global pvcentry
    global pexlabel
    global pexentry
    global copperlabel
    global copperentry
    global abslabel
    global absentry
    global flexilabel
    global flexientry
    global reducerlabel
    global reducerentry
    global toolspricelabel
    global toolspriceentry
    global electricpricelabel
    global electricpriceentry
    global pipepricelabel
    global pipepriceentry
    global toolstaxlabel
    global toolstaxentry
    global electrictaxlabel
    global electrictaxentry
    global pipetaxlabel
    global pipetaxentry
    global area

    customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new romen',15,'bold')
                                    ,bg='azure2',bd=8,relief=GROOVE)
    customer_details_frame.pack(fill=X)

    
    billnolabel=Label(customer_details_frame,text='Bill Number',font=('times new romen',15,'bold'),bg='azure2')
    billnolabel.grid(row=0,column=4,padx=20,pady=2)
    billnoentry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
    billnoentry.grid(row=0,column=5,padx=8)
    searchbutton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=7,command=search)
    searchbutton.grid(row=0,column=6,padx=20,pady=8)

    productframe=Frame(root)
    productframe.pack()

    toolsframe=LabelFrame(productframe,text="Tools",font=('times new romen',15,'bold')
                                    ,bg='thistle',bd=8,relief=GROOVE)
    toolsframe.grid(row=0,column=0)


    wirestripperlabel=Label(toolsframe,text="Wire Stripper",font=('times new romen',15,'bold'),bg='thistle')
    wirestripperlabel.grid(row=0,column=0,pady=8)
    wirestripperentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    wirestripperentry.grid(row=0,column=1)
    wirestripperentry.insert(0,0)

    screwdriverlabel=Label(toolsframe,text="Screwdriver Set",font=('times new romen',15,'bold'),bg='thistle')
    screwdriverlabel.grid(row=1,column=0,pady=8)
    screwdriverentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    screwdriverentry.grid(row=1,column=1)
    screwdriverentry.insert(0,0)


    screwdriverslabel=Label(toolsframe,text="Tool Kit",font=('times new romen',15,'bold'),bg='thistle')
    screwdriverslabel.grid(row=2,column=0,pady=8)
    screwdriversentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    screwdriversentry.grid(row=2,column=1)
    screwdriversentry.insert(0,0)


    testerlabel=Label(toolsframe,text="Tester",font=('times new romen',15,'bold'),bg='thistle')
    testerlabel.grid(row=3,column=0,pady=8)
    testerentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    testerentry.grid(row=3,column=1)
    testerentry.insert(0,0)


    pilerlabel=Label(toolsframe,text="Piler",font=('times new romen',15,'bold'),bg='thistle')
    pilerlabel.grid(row=4,column=0,pady=8)
    pilerentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    pilerentry.grid(row=4,column=1)
    pilerentry.insert(0,0)

    tapelabel=Label(toolsframe,text="Tape Measure",font=('times new romen',15,'bold'),bg='thistle')
    tapelabel.grid(row=5,column=0,pady=8)
    tapeentry=Entry(toolsframe,font=('times new romen',15,'bold'),width=10,bd=5)
    tapeentry.grid(row=5,column=1)
    tapeentry.insert(0,0)


    electricframe=LabelFrame(productframe,text="Electric Tools",font=('times new romen',15,'bold')
                                    ,bg='thistle',bd=8,relief=GROOVE)
    electricframe.grid(row=0,column=1)


    switchboardlabel=Label(electricframe,text="Switch Board",font=('times new romen',15,'bold'),bg='thistle')
    switchboardlabel.grid(row=0,column=0,pady=8)
    switchboardentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    switchboardentry.grid(row=0,column=1)
    switchboardentry.insert(0,0)


    switchlabel=Label(electricframe,text="Switch",font=('times new romen',15,'bold'),bg='thistle')
    switchlabel.grid(row=1,column=0,pady=8)
    switchentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    switchentry.grid(row=1,column=1)
    switchentry.insert(0,0)


    socketlabel=Label(electricframe,text="Pin Socket",font=('times new romen',15,'bold'),bg='thistle')
    socketlabel.grid(row=2,column=0,pady=8)
    socketentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    socketentry.grid(row=2,column=1)
    socketentry.insert(0,0)


    meterboardlabel=Label(electricframe,text="Meter Board",font=('times new romen',15,'bold'),bg='thistle')
    meterboardlabel.grid(row=3,column=0,pady=8)
    meterboardentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    meterboardentry.grid(row=3,column=1)
    meterboardentry.insert(0,0)


    junctionlabel=Label(electricframe,text="Junction Box",font=('times new romen',15,'bold'),bg='thistle')
    junctionlabel.grid(row=4,column=0,pady=8)
    junctionentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    junctionentry.grid(row=4,column=1)
    junctionentry.insert(0,0)


    mcblabel=Label(electricframe,text="MCB",font=('times new romen',15,'bold'),bg='thistle')
    mcblabel.grid(row=5,column=0,pady=8)
    mcbentry=Entry(electricframe,font=('times new romen',15,'bold'),width=10,bd=5)
    mcbentry.grid(row=5,column=1)
    mcbentry.insert(0,0)


    pipeframe=LabelFrame(productframe,text="Pipe",font=('times new romen',15,'bold')
                                    ,bg='thistle',bd=8,relief=GROOVE)
    pipeframe.grid(row=0,column=2)


    pvclabel=Label(pipeframe,text="PVC Pipe 1M",font=('times new romen',15,'bold'),bg='thistle')
    pvclabel.grid(row=0,column=0,pady=8)
    pvcentry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    pvcentry.grid(row=0,column=1)
    pvcentry.insert(0,0)


    pexlabel=Label(pipeframe,text="Cross Tee",font=('times new romen',15,'bold'),bg='thistle')
    pexlabel.grid(row=1,column=0,pady=8)
    pexentry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    pexentry.grid(row=1,column=1)
    pexentry.insert(0,0)


    copperlabel=Label(pipeframe,text="Coupler 50mm",font=('times new romen',15,'bold'),bg='thistle')
    copperlabel.grid(row=2,column=0,pady=8)
    copperentry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    copperentry.grid(row=2,column=1)
    copperentry.insert(0,0)


    abslabel=Label(pipeframe,text="Bend 75mm",font=('times new romen',15,'bold'),bg='thistle')
    abslabel.grid(row=3,column=0,pady=8)
    absentry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    absentry.grid(row=3,column=1)
    absentry.insert(0,0)


    flexilabel=Label(pipeframe,text="Clamp 4Inch",font=('times new romen',15,'bold'),bg='thistle')
    flexilabel.grid(row=4,column=0,pady=8)
    flexientry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    flexientry.grid(row=4,column=1)
    flexientry.insert(0,0)


    reducerlabel=Label(pipeframe,text="Reducer",font=('times new romen',15,'bold'),bg='thistle')
    reducerlabel.grid(row=5,column=0,pady=8)
    reducerentry=Entry(pipeframe,font=('times new romen',15,'bold'),width=10,bd=5)
    reducerentry.grid(row=5,column=1)
    reducerentry.insert(0,0)


    billframe=Frame(productframe,bd=8,relief=GROOVE)
    billframe.grid(row=0,column=3)


    billarealabel=Label(billframe,text="PRICE AREA",font=('times new romen',15,'bold'),bd=7,relief=GROOVE)
    billarealabel.pack(fill=X)

    scrollbar=Scrollbar(billframe,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    area=Text(billframe,width=49,height=16,yscrollcommand=scrollbar.set)
    area.pack()
    scrollbar.config(command=area.yview)


    billmenuframe=LabelFrame(root,text='Bill Menu',font=('times new romen',15,'bold')
                                    ,bg='azure2',bd=8,relief=GROOVE)
    billmenuframe.pack()


    toolspricelabel=Label(billmenuframe,text="Tools Price:",font=('times new romen',15,'bold'),bg='thistle')
    toolspricelabel.grid(row=0,column=0,pady=10,padx=10)
    toolspriceentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    toolspriceentry.grid(row=0,column=1,padx=10)


    electricpricelabel=Label(billmenuframe,text="Electric Price:",font=('times new romen',15,'bold'),bg='thistle')
    electricpricelabel.grid(row=1,column=0,pady=10,padx=10)
    electricpriceentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    electricpriceentry.grid(row=1,column=1,padx=10)


    pipepricelabel=Label(billmenuframe,text="Pipe Price:",font=('times new romen',15,'bold'),bg='thistle')
    pipepricelabel.grid(row=2,column=0,pady=10,padx=10)
    pipepriceentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    pipepriceentry.grid(row=2,column=1,padx=10)



    toolstaxlabel=Label(billmenuframe,text="Tools Tax:",font=('times new romen',15,'bold'),bg='thistle')
    toolstaxlabel.grid(row=0,column=2,pady=10,padx=10)
    toolstaxentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    toolstaxentry.grid(row=0,column=3,padx=10)


    electrictaxlabel=Label(billmenuframe,text="Electric Tax:",font=('times new romen',15,'bold'),bg='thistle')
    electrictaxlabel.grid(row=1,column=2,pady=10,padx=10)
    electrictaxentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    electrictaxentry.grid(row=1,column=3,padx=10)


    pipetaxlabel=Label(billmenuframe,text="Pipe Tax:",font=('times new romen',15,'bold'),bg='thistle')
    pipetaxlabel.grid(row=2,column=2,pady=10,padx=10)
    pipetaxentry=Entry(billmenuframe,font=('times new romen',15,'bold'),width=10,bd=5)
    pipetaxentry.grid(row=2,column=3,padx=10)


    buttonframe=Frame(billmenuframe,bd=8,relief=GROOVE)
    buttonframe.grid(row=0,column=4,rowspan=4)


    Total_button=Button(buttonframe,text="Total",font=('arial',16,'bold'),bg='thistle3',bd=5,width=9,command=total)
    Total_button.grid(row=0,column=0,pady=4,padx=15)

    bill=Button(buttonframe,text="Bill",font=('arial',16,'bold'),bg='thistle3',bd=5,width=9,command=bill_area)
    bill.grid(row=0,column=1,padx=15,pady=4)

    print=Button(buttonframe,text="Print",font=('arial',16,'bold'),bg='thistle3',bd=5,width=9,command=print_bill)
    print.grid(row=0,column=3,padx=15,pady=4)

    clears=Button(buttonframe,text="Clear",font=('arial',16,'bold'),bg='thistle3',bd=5,width=9,command=clear)
    clears.grid(row=0,column=4,padx=15,pady=4)
window()

root.mainloop()