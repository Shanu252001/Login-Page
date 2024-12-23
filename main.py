import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameentry.get()=="Shanu" and pwdentry.get()=="1234":
        messagebox.showinfo("Success","Login Successfull")
        root.destroy()
        import sms
    elif usernameentry.get()=="Shanu" and pwdentry.get()!="1234":
        messagebox.showerror("Error","Password is incorrect ")
    elif usernameentry.get()!="Shanu" and pwdentry.get()=="1234":
        messagebox.showerror("Error", "Username is incorrect ")
    else:
            messagebox.showerror("Error","Enter correct Credentials")

root=Tk()
root.title("Student System Management Login Page")
root.geometry("1500x780+0+0")
root.resizable(False,False)
bgimage=ImageTk.PhotoImage(file="redforest.jpg")
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)
#Login frame
loginframe=Frame(root,bg="gold",borderwidth=5)
loginframe.place(x=550,y=150)
logo=ImageTk.PhotoImage(file="avatar.jpg")
#Login label
logolabel=Label(loginframe,image=logo)
logolabel.grid(row=0,column=0,pady=20,columnspan=2)

#username label and entry
usernamepic=ImageTk.PhotoImage(file="username.jpg")
usernamelabel=Label(loginframe,image=usernamepic,text="Username",font=("arial",15),compound=LEFT,bg="gold",fg="black")
usernamelabel.grid(row=1,column=0,padx=10,pady=10)

usernameentry=Entry(loginframe,font=("arial",15,"bold"),width=15,fg="darkblue",bd=3)
usernameentry.grid(row=1,column=1,padx=10,pady=10)

#password label and entry
passwordpic=ImageTk.PhotoImage(file="password.jpg")
pwdlabel=Label(loginframe,image=passwordpic,text="Password",font=("arial",15),compound=LEFT,bg="gold",fg="black")
pwdlabel.grid(row=2,column=0,padx=10,pady=10)

pwdentry=Entry(loginframe,font=("arial",15,"bold"),width=15,fg="darkblue",bd=3)
pwdentry.grid(row=2,column=1,padx=10,pady=10)

#login button
loginbutton=Button(loginframe,width=7,height=1,font=("arial",20),text="Login",bg="deepskyblue",bd=3,cursor="hand2",activebackground="orange",command=login)
loginbutton.grid(row=3,column=0,pady=30,columnspan=2)


root.mainloop()