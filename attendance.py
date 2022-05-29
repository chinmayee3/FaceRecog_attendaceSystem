from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os,csv
from tkinter import filedialog

# matched data with time is stored in attendance.csv file
mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        p1 = PhotoImage(file=r'myimages\icon2.png')
        self.root.iconphoto(False, p1)
        self.root.title("Attendance")
        #variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


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

        title_lbl = Label(bg_img, text="Attendance Report", font=("times new roman", 30, "bold"), fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendence Details",font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=600)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=65,width=720,height=400)

        AttendanceId_label = Label(left_inside_frame, text="AttendanceID :", font=("times new roman", 12, "bold"),
                                    bg="white")
        AttendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        AttendanceId_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,
                                    font=("times new roman", 12, "bold"))
        AttendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        #Roll
        rollLabel=Label(left_inside_frame,text="Roll : ",bg="white",font=("times new roman", 12, "bold"))
        rollLabel.grid(row=0, column=2, padx=4, pady=8)
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=22, font=" comicsansns 11 bold ")
        atten_roll.grid(row=0, column=3, pady=8)
        # date
        nameLabel = Label(left_inside_frame, text=" Name : ", bg="white", font="comicsansns 11 bold ")
        nameLabel.grid(row=1, column=0)
        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name, width=22, font="comicsansns 11 bold ")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text=" Department : ", bg="white", font=" comicsansns 11 bold ")
        depLabel.grid(row=1, column=2)
        atten_dep = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep,width=22, font=" comicsansns 11 bold ")
        atten_dep.grid(row=1, column=3, pady=8)
        # time
        timeLabel = Label(left_inside_frame, text=" Time : ", bg="white", font=" comicsansns 11 bold ")
        timeLabel.grid(row=2, column=0)
        atten_time = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time,width=22, font=" comicsansns 11 bold ")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date : ", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date,width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)
        # attendance
        attendanceLabel = Label(left_inside_frame, text=" Attendance Status ", bg="white",
                                font="comicsansns 11 bold ")
        attendanceLabel.grid(row=3, column=0)
        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, width=20, font=" comicsansns 11 bold ", state="readonly")
        self.atten_status["values"] = ("Status", "Present ", "Absent ")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)
        import_btn=Button(btn_frame, text=" Import csv ",command=self.importCsv, width=23, font=("times new roman ", 13, " bold "),
                          bg="grey", fg="white")
        import_btn.grid(row=0, column=0)
        export_btn = Button(btn_frame, text=" Export csv ",command=self.exportCsv, width=23, font=(" times new roman ", 13, "bold"),
                            bg="grey",fg="white")
        export_btn.grid(row=0, column=1)
        reset_btn= Button(btn_frame, text=" Reset ",command=self.reset_data, width=23, font=("times new roman ", 13, " bold "), bg="grey",
                           fg="white")
        reset_btn.grid(row=0, column=2)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendence Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=800, y=10, width=700, height=600)

        table_frame=Frame(right_frame, bd= 2, relief= RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        # scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.AttendaceReportTable = ttk.Treeview(table_frame, column=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand =scroll_x.set , yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side =RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview )
        scroll_y.config(command=self.AttendaceReportTable.yview )
        self.AttendaceReportTable.heading("id", text="Attendace ID")


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side =RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        self.AttendaceReportTable.heading("id", text=" Attendance ID ")
        self.AttendaceReportTable.heading("roll", text=" Roll ")
        self.AttendaceReportTable.heading("name", text=" Name ")
        self.AttendaceReportTable.heading("department", text=" Department ")
        self.AttendaceReportTable.heading("time", text=" Time ")
        self.AttendaceReportTable.heading("date", text=" Date ")
        self.AttendaceReportTable.heading("attendance", text="Attendance ")
        self.AttendaceReportTable["show"] = "headings "
        #self.AttendaceReportTable.column()

        self.AttendaceReportTable.column("id", width=100)
        self.AttendaceReportTable.column("roll", width=100)
        self.AttendaceReportTable.column("name", width=100)
        self.AttendaceReportTable.column("department", width=100)
        self.AttendaceReportTable.column("time", width=100)
        self.AttendaceReportTable.column("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100)
        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)
    #fetch data
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)

    # import data from csv file
    def importCsv(self):
        global mydata
        mydata.clear()
        fln =filedialog.askopenfilename(initialdir= os.getcwd(), title=" Open CSV ", filetypes=(("CSV File", "*.csv"),("All File","*.*")),parent=self.root)
        with open (fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export ", parent = self.root)
                return False
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(" Data Export ", " Your data exported to " + os.path.basename(fln) + " successfully ")
        except Exception as es:
                messagebox.showerror("Error", f" Due To : {str(es)} ", parent = self.root )

    def get_cursor(self, event=" "):
        cursor_row =self.AttendaceReportTable.focus()
        content =self.AttendaceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    #reset the values
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
