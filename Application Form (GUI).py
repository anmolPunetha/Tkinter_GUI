from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
root=Tk()
root.geometry("600x400")
root.title('iot4beginners')
root.iconbitmap('logo.ico')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

box_1=StringVar() #name
box_2=StringVar() #age
box_3=StringVar() #father's name
box_4=StringVar() #class
box_5=StringVar() #school
box_6=StringVar() #city
box_7=StringVar() #pincode
r= IntVar()

def check():
    val_1 = "Name: "+box_1.get()+"\n"
    val_2 = "Age: "+box_2.get()+"\n"
    val_3 = "Father\'s Name: "+box_3.get()+"\n"
    val_4 = "Class/Semester: "+box_4.get()+"\n"
    val_5 = "School/College: "+box_5.get()+"\n"
    val_6 = "City: "+box_6.get()+"\n"
    val_7 = "Pincode: "+box_7.get()
    file = asksaveasfile(defaultextension='.yaml')
    file.write(val_1)
    file.write(val_2)
    file.write(val_3)
    file.write(val_4)
    file.write(val_5)
    file.write(val_6)
    file.write(val_7)

def radCall():
    select=r.get()
    if select==1:
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        a = Entry(mainframe, width=21, textvariable=box_1)
        a.grid(row=1, column=3)
        a.focus()

    if select==2:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        b = Entry(mainframe, width=21, textvariable=box_2)
        b.grid(row=2, column=3)
        b.focus()

    if select==3:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        c_ = Entry(mainframe, width=21, textvariable=box_3)
        c_.grid(row=3, column=3)
        c_.focus()

    if select==4:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        d = Entry(mainframe, width=21, textvariable=box_4)
        d.grid(row=4, column=3)
        d.focus()

    if select==5:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        e = Entry(mainframe, width=21, textvariable=box_5)
        e.grid(row=5, column=3)
        e.focus()

    if select==6:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        c = Entry(mainframe, width=21, textvariable=box_7, state=DISABLED).grid(row=7, column=3)
        f = Entry(mainframe, width=21, textvariable=box_6)
        f.grid(row=6, column=3)
        f.focus()

    if select==7:
        c = Entry(mainframe, width=21, textvariable=box_1, state=DISABLED).grid(row=1, column=3)
        c = Entry(mainframe, width=21, textvariable=box_3, state=DISABLED).grid(row=3, column=3)
        c = Entry(mainframe, width=21, textvariable=box_4, state=DISABLED).grid(row=4, column=3)
        c = Entry(mainframe, width=21, textvariable=box_5, state=DISABLED).grid(row=5, column=3)
        c = Entry(mainframe, width=21, textvariable=box_6, state=DISABLED).grid(row=6, column=3)
        c = Entry(mainframe, width=21, textvariable=box_2, state=DISABLED).grid(row=2, column=3)
        g = Entry(mainframe, width=21, textvariable=box_7)
        g.grid(row=7, column=3)
        g.focus()


ttk.Radiobutton(mainframe,variable=r,value=1,command=radCall).grid(row=1,column=1)
ttk.Radiobutton(mainframe,variable=r,value=2,command=radCall).grid(row=2,column=1)
ttk.Radiobutton(mainframe,variable=r,value=3,command=radCall).grid(row=3,column=1)
ttk.Radiobutton(mainframe,variable=r,value=4,command=radCall).grid(row=4,column=1)
ttk.Radiobutton(mainframe,variable=r,value=5,command=radCall).grid(row=5,column=1)
ttk.Radiobutton(mainframe,variable=r,value=6,command=radCall).grid(row=6,column=1)
ttk.Radiobutton(mainframe,variable=r,value=7,command=radCall).grid(row=7,column=1)



a=Entry(mainframe,width=21,textvariable=box_1)
a.grid(row=1,column=3)
ttk.Label(mainframe,text='Full Name').grid(row=1,column=2,sticky=W)

b=Entry(mainframe,width=21,textvariable=box_2)
b.grid(row=2,column=3)
ttk.Label(mainframe,text='Age').grid(row=2,column=2,sticky=W)


c=Entry(mainframe,width=21,textvariable=box_3)
c.grid(row=3,column=3)
ttk.Label(mainframe,text='Father\'s Name',).grid(row=3,column=2,sticky=W)


d=Entry(mainframe,width=21,textvariable=box_4)
d.grid(row=4,column=3)
ttk.Label(mainframe,text='Current Grade/Semester').grid(row=4,column=2,sticky=W)

e=Entry(mainframe,width=21,textvariable=box_5)
e.grid(row=5,column=3)
ttk.Label(mainframe,text='School/College').grid(row=5,column=2,sticky=W)


f=Entry(mainframe,width=21,textvariable=box_6)
f.grid(row=6,column=3)
ttk.Label(mainframe,text='Current Residential City').grid(row=6,column=2,sticky=W)


g=Entry(mainframe,width=21,textvariable=box_7)
g.grid(row=7,column=3)
ttk.Label(mainframe,text='Pincode').grid(row=7,column=2,sticky=W)


ttk.Button(mainframe, text="Save as",command=check).grid(row=8, column=3)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

mainloop()