from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import cv2,os
import numpy as np

class Train():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.title("Train")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img_top = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\train3.png")
        img_top = img_top.resize((1530, 400), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=400)

        img_top2 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\bg1.png")
        img_top2 = img_top2.resize((1530, 450), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=0, y=325, width=1530, height=450)

        # bg image


        b1_1 = Button(self.root, text="Click Here To Train !", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 15, "bold"))
        b1_1.place(x=200, y=390, width=220, height=35)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # gray scale img
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

