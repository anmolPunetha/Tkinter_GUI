from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("400x300")
root.title('Team Kalpana: Energy Calculation')
root.iconbitmap('KALPANA.ico')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

box_1=StringVar()#intvar
box_2=StringVar()
box_3=StringVar()
box_4=StringVar()
box_5=StringVar()
box_6=StringVar()
box_7=StringVar()

def calculate():
    total_power = float(box_2.get()) * float(box_3.get()) * ((
                (2 * float(box_4.get())) + (0.03 * float(box_5.get())) + (1 * float(box_5.get())))/100)
    box_7.set('So, the total Energy used be  '+box_1.get()+' will be '+str(total_power)+' mW-hr')



a=Entry(mainframe,width=11,textvariable=box_1)
a.grid(row=1,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the component\'s name').grid(row=1,column=2,sticky=W)


b=Entry(mainframe,width=11,textvariable=box_2)
b.grid(row=2,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the current in mA ').grid(row=2,column=2,sticky=W)

c=Entry(mainframe,width=11,textvariable=box_3)
c.grid(row=3,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the voltage in V').grid(row=3,column=2,sticky=W)

d=Entry(mainframe,width=11,textvariable=box_4)
d.grid(row=4,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the duty cycle in Pre-launch').grid(row=4,column=2,sticky=W)

e=Entry(mainframe,width=11,textvariable=box_5)
e.grid(row=5,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the duty cycle in Post-launch').grid(row=5,column=2,sticky=W)

f=Entry(mainframe,width=11,textvariable=box_6)
f.grid(row=6,column=3,sticky=W)
ttk.Label(mainframe,text='Enter the duty cycle in Recovery').grid(row=6,column=2,sticky=W)

ttk.Label(mainframe,textvariable=box_7).grid(row=7,column=2,sticky=W)

ttk.Button(mainframe, text="Calculate",command=calculate).grid(row=8, column=2)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

mainloop()