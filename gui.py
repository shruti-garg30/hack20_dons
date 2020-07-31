from tkinter import *
class MyWindow:
    def __init__(self, win):
        #replace data with values of list
        self.lb = Listbox(win, height=5, selectmode='multiple')
        data=("abc.com","xyz.com")
        for num in data:
            self.lb.insert(END,num)
        self.btn1 = Button(win, text='Search the web')
        self.lb.place(x=100, y=50)
        self.b1=Button(win, text='Search the web', command=self.search)
        self.b1.place(x=100, y=150)
    def search(self):
        webbrowser.open_next_tab("https://google.com")
        #oshi add function here
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
