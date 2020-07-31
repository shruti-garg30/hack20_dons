from tkinter import *
import t
import callfunction
from tqdm import tqdm 
class MyWindow:
    data=[]
    def __init__(self, win):
        
        #replace data with values of list
        self.lb = Listbox(win,width=80, height=20, selectmode='multiple')
        data=[]
        for num in data:
            self.lb.insert(END,num)
        self.btn1 = Button(win, text='Select All')
        self.btn2 = Button(win, text='Search the web')
        self.lb.place(x=150, y=70)
        self.b1=Button(win, text='Select All', command=self.selectall)
        self.b2=Button(win, text='Search the web', command=self.search)
        self.b3=Button(win, text='Load', command=self.load)
        self.b3.place(x=200, y=400)
        self.b1.place(x=350, y=400)
        self.b2.place(x=500, y=400)
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
window.mainloop()
