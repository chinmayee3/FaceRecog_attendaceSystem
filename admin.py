from tkinter import *
from PIL import Image,ImageTk
import os
from train import Train
from StudentRegister import StudentRegister
from attendance import Attendance

class Admin():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        #icon
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        #title
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
        title_lbl=Label(bg_img,text="FACULTY DASHBOARD",font=("times new roman",30,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        # photos button
        img5 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\photos.png")
        img5 = img5.resize((300, 300), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, command=self.open_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=200, y=180, width=220, height=220)


        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"))
        b1_1.place(x=200, y=400, width=220, height=35)

        # train data  button
        img6 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\train.png")
        img6 = img6.resize((300, 300), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b2 = Button(bg_img, command=self.train_data, image=self.photoimg6, cursor="hand2")
        b2.place(x=500, y=180, width=220, height=220)

        b2_1 = Button(bg_img, text="Train", command=self.train_data, cursor="hand2",
                      font=("times new roman", 15, "bold"))
        b2_1.place(x=500, y=400, width=220, height=35)

        # view attendance reports button
        img7 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\attendance.png")
        img7 = img7.resize((300, 300), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b3 = Button(bg_img, command=self.attendance, image=self.photoimg7, cursor="hand2")
        b3.place(x=800, y=180, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance Reports", command=self.attendance, cursor="hand2",
                      font=("times new roman", 15, "bold"))
        b3_1.place(x=800, y=400, width=220, height=35)

        # register new student button
        img8 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\newstud.png")
        img8 = img8.resize((300, 300), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b4 = Button(bg_img, command=self.register_stud, image=self.photoimg8, cursor="hand2")
        b4.place(x=1100, y=180, width=220, height=220)

        b4_1 = Button(bg_img, text="Register New Student", command=self.register_stud, cursor="hand2",
                      font=("times new roman", 15, "bold"))
        b4_1.place(x=1100, y=400, width=220, height=35)


    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def register_stud(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentRegister(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Admin(root)
    root.mainloop()



