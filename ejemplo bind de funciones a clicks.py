from tkinter import *


class Botones:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printButton= Button(frame,text=" Print message",command=self.printmessage)
        self.printButton.pack(side=LEFT)
        self.quickbutton= Button(frame,text=" Quit",command=frame.quit)
        self.quickbutton.pack(side=LEFT)
    def printmessage(self):
        print("wow actually works")
        

root= Tk()
objeto= Botones(root)


root.mainloop()
