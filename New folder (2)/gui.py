from tkinter import *
from PIL import ImageTk, Image

import t
import callfunction
#from tqdm import tqdm 
class MyWindow:
    data=[]
    def __init__(self, win):
        
        #replace data with values of list
        #self.img = ImageTk.PhotoImage(Image.open("hevo3.jpg"))
        #self.imglabel = Label(win, image=self.img).grid(row=1, column=1)
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        self.lab = Label( text="HevoValYou",font="-weight bold")
        self.lab.config(font=("Courier", 44))

        self.lb = Listbox(win,width=80, height=20, selectmode='multiple')
        data=[]
        for num in data:
            self.lb.insert(END,num)
        self.btn1 = Button(win, text='Select All')
        self.btn2 = Button(win, text='Search the web')
        self.lab.place(x=190, y=5)
        self.lb.place(x=150, y=90)
        self.b1=Button(win, text='Select All', command=self.selectall)
        self.b2=Button(win, text='Search the web', command=self.search)
        self.b3=Button(win, text='Load', command=self.load)
        self.b3.place(x=200, y=450)
        self.b1.place(x=350, y=450)
        self.b2.place(x=500, y=450)
    def selectall(self):
        callfunction.callfunction(self.data)
    def load(self):
        self.data=t.check()
        for num in self.data:
            self.lb.insert(END,num)
    def search(self):
        selection = self.lb.curselection()
        selection=list(selection)
        print(selection)
        l=[]
        for x in range(len(selection)):
            l.append(self.data[selection[x]])
        callfunction.callfunction(l)
        

window=Tk()
mywin=MyWindow(window)
window.title('HevoValYou')
window.geometry("800x500+10+10")
window.configure(bg="#000000")
window.mainloop()
