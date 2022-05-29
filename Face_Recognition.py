from tkinter import *
from PIL import Image, ImageTk
from mysql.connector import connect
import cv2
from datetime import datetime


lst=[]
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.title("Face_Recognition")
        # bg image
        # put path of image here
        img4 = Image.open(r"C:\Users\chinm\PycharmProjects\TkinterApp\myimages\bg1.png")
        img4 = img4.resize((1530, 750), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=1530, height=750)
        title_lbl = Label(bg_img, text="Mark Attendance ", font=("times new roman", 30, "bold"), fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        img_top = Image.open(r"myimages\face2.png")
        img_top = img_top.resize((400, 400), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(bg_img, image=self.photoimg_top)
        f_lbl.place(x=700, y=45, width=650, height=700)

        b1_1 = Button(bg_img, text="Click here To Capture !", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="silver", fg="black")
        b1_1.place(x=150, y=300, width=400, height=40)

    # save attendance in csv file here
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i in myDataList) or (r in myDataList) or (n in myDataList) or (d in myDataList)):
                pass
            elif ((i not in myDataList) and (r not in myDataList) and (n not in myDataList) and (d not in myDataList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i[0]},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        # rectangle to focus on face
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))


                conn = connect(host="localhost", user="root", password="root", database="face_recognizer")

                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()


                try:
                    n = "+".join(n)
                except Exception as e:
                    pass

                my_cursor.execute("select Rollno from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                try:
                    r = "+".join(r)
                except Exception as e:
                    pass

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                try:
                    d = "+".join(d)
                except Exception as e:
                    pass

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                try:
                    i = "+".join(i)
                except Exception as e:
                    pass
                #recognize face only if confidence is greater than 80%
                if confidence > 80:
                    cv2.putText(img, f"Id :{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll :{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name :{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department :{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    if id not in lst:
                        lst.append(id)
                        self.mark_attendance(i, r, n, d)
                    else:
                        break

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome", img)
            #open camera until enter key is pressed
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
