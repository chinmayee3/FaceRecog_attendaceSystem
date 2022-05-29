from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Student import Student
from mysql.connector import connect

class StudentSignin():
    def __init__(self,root):
        self.root = root
        self.root.title(' Student SignIn')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.resizable(False, False)

        # signin function taking default user as name of student and password also name of student
        def signin():
            username=user.get()
            password=code.get()
            #connecting with mysql
            conn = connect(host="localhost", user="root", password="root", database="face_recognizer")
            sql="select * from student where Name=%s and Name=%s"
            my_cursor = conn.cursor()
            my_cursor.execute(sql,[(username),(password)])
            results=my_cursor.fetchall()

            if results:
                #Redirect to student dashboard
                self.new_window = Toplevel(self.root)
                self.app = Student(self.new_window)
            elif username != 'student' and password != "1234":
                messagebox.showerror("Invalid", "invalid username and password ")
            elif password != "1234":
                messagebox.showerror(" Invalid ", " invalid password ")
            elif username != 'student':
                messagebox.showerror(" Invalid ", " invalid password ")


        self.img = PhotoImage(file=r'myimages\login.png')
        Label(root, image=self.img, bg='white').place(x=50, y=50)

        frame = Frame(root, width=350, height=350)
        frame.place(x=480, y=70)
        heading = Label(frame, text='Sign in ', fg='#57a1f8',  font=('Microsoft YaHei UI Light ', 23, 'bold'))
        heading.place(x=120, y=5)

        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')

        user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light ', 11))
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
        code = Entry(frame, width=25, textvariable=password,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light ', 11),show="*")
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button ( frame , width=39 , pady= 7 , text ='Sign in ' , bg ='#57a1f8' , fg = 'white' , border = 0 ,command=signin) .place ( x=35 , y=250 )


if __name__ == "__main__":
    root=Tk()
    obj=StudentSignin(root)
    root.mainloop()



