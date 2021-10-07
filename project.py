Applications.py

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from admin import Admin
from attendance import Recognition
from login import Login


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Page")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg="light blue")
        # first img
        img = Image.open(r"background.jfif")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.master, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=130)

        # second img
        img2 = Image.open(r"back.jfif")
        img2 = img2.resize((600, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.master, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=600, height=130)

        # third img
        img3 = Image.open(r"face.jfif")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.master, image=self.photoimg3)
        f_lb1.place(x=1000, y=0, width=500, height=130)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.master, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        # reg img
        reg = Image.open(r"recognition.jfif")
        reg = reg.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(reg)

        btn1 = Button(bg_img, image=self.photoimg5)
        btn1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Take Attendance", command=self.new_window2, cursor="hand2", font=("time new roman", 16, "bold"), bg="white",
                      fg="dark blue")
        b1_1.place(x=100, y=300, width=220, height=40)

        # log img
        log = Image.open(r"login.png")
        log = log.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(log)
        btn2 = Button(bg_img, image=self.photoimg6)
        btn2.place(x=400, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Employee Login", command=self.employee_login, cursor="hand2", font=("time new roman", 16, "bold"), bg="white",
                      fg="dark blue")
        b1_1.place(x=400, y=300, width=220, height=40)

        # admin img
        admin = Image.open(r"admin.jfif")
        admin = admin.resize((200, 100), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(admin)
        btn3 = Button(bg_img, image=self.photoimg7, command=self.employee_details)
        btn3.place(x=700, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Admin", cursor="hand2", command=self.employee_details, font=("time new roman", 16, "bold"), bg="white",
                      fg="dark blue")
        b1_1.place(x=700, y=300, width=220, height=40)

        # exit img
        exe = Image.open(r"Exit.jfif")
        exe = exe.resize((200, 100), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(exe)
        btn4 = Button(bg_img, image=self.photoimg8, command=self.iExit)
        btn4.place(x=1000, y=100, width=230, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("time new roman", 16, "bold"), bg="white",
                      fg="dark blue")
        b1_1.place(x=1000, y=300, width=230, height=40)

        title = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  PORTAL", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1400, height=45)

    # ===============Function Buttons================

    def employee_details(self):
        self.new_window = Toplevel(self.master)
        self.app = Admin(self.new_window)

    def employee_login(self):
        self.new1_window = Toplevel(self.master)
        self.app = Login(self.new1_window)

    def new_window2(self):
        self.newWindow = Toplevel(self.master)
        self.app = Recognition(self.newWindow)

    def iExit(self):
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
            root.destroy()


root = Tk()
app = Window1(root)
root.mainloop()

                    --------------------------------------------------------------------------
employee.py

from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import random


class Employee:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Details")

        # ==========Variables==========
        self.var_dep = StringVar()
        self.var_design = StringVar()
        self.var_doj = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_gen = StringVar()
        self.var_blood = StringVar()
        self.var_email = StringVar()
        self.var_pno = StringVar()
        self.var_address = StringVar()
        self.var_status = StringVar()

        # first img
        img = Image.open(r"emp2.jfif")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=150)

        # second img
        img2 = Image.open(r"office.jfif")
        img2 = img2.resize((600, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=500, height=150)

        # third img
        img3 = Image.open(r"emp1.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root, image=self.photoimg3)
        f_lb1.place(x=900, y=0, width=500, height=150)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title = Label(bg_img, text="EMPLOYEE MANAGEMENT SYSTEM", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1350, height=45)
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=45, width=1480, height=600)

        # left label

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=670, height=580)

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=690, y=10, width=660, height=580)

        depart_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Department",
                                  font=("times new roman", 12, "bold"))
        depart_frame.place(x=10, y=20, width=650, height=100)

        dep_label = Label(depart_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(depart_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "HR", "Finance", "SAP", "Information Services", "Mobility", "DMS",
                               "ABAP")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        doj = Label(depart_frame, text="Date Of Joining", font=("times new roman", 12, "bold"))
        doj.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        cal = DateEntry(depart_frame, textvariable=self.var_doj, width=12, background='darkblue', foreground='white',
                        borderwidth=2)
        cal.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Design = Label(depart_frame, text="Designation", font=("times new roman", 12, "bold"))
        Design.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        des_combo = ttk.Combobox(depart_frame, textvariable=self.var_design, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        des_combo["values"] = ("select", "Trainee", "Associate Consultant", "Senior Consultant", "Principal Consultant",
                               "Project Manager")
        des_combo.current(0)
        des_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # employee details
        employee_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Employee Details",
                                    font=("times new roman", 12, "bold"))
        employee_frame.place(x=5, y=135, width=650, height=300)

        name = Label(employee_frame, text="Name:", font=("times new roman", 12, "bold"))
        name.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(employee_frame, textvariable=self.var_name, width=20,
                               font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        dob = Label(employee_frame, text="Date Of Birth:", font=("times new roman", 12, "bold"))
        dob.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        dob_cal = DateEntry(employee_frame, textvariable=self.var_dob, width=12, background='darkblue',
                            foreground='white', borderwidth=2)
        dob_cal.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        gender = Label(employee_frame, text="Gender:", font=("times new roman", 12, "bold"))
        gender.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        gen_combo = ttk.Combobox(employee_frame, textvariable=self.var_gen, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        gen_combo["values"] = ("select", "Male", "Female")
        gen_combo.current(0)
        gen_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        blood = Label(employee_frame, text="Blood Group:", font=("times new roman", 12, "bold"))
        blood.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        blood_entry = ttk.Entry(employee_frame, textvariable=self.var_blood, width=20,
                                font=("times new roman", 12, "bold"))
        blood_entry.grid(row=1, column=3, padx=10, sticky=W)

        email = Label(employee_frame, text="Email ID:", font=("times new roman", 12, "bold"))
        email.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(employee_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        phone = Label(employee_frame, text="Phone No:", font=("times new roman", 12, "bold"))
        phone.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        phn_entry = ttk.Entry(employee_frame, textvariable=self.var_pno, width=20, font=("times new roman", 12, "bold"))
        phn_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        address = Label(employee_frame, text="Address:", font=("times new roman", 12, "bold"))
        address.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(employee_frame, textvariable=self.var_address, width=20,
                               font=("times new roman", 12, "bold"))
        name_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        status = Label(employee_frame, text="Active Status:", font=("times new roman", 12, "bold"))
        status.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        state_combo = ttk.Combobox(employee_frame, textvariable=self.var_status, font=("times new roman", 12, "bold"),
                                   width=17, state="readonly")
        state_combo["values"] = ("select", "Active", "In Active")
        state_combo.current(0)
        state_combo.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        btn_frame = Frame(employee_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=160, width=640, height=110)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=25, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=1, padx=25, pady=15, sticky=W)

        Edit_btn = Button(btn_frame, text="Update", command=self.update_data, width=25,
                          font=("times new roman", 13, "bold"), bg="blue",
                          fg="white")
        Edit_btn.grid(row=0, column=2, padx=10, pady=15, sticky=W)

        del_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=25,
                         font=("times new roman", 13, "bold"), bg="blue",
                         fg="white")
        del_btn.grid(row=1, column=1, padx=25, pady=7, sticky=W)

        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=25,
                           font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=1, column=2, padx=10, pady=7, sticky=W)

        # ------------------Search System---------
        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System",
                                  font=("times new roman", 13, "bold"))
        Search_frame.place(x=5, y=23, width=600, height=70)

        search = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red")
        search.grid(row=0, column=0, padx=2, pady=10, sticky=W)
        self.search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=10, state="readonly")
        self.search_combo["values"] = ("select", "id", "Name", "department", "Designation")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        self.search_entry = ttk.Entry(Search_frame, width=20,
                                 font=("times new roman", 12, "bold"))
        self.search_entry.grid(row=0, column=2)

        search_btn = Button(Search_frame, text="Search", command=self.search_btn, width=10,
                            font=("times new roman", 12, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3)

        show_btn = Button(Search_frame, text="Show All", command=self.fetch_data, width=10, font=("times new roman", 12,
                                                                                                  "bold"), bg="blue",
                          fg="white")
        show_btn.grid(row=0, column=4)

        # =========== Search Attendance ========
        Attendance_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search Attendance",
                                      font=("times new roman", 13, "bold"))
        Attendance_frame.place(x=5, y=230, width=600, height=70)

        search = Label(Attendance_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red")
        search.grid(row=0, column=0, padx=2, pady=10, sticky=W)
        self.search_combo1 = ttk.Combobox(Attendance_frame, font=("times new roman", 12, "bold"), width=17,
                                          state="readonly")
        self.search_combo1["values"] = ("select", "1100", "1157", "1171", "1191", "1255", "1287", "1432")
        self.search_combo1.current(0)
        self.search_combo1.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        search_btn1 = Button(Attendance_frame, text="Search", width=10, command=self.attendance,
                             font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        search_btn1.grid(row=0, column=2)

        # =============Table Frame===========
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=100, width=570, height=130)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=("dep", "design", "doj", "id", "name", "dob", "gen",
                                                                "blood", "email", "phn no", "address", "status"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep", text="Department")
        self.employee_table.heading("design", text="Designation")
        self.employee_table.heading("doj", text="Date of Joining")
        self.employee_table.heading("id", text="Emp ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("dob", text="Date of Birth")
        self.employee_table.heading("gen", text="Gender")
        self.employee_table.heading("blood", text="Blood Group")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("phn no", text="Phone no")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("status", text="Status")
        self.employee_table["show"] = "headings"

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # table view for attendance
        table1_frame1 = Frame(Right_frame, bd=2, relief=RIDGE)
        table1_frame1.place(x=5, y=310, width=570, height=130)

        scroll_x = ttk.Scrollbar(table1_frame1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table1_frame1, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table1_frame1, column=("empid", "name", "date", "cintime", "couttime"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("empid", text="Employee id")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("cintime", text="Check in")
        self.attendance_table.heading("couttime", text="Check out")
        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill=BOTH, expand=1)

    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        rows = content['values']
        self.var_dep.set(rows[0])
        self.var_design.set(rows[1])
        self.var_doj.set(rows[2])
        self.var_name.set(rows[4])
        self.var_dob.set(rows[5])
        self.var_gen.set(rows[6])
        self.var_blood.set(rows[7])
        self.var_email.set(rows[8])
        self.var_pno.set(rows[9])
        self.var_address.set(rows[10])
        self.var_status.set(rows[11])

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pno.get() == "" or self.var_design.get() == "select" or self.var_gen.get() == "select" or self.var_blood.get() == "" or self.var_email.get() == "" or self.var_address.get() == "" or self.var_status.get() == "select":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="atna")
                cur = con.cursor()
                id = random.randint(1000, 1500)

                cur.execute("Insert into register(department, designation, doj, id, name, dob, gender, blood, email, "
                            "phone, address, "
                            "status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.var_dep.get(),
                                self.var_design.get(),
                                self.var_doj.get(),
                                id,
                                self.var_name.get(),
                                self.var_dob.get(),
                                self.var_gen.get(),
                                self.var_blood.get(),
                                self.var_email.get(),
                                self.var_pno.get(),
                                self.var_address.get(),
                                self.var_status.get()
                            )
                            )
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Saved Successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", "Error occur", parent=self.root)

    # =================fetch data==========
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", db="atna")
        cur = con.cursor()
        cur.execute("select * from register")
        data = cur.fetchall()

        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            con.commit()
        con.close()

    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_pno.get() == "" or self.var_design.get() == "select" or self.var_gen.get() == "select" or self.var_blood.get() == "" or self.var_email.get() == "" or self.var_address.get() == "" or self.var_status.get() == "select":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this employee details", parent=self.root)
                if Update > 0:
                    con = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    cur = con.cursor()
                    cur.execute(
                        "update register set dep=%s, design=%s, doj=%s, name=%s, dob=%s, gen=%s, blood=%s, email=%s, "
                        "phno=%s, address=%s, status=%s, where name=%s",
                        (
                            self.var_dep.get(),
                            self.var_design.get(),
                            self.var_doj.get(),
                            self.var_name.get(),
                            self.var_dob.get(),
                            self.var_gen.get(),
                            self.var_blood.get(),
                            self.var_email.get(),
                            self.var_pno.get(),
                            self.var_address.get(),
                            self.var_status.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Employee Details successfully updated")
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_name.get() == "":
            messagebox.showerror("Error", "Employee Name must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Details", "Do you want to Delete this Employee Details",
                                             parent=self.root)
                if delete > 0:
                    con = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    cur = con.cursor()
                    sql = "delete from register where name=%s"
                    val = (self.var_name.get())
                    cur.execute(sql, val)
                else:
                    if not delete:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Delete", "Successfully deleted employee details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_design.set("select"),
        self.var_doj.set(""),
        self.var_name.set(""),
        self.var_dob.set(""),
        self.var_gen.set("select"),
        self.var_blood.set(""),
        self.var_email.set(""),
        self.var_pno.set(""),
        self.var_address.set(""),
        self.var_status.set("select")

    def search_btn(self):
        search = self.search_combo.get()
        text = self.search_entry.get()
        con = pymysql.connect(host="localhost", user="root", password="", db="atna")
        cur = con.cursor()
        if search == "Name":
            cur.execute("select * from register where name=%s", text)
            data = cur.fetchall()
        if search == "id":
            cur.execute("select * from register where id=%s", text)
            data = cur.fetchall()
        if search == "department":
            cur.execute("select * from register where department=%s", text)
            data = cur.fetchall()
        if search == "Designation":
            cur.execute("select * from register where designation=%s", text)
            data = cur.fetchall()

        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            con.commit()
        con.close()

    def attendance(self):
        ID = self.search_combo1.get()
        conn = pymysql.connect(host="localhost", user="root", password="", db="atna")
        curr = conn.cursor()
        curr.execute("select * from checkout where empid=%s", ID)
        data = curr.fetchall()

        if len(data) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in data:
                self.attendance_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
-----------------------------------------------------------------------------------------------------------

admin.py

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from employee import Employee


class Admin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Admin Page")

        # first img
        img = Image.open(r"emp2.jfif")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=150)

        # second img
        img2 = Image.open(r"office.jfif")
        img2 = img2.resize((600, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=500, height=150)

        # third img
        img3 = Image.open(r"emp1.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root, image=self.photoimg3)
        f_lb1.place(x=900, y=0, width=500, height=150)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title = Label(bg_img, text="ADMIN LOGIN PAGE", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1350, height=45)
        admin_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="light blue")
        admin_frame.place(x=465, y=135, width=450, height=250)
        user = Label(admin_frame, text="Admin ID", font=("times new roman", 12, "bold"), bg="light blue")
        user.grid(row=0, column=0, padx=50, pady=40, sticky=W)
        self.name_entry = ttk.Entry(admin_frame, width=20, font=("times new roman", 12, "bold"))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        password = Label(admin_frame, text="Password", font=("times new roman", 12, "bold"), bg="light blue")
        password.grid(row=1, column=0, padx=50, pady=5, sticky=W)
        self.pass_entry = ttk.Entry(admin_frame, width=20, show="*", font=("times new roman", 12, "bold"))
        self.pass_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        self.reset_btn = Button(admin_frame, text="Login", width=15, command=self.admin_pass,
                                font=("times new roman", 13, "bold"), bg="blue",
                                fg="white")
        self.reset_btn.grid(row=2, column=1, padx=50, pady=50, sticky=W)

    def admin_pass(self):
        var_name = "tafe21"
        var_pass = "here2021"
        if self.pass_entry.get() == "" or self.name_entry.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            if self.name_entry.get() == var_name and self.pass_entry.get() == var_pass:
                messagebox.showinfo("Success", "Successfully logged in..", parent=self.root)
                self.employee_details()
            else:
                messagebox.showinfo("Error", "Id or password is wrong", parent=self.root)

    def employee_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Employee(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()
------------------------------------------------------------------------------------------------------------------------

attendance.py

import os
from datetime import datetime
from tkinter import *
import cv2
import face_recognition
import numpy as np
import pymysql
from PIL import Image, ImageTk


class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Attendance Page")

        self.var_name = StringVar()
        self.var_pass = StringVar()

        # first img
        img = Image.open(r"emp2.jfif")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=150)

        # second img
        img2 = Image.open(r"office.jfif")
        img2 = img2.resize((600, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=500, height=150)

        # third img
        img3 = Image.open(r"emp1.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root, image=self.photoimg3)
        f_lb1.place(x=900, y=0, width=500, height=150)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title = Label(bg_img, text="EMPLOYEE ATTENDANCE PAGE", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1350, height=45)

        Checking = Image.open(r"check.png")
        Checking = Checking.resize((200, 100), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(Checking)
        btn3 = Button(bg_img, image=self.photo1)
        btn3.place(x=400, y=100, width=220, height=220)

        self.btn1 = Button(bg_img, text="Check In", cursor="hand2", command=self.new_window3,
                           font=("time new roman", 16, "bold"), bg="white",
                           fg="dark blue")
        self.btn1.place(x=400, y=300, width=220, height=40)

        checkout = Image.open(r"checkout.png")
        checkout = checkout.resize((200, 100), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(checkout)
        btn4 = Button(bg_img, image=self.photo2)
        btn4.place(x=700, y=100, width=220, height=220)

        self.btn2 = Button(bg_img, text="Check Out", cursor="hand2", command=self.face_recog,
                           font=("time new roman", 16, "bold"), bg="white",
                           fg="dark blue")
        self.btn2.place(x=700, y=300, width=220, height=40)

    def new_window3(self):
        path = "imageAttendence"
        images = []
        classNames = []
        myList = os.listdir(path)

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        def findEncodings(images):
            encodelist = []

            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodelist.append(encode)
            return encodelist

        def markAttendance(ename):
            with open('Attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if ename not in nameList:
                    now = datetime.now()
                    date = now.strftime('%y-%m-%d')
                    time = now.strftime('%H:%M:%S')
                    status = "present"

                    f.writelines(f'\n{num},{ename},{date},{time},{status}')
                    conn = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    curr = conn.cursor()
                    curr.execute("insert into attendance(empid, name, date, cintime)values(%s,%s,%s,%s)",
                                 (num, ename, date, time))
                    conn.commit()
                    conn.close()

        encodeListKnown = findEncodings(images)
        print('Encoding complete')

        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    ename = classNames[matchIndex]
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    con = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    cur = con.cursor()

                    cur.execute("select id from register where name=%s", ename)
                    nom = cur.fetchone()
                    num = "+".join(nom)

                    cur.execute("select department from register where name=%s", ename)
                    d = cur.fetchone()
                    d = "+".join(d)

                    cv2.putText(img, f"Emp ID:{num}", (x1, y2+10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{ename}", (x1, y2+30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x1, y2+55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    markAttendance(ename)

                elif matches != [matchIndex]:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.putText(img, "UNKNOWN FACE", (x1+6, y2-3), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255),
                                2)

            cv2.imshow('Check in', img)
            cv2.waitKey(1)

    # ============ Face Recognition ===============
    def face_recog(self):
        path = "imageAttendence"
        images = []
        classNames = []
        myList = os.listdir(path)

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        def findEncodings(images):
            encodelist = []

            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodelist.append(encode)
            return encodelist

        def checkout(name):
            with open('employee_attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    date = now.strftime('%y-%m-%d')
                    out = now.strftime('%H:%M:%S')

                    connect = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    cursor = connect.cursor()
                    cursor.execute("select cintime from attendance where name=%s", name)
                    i = cursor.fetchone()
                    check = ":".join(i)
                    cursor.execute("insert into checkingout(empid, name, date, cintime, couttime)values(%s,%s,%s,%s,%s)",
                                   (t, name, date, check, out))
                    connect.commit()
                    connect.close()
                    f.writelines(f'\n{t},{name},{date},{check},{out}')

        encodeListKnown = findEncodings(images)
        print('Encoding complete')

        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex]
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cone = pymysql.connect(host="localhost", user="root", password="", db="atna")
                    curs = cone.cursor()

                    curs.execute("select id from register where name=%s", name)
                    y = curs.fetchone()
                    t = ":".join(y)

                    curs.execute("select department from register where name=%s", name)
                    d = curs.fetchone()
                    d = ":".join(d)

                    cv2.putText(img, f"Emp ID:{t}", (x1, y2+10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x1, y2+30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x1, y2+55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    checkout(name)

                elif matches != [matchIndex]:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.putText(img, "UNKNOWN FACE", (x1 + 6, y2 - 3), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255),
                                2)

            cv2.imshow('Check out', img)
            cv2.waitKey(1)


if __name__ == "__main__":
    root = Tk()
    obj = Recognition(root)
    root.mainloop()
------------------------------------------------------------------------------------------------------------------------

login.py

from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk

from userpage import Userpage


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Login Page")

        self.var_name = StringVar()
        self.var_pass = StringVar()

        # first img
        img = Image.open(r"emp2.jfif")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=150)

        # second img
        img2 = Image.open(r"office.jfif")
        img2 = img2.resize((600, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=500, height=150)

        # third img
        img3 = Image.open(r"emp1.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root, image=self.photoimg3)
        f_lb1.place(x=900, y=0, width=500, height=150)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title = Label(bg_img, text="EMPLOYEE LOGIN PAGE", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1350, height=45)
        admin_frame = Frame(bg_img, bd=2, relief=RIDGE, bg="light blue")
        admin_frame.place(x=465, y=135, width=450, height=250)
        user = Label(admin_frame, text="EMPLOYEE ID:", font=("times new roman", 12, "bold"), bg="light blue")
        user.grid(row=0, column=0, padx=50, pady=40, sticky=W)
        name_entry = ttk.Entry(admin_frame, width=20, textvariable=self.var_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        password = Label(admin_frame, text="PASSWORD:", font=("times new roman", 12, "bold"), bg="light blue")
        password.grid(row=1, column=0, padx=50, pady=5, sticky=W)
        pass_entry = ttk.Entry(admin_frame, width=20, show="*", textvariable=self.var_pass,
                               font=("times new roman", 12, "bold"))
        pass_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        login_btn = Button(admin_frame, text="Login", width=15, command=self.verify_data,
                           font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        login_btn.grid(row=2, column=1, padx=50, pady=50, sticky=W)

    def verify_data(self):
        if self.var_name.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("warning", "All fields are required to fill", parent=self.root)
        else:
            try:
                eid = self.var_name.get()
                Password = self.var_pass.get()
                con = pymysql.connect(host="localhost", user="root", password="", db="atna")
                cur = con.cursor()
                sql = "select * from register where id=%s and phone=%s"
                cur.execute(sql, [eid, Password])
                results = cur.fetchall()
                if results:
                    for i in results:
                        messagebox.showinfo("Success", "Logged in Successfully..", parent=self.root)
                        self.user_page()
                        break
                    else:
                        messagebox.showerror("warring", "Check your id, password", parent=self.root)
                con.commit()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", "Error Handling", parent=self.root)

    def user_page(self):
           self.window = Toplevel(self.root)
           self.app = Userpage(self.window)


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
-----------------------------------------------------------------------------------------------------------------

userpage.py

from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from PIL import Image, ImageTk


class Userpage():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee User Page")

        # first img
        img = Image.open(r"emp2.jfif")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=400, height=150)

        # second img
        img2 = Image.open(r"office.jfif")
        img2 = img2.resize((600, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=400, y=0, width=500, height=150)

        # third img
        img3 = Image.open(r"emp1.jfif")
        img3 = img3.resize((500, 150), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root, image=self.photoimg3)
        f_lb1.place(x=900, y=0, width=500, height=150)

        # bg img
        bg = Image.open(r"bgimg.jpg")
        bg = bg.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title = Label(bg_img, text="EMPLOYEE PAGE", font=("time new roman", 26, "bold"),
                      bg="powder blue", fg="black").place(x=0, y=0, width=1350, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=45, width=1480, height=600)

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Employee Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=690, y=10, width=660, height=580)

        # img 1

        View_details = Image.open(r"register.png")
        View_details = View_details.resize((200, 100), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(View_details)
        btn3 = Button(bg_img, image=self.img1, command=self.check_details)
        btn3.place(x=100, y=100, width=220, height=220)

        self.btn1 = Button(bg_img, text="View My Details", cursor="hand2", command=self.check_details,
                           font=("time new roman", 16, "bold"), bg="white",
                           fg="dark blue")
        self.btn1.place(x=100, y=300, width=220, height=40)

        # img 2

        attendance = Image.open(r"check.png")
        attendance = attendance.resize((200, 100), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(attendance)
        btn4 = Button(bg_img, image=self.img2, command=self.check_attendance)
        btn4.place(x=400, y=100, width=220, height=220)

        self.btn2 = Button(bg_img, text="Attendance Details", cursor="hand2", command=self.check_attendance,
                           font=("time new roman", 16, "bold"), bg="white",
                           fg="dark blue")
        self.btn2.place(x=400, y=300, width=220, height=40)
        # =================== Search for Attendance ==================
        self.search_combo = ttk.Combobox(Right_frame, font=("times new roman", 12, "bold"), width=17, state="readonly")
        self.search_combo["values"] = ("select", "1100", "1171", "1191", "1151", "1255", "1287", "1432", "1157")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ==============table=============
        table_frame1 = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame1.place(x=5, y=50, width=570, height=150)

        scroll_x = ttk.Scrollbar(table_frame1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame1, orient=VERTICAL)

        self.employee_detail = ttk.Treeview(table_frame1, column=("dep", "design", "doj", "id", "name", "dob", "gen",
                                                                 "blood", "email", "phn no", "address", "status"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_detail.xview)
        scroll_y.config(command=self.employee_detail.yview)

        self.employee_detail.heading("dep", text="Department")
        self.employee_detail.heading("design", text="Designation")
        self.employee_detail.heading("doj", text="Date of Joining")
        self.employee_detail.heading("id", text="Emp ID")
        self.employee_detail.heading("name", text="Name")
        self.employee_detail.heading("dob", text="Date of Birth")
        self.employee_detail.heading("gen", text="Gender")
        self.employee_detail.heading("blood", text="Blood Group")
        self.employee_detail.heading("email", text="Email")
        self.employee_detail.heading("phn no", text="Phone no")
        self.employee_detail.heading("address", text="Address")
        self.employee_detail.heading("status", text="Status")
        self.employee_detail["show"] = "headings"

        self.employee_detail.pack(fill=BOTH, expand=1)

        # ==============table=============
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=250, width=570, height=140)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame, column=("empid", "name", "date", "checkin", "checkout"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("empid", text="Emp id")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("checkin", text="Check in")
        self.attendance_table.heading("checkout", text="Check out")
        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill=BOTH, expand=1)

    def check_attendance(self):
        ID = self.search_combo.get()
        con = pymysql.connect(host="localhost", user="root", password="", db="atna")
        cur = con.cursor()
        cur.execute("select * from checkout where empid=%s", ID)
        data = cur.fetchall()

        if len(data) != 0:
            self.attendance_table.delete(*self.attendance_table.get_children())
            for i in data:
                self.attendance_table.insert("", END, values=i)
            con.commit()
        con.close()

        # ======= Details of the Employee =======

    def check_details(self):
        ID = self.search_combo.get()
        conn = pymysql.connect(host="localhost", user="root", password="", db="atna")
        cur = conn.cursor()
        cur.execute("select * from register where id=%s", ID)
        data = cur.fetchall()

        if len(data) != 0:
            self.employee_detail.delete(*self.employee_detail.get_children())
            for i in data:
                self.employee_detail.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Userpage(root)
    root.mainloop()
---------------------------------------------------------------------------------------------------------

