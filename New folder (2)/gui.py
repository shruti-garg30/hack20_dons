from tkinter import *
from PIL import ImageTk, Image

import t
import callfunction
#from tqdm import tqdm 
class MyWindow:
    data=[]
    def __init__(self, win):
        
        #replace data with values of list
        ima=Image.open('hevo1.png')
        pho=ImageTk.PhotoImage(ima)
        i4=Label(win,bg='black')
        i4.config(image=pho)
        i4.img=pho
        i4.place(x=150,y=5)
        #canvas.create_image(20,20, anchor=NW, image=img)
        self.lab = Label( text="HevoValYou",font="-weight bold")
        self.lab.config(font=("Courier", 48))
        self.lab.config(fg='white')
        self.lab.config(bg='black')
        self.lb = Listbox(win,width=80, height=20, selectmode='multiple')
        data=[]
        for num in data:
            self.lb.insert(END,num)
        self.btn1 = Button(win, text='Select All')
        self.btn2 = Button(win, text='Search the web')
        self.lab.place(x=250, y=5)
        self.lb.place(x=150, y=100)  
        self.b1=Button(win, text='    Select All    ',command=self.selectall)
        self.b2=Button(win, text='Search the Web', command=self.search)
        self.b3=Button(win, text='      Load        ', command=self.load)
        self.b3.place(x=200, y=450)
        self.b1.place(x=350, y=450)
        self.b2.place(x=500, y=450)
    def selectall(self):
        callfunction.callfunction(self.data)
    def load(self):
        self.data=[]
        self.lb.delete(0,'end')
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
p1 = PhotoImage(file = 'hevo1.png')
window.iconphoto(False, p1) 
window.mainloop()
