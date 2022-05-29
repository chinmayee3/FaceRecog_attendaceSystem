#student dashboard
from tkinter import *
from PIL import Image, ImageTk
from Face_Recognition import Face_Recognition

class Student():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.title("Attendance")

        img = Image.open(r"myimages\facial-recognition.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img2 = Image.open(r"myimages\studgrp.jpg")
        img2 = img2.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg image
        img4 = Image.open(r"myimages\bg1.png")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        img5 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\stdf.png")
        img5 = img5.resize((650, 500), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        f_lbl = Label(bg_img, image=self.photoimg5)
        f_lbl.place(x=20, y=45, width=650, height=500)

        title_lbl = Label(bg_img, text="Student Dashboard", font=("times new roman", 30, "bold"), fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        b4_1 = Button(bg_img, text="Mark Your Attendance",command=self.face_rec, cursor="hand2",
                      font=("times new roman", 15, "bold"))
        b4_1.place(x=900, y=320, width=220, height=35)

    # Call Face Rec class from Face_Recognition.py
    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()