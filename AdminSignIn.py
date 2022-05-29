from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from admin import Admin

class AdminSignin():
    def __init__(self,root):
        self.root=root
        self.root.geometry('930x600+300+200')
        self.root.configure(bg="#fff")
        self.root.title("Admin Sign In")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.resizable(False, False)

        # signin function taking default user as 'admin' and password as '1234'
        def signin():
            username=user.get()
            password=code.get()

            if username=='admin' and password=='1234':
                self.new_window = Toplevel(self.root)
                self.app = Admin(self.new_window)
            elif username != 'admin' and password != "1234":
                messagebox.showerror("Invalid", "invalid username and password ")
            elif password != "1234":
                messagebox.showerror(" Invalid ", " invalid password ")
            elif username != 'admin':
                messagebox.showerror(" Invalid ", " invalid password ")


        self.img = PhotoImage(file=r'myimages\admin.png')
        Label(root, image=self.img, bg='white').place(x=50, y=50)

        frame = Frame(root, width=350, height=350)
        frame.place(x=550, y=100)
        heading = Label(frame, text='Sign in ', fg='#57a1f8', font=('Microsoft YaHei UI Light ', 23, 'bold'))
        heading.place(x=120, y=5)

        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

        user = Entry(frame, width=25, fg='black', border=0,  font=('Microsoft YaHei UI Light ', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            code.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Password')
        def show():
           p = password.get()
           ttk.Label(root, text="Your Password is: " + str(p)).pack()

        password = StringVar()
        code = Entry(frame, width=25, textvariable=password,fg='black', border=0, font=('Microsoft YaHei UI Light ', 11),show="*")
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
        Button ( frame , width=39 , pady= 7 , text ='Sign in ' , bg ='#57a1f8'  ,border = 0 ,command=signin) .place ( x=35 , y=234 )

if __name__ == "__main__":
    root=Tk()
    obj=AdminSignin(root)
    root.mainloop()


