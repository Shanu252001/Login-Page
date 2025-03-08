import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def submit():
    if usernameentry.get()=="Shanu" and passwordentry.get()=="1234":
        messagebox.showinfo("Success","Login Successful")
        root.destroy()
        import main
    elif usernameentry.get()!="Shanu" and passwordentry.get()=="1234":
        messagebox.showerror("Error", "Enter Valid username")
    elif usernameentry.get()=="Shanu" and passwordentry.get()!="1234":
        messagebox.showerror("Error", "Enter Valid password")
    else:
        messagebox.showerror("Error","Enter Valid Credentials")


if __name__=="__main__":
    root=tkinter.Tk()
    root.title("Login Page")
    root.geometry("1500x770+0+0")
    root.resizable(False,False)
    bgimage=ImageTk.PhotoImage(file="redforest.jpg")
    bglabel=Label(root,image=bgimage).place(x=0,y=0)
    loginframe=Frame(root,height=500,width=420,bg="orange")
    loginframe.place(x=580,y=150)
    loginimage=ImageTk.PhotoImage(file="students.png")
    loginimglabel=Label(loginframe,image=loginimage)
    loginimglabel.place(x=150,y=20)

    usernamepic=ImageTk.PhotoImage(file="username.jpg")
    usernamelabel=Label(loginframe,image=usernamepic,font=("arial",15),bg="orange",text="Username",compound=LEFT)
    usernamelabel.place(x=40,y=150)
    usernameentry=Entry(loginframe,width=15,font=("arial",15))
    usernameentry.place(x=220,y=160)

    passwordpic = ImageTk.PhotoImage(file="password.jpg")
    passwordlabel = Label(loginframe, image=passwordpic, font=("arial", 15), bg="orange", text="Password",
                          compound=LEFT)
    passwordlabel.place(x=40, y=250)
    passwordentry = Entry(loginframe, width=15, font=("arial", 15))
    passwordentry.place(x=220, y=260)
    submitbutton=Button(loginframe,text="Submit",font=("arial", 11,"bold"),command=submit,bg="red",width=15)
    submitbutton.place(x=150,y=350)


    root.mainloop()
