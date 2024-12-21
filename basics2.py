from tkinter import *

root=Tk()
root.geometry('200x200')
root.title("Login Form")

#Label

userlabel=Label(root,text="Username").place(x=40,y=60)

userEntry=Entry(root,width=30).place(x=100,y=60)

userlabel2=Label(root,text="Password").place(x=40,y=110)

userEntry2=Entry(root,width=30).place(x=100,y=110)

btn = Button(root,text='login',bd=5,background='orange',command=root.destroy)

btn.place(x=100,y= 135)







root.mainloop()