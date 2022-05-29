import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from AdminSignIn import AdminSignin
from StudentSignIn import StudentSignin

class Face_Recognition_System():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        #icon
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.title("Attendance Management System")

        #top images
        img=Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\I1.jpg")
        img=img.resize((500,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=200)

        img2 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\I2.jpg")
        img2 = img2.resize((500, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=200)

        img3 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\I3.jpg")
        img3 = img3.resize((700,200), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=700, height=200)

        #bg image
        img4 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\bg1.png")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)
        title_lbl=Label(bg_img,text="ATTENDANCE MONITORING SYSTEM",font=("times new roman",30,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        #student button
        img5=Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\student1.png")
        img5=img5.resize((300,300),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,command=self.student_login,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,command=self.student_login,text="Student Login",cursor="hand2",font=("times new roman",15,"bold"))
        b1_1.place(x=200,y=320,width=220,height=35)

        # faculty button
        img6 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\facullty1.png")
        img6 = img6.resize((250, 250), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2 = Button(bg_img,command=self.faculty_login, image=self.photoimg6, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img,command=self.faculty_login, text="Faculty Login", cursor="hand2", font=("times new roman", 15, "bold"))
        b2_1.place(x=500, y=320, width=220, height=35)

        # exit button
        img7 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\exit2.png")
        img7 = img7.resize((250, 250), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b3 = Button(bg_img,command=self.iExit,image=self.photoimg7, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img,command=self.iExit,text="Exit", cursor="hand2", font=("times new roman", 15, "bold"))
        b3_1.place(x=800, y=320, width=220, height=35)

    def student_login(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentSignin(self.new_window)

    def faculty_login(self):
        self.new_window=Toplevel(self.root)
        self.app=AdminSignin(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit")
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


