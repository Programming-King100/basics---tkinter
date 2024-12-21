from tkinter import *

#create a window

root=Tk()

root.geometry('200x200')

def display():
    print("Hello UcheKing150!")

#create a button

btn=Button(root,text='clickme',bd='5',background='teal',command=root.destroy)

btn.pack(side='top')

btn2=Button(root,text='Bruh',bd='5',background='red',command=display)

btn2.pack(side='bottom')


root.mainloop()