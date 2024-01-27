from tkinter import *
from tkinter import messagebox
def clear(*entries):
 for entry in entries:
   entry.delete(0, END)
def validate_and_move():
 # Validation code...
 # Assuming the validation is successful and you want to open the details window
 win.withdraw() # Hide the main window
 details_window()
def details_window():
    if not all(entry.get() for entry in (box1, box2, box3, box4, box5)): messagebox.showwarning("Missing Information", "Please fill all details to get the budget.")
    return
w = Tk()
w.title("Next Window")
w['background'] = '#F0F0FF'
w.maxsize(550, 650)
w.minsize(550, 650)
c1 = '#F0F0FF'
txt = "time 14 bold"
top = Frame(w, bg="#3AAFA9", width=2000, height=230)
top.place(x=0, y=-90)
sep3= Frame(w, bg='black', width=2000, height=0.3)
sep3.place(x=0, y=0)
sep3= Frame(w, bg='black', width=2000, height=0.3)
sep3.place(x=0, y=140)
sep1= Frame(w, bg='black', width=0.3, height=600)
sep1.place(x=0, y=0)
sep1= Frame(w, bg='black', width=0.3, height=600)
sep1.place(x=1499, y=0)
sep = Frame(w, bg='black', width=0.3, height=460)
sep.place(x=730, y=140)
sep1= Frame(w, bg='black', width=0.3, height=460)
sep1.place(x=1080, y=140)
sep2= Frame(w, bg='black', width=2000, height=0.3)
sep2.place(x=0, y=600)
sep3= Frame(w, bg='black', width=2000, height=0.3)
sep3.place(x=0, y=230)
 # Rest of the details window code... Done
l=Label(w,text="PS CONSTRUCTIONS",bg="#3AAFA9",font=('Impact',70)).place(x=450,y=13)
l=Label(w,text="DETAILS",bg=c1,font=('Impact',25)).place(x=300,y=160)
l1=Label(w,text="BRICKS REQUIRED(IN NO.OF)",bg=c1,font=(txt,25)).place(x=100,y=250)
l2=Label(w,text="CEMENT REQUIRED(IN KG)",bg=c1,font=(txt,25)).place(x=100,y=320)
l3=Label(w,text="IRON BAR REQUIRED(IN NO.OF)",bg=c1,font=(txt,25)).place(x=100,y=390)
l4=Label(w,text="AGGREGATE REQUIRED(IN KG)",bg=c1,font=(txt,25)).place(x=100,y=460)
l5=Label(w,text="SAND REQUIRED(IN NO.OF)",bg=c1,font=(txt,25)).place(x=100,y=530)
l6=Label(w,text="AMOUNT OF MATERIAL",bg=c1,font=('Impact',25)).place(x=768,y=160)
l6=Label(w,text="MATERIALS PRICE",bg=c1,font=('Impact',25)).place(x=1172,y=160)
'''ln=Entry(w).place(x=680,y=200)
 ln1=Entry(w).place(x=680,y=250)
 ln2=Entry(w).place(x=680,y=300)
 ln3=Entry(w).place(x=680,y=350)
 ln4=Entry(w).place(x=680,y=400)
 ln=Entry(w).place(x=920,y=200)
 ln1=Entry(w).place(x=920,y=250)
 ln2=Entry(w).place(x=920,y=300)
 ln3=Entry(w).place(x=920,y=350)
 ln4=Entry(w).place(x=920,y=400)
 ln4=Entry(w).place(x=920,y=450)'''
 #sep=ttk.Seperator(w,orient='vertical').place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
l6=Label(w,text="TOTAL PRICE =",bg=c1,font=(txt,25)).place(x=800,y=620)
back = Button(w, text="BACK", bg="#FF4040", font=(txt, 18), 
command=lambda: back_to_main(w))
back.place(x=700, y=710)
w.mainloop()
def back_to_main(details_window):
  details_window.destroy() # Close the details window
  win.deiconify() # Show the main window again
win = Tk()
win.title("Construction Budget for Home")
win['background'] = '#F0F0FF'
win.maxsize(550, 650)
win.minsize(500, 650)
# Rest of the main window code...
cb="#3AAFA9"
cb2='#F0F0FF'
LF="Courier"
RF="Arial 24"
top=Frame(win,bg=cb,width=1560,height=230).place(x=0,y=-90)
sep3= Frame(win, bg='black', width=2000, height=0.3)
sep3.place(x=0, y=0)
sep3= Frame(win, bg='black', width=2000, height=0.3)
sep3.place(x=0, y=140)
l=Label(win,text="PS CONSTRUCTIONS",bg=cb,font=('Impact',70)).place(x=450,y=13)
l1=Label(win,text="NAME",bg=cb2,font=(LF,25))
l1.place(x=400,y=190)
box1=Entry(win,width=18,font=('Arial 24'))
box1.place(x=670,y=190)
l2=Label(win,text="ADDRESS",bg=cb2,font=(LF,25))
l2.place(x=400,y=240)
box2=Entry(win,width=18,font=('Arial 24'))
box2.place(x=670,y=240)
l3=Label(win,text="PHONE NUMBER",bg=cb2,font=(LF,25))
l3.place(x=400,y=290)
box3=Entry(win,width=18,font=('Arial 24'))
box3.place(x=670,y=290)
l4=Label(win,text="EMAIL",bg=cb2,font=(LF,25))
l4.place(x=400,y=340)
box4=Entry(win,width=18,font=('Arial 24'))
box4.place(x=670,y=340)
l5=Label(win,text="AREA OF LAND",bg=cb2,font=(LF,25))
l5.place(x=400,y=390)
op=StringVar(win,)
op.set("CHOOSE")
menu=OptionMenu(win,op,"FEET","METER")
menu.place(x=670,y=393)
box5=Entry(win,text='in m',width=7,font=('Arial 24'))
box5.place(x=770,y=390)
l6=Label(win,text="BHK",bg=cb2,font=(LF,25))
l6.place(x=400,y=440)
cr="#CACAFF"
vl=IntVar()
l7=Radiobutton(win,bg=cb2,text="1BHK",variable=vl,value=1,font=(RF,10))
l7.place(x=670,y=440)
l7=Radiobutton(win,bg=cb2,text="2BHK",variable=vl,value=2,font=(RF,10))
l7.place(x=740,y=440)
l7=Radiobutton(win,bg=cb2,text="3BHK",variable=vl,value=3,font=(RF,10))
l7.place(x=670,y=490)
l7=Radiobutton(win,bg=cb2,text="4BHK",variable=vl,value=4,font=(RF,10))
l7.place(x=740,y=490)
l7=Label(win,text="PARKING AREA",bg=cb2,font=(LF,25))
l7.place(x=400,y=540)
vp=IntVar()
l9=Radiobutton(win,bg=cb2,text="WITH",variable=vp,value=1,font=(RF,10))
l9.place(x=670,y=540) 
l9=Radiobutton(win,bg=cb2,text="WITHOUT",variable=vp,value=2,font=(RF,10))
l9.place(x=740,y=540)
l8=Label(win,text="NO.OF.FLOORS",bg=cb2,font=(LF,25))
l8.place(x=400,y=590)
listroom=StringVar(win)
listroom.set("CHOOSE")
menu=OptionMenu(win,listroom,"1","2","3")
menu.place(x=670,y=590)
clear1 = Button(win, text="CLEAR", bg="#FF4040", width=15, pady=10, 
command=lambda: clear(box1, box2, box3, box4, box5))
clear1.place(x=700, y=680)
submit = Button(win, text="SUBMIT", bg="#66CD00", width=15, pady=10, 
command=validate_and_move)
submit.place(x=850, y=680)
win.mainloop()