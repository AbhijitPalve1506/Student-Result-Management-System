from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from login import Login_System
from datetime import*
import os
import time
import sqlite3
from math import *
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #====icons====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #===title=====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===Menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=12,y=70,width=1250,height=80)
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=180,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_student).place(x=230,y=5,width=180,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=430,y=5,width=180,height=40)
        btn_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=630,y=5,width=180,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=830,y=5,width=180,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1030,y=5,width=180,height=40)
        #===content_window====
        self.lbl_img=Image.open("images/bg.png")
        self.bg_img=self.lbl_img.resize((900,320),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=900,height=320)
        #===update_label===
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=500,width=250,height=100)
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=700,y=500,width=250,height=100)
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1000,y=500,width=250,height=100)
        self.lbl=Label(self.root,bg="white",bd=0)
        self.lbl.place(x=10,y=170,height=350,width=350)
        #self.clock_img()
        self.working()
        #===footer===
        footer=Label(self.root,text="ABHI Student Result Mangement System\n Contact us for any Technical Issue: 987xxxxx01",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def exit(self):
        self.root.destroy()
        os.system("python register.py")

    def logout(self):
        self.root.destroy()
        os.system("python login.py")        

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def add_login(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Login_System(self.new_win)                                

    def clock_img(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))    
        draw=ImageDraw.Draw(clock)
        #===For Clock Image====
        bg=Image.open("images/cl.jpg")
        bg=bg.resize((300,300),Image.LANCZOS)
        clock.paste(bg,(50,50))
        # Formula to rotate the Anticlock
        # angle_in_radians = angle_in_degrees * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)

        #===Hour Line Image===
        #  x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        #===Hour Line Image===
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        #===Hour Line Image===
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")

    def working(self):
         con=sqlite3.connect(database=r'rms.db')
         cur=con.cursor()
         try:
              h=datetime.now().time().hour
              m=datetime.now().time().minute
              s=datetime.now().time().second
              #print(h,m,s)
              hr=(h/12)*360
              min_=(m/60)*360
              sec_=(s/60)*360
              #print(hr,min_,sec_)
              self.clock_img(hr,min_,sec_)
              self.img=ImageTk.PhotoImage(file="clock_new.png")
              self.lbl.config(image=self.img)
              
              cur.execute("select * from course")
              course=cur.fetchall()
              self.lbl_course.config(text=f"Total Courses\n[{str(len(course))}]")

              cur.execute("select * from student")
              student=cur.fetchall()
              self.lbl_student.config(text=f"Total Students\n[{str(len(student))}]")

              cur.execute("select * from result")
              result=cur.fetchall()
              self.lbl_result.config(text=f"Total Results\n[{str(len(result))}]")
              self.lbl.after(200,self.working)

         except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()    
    obj=RMS(root)
    root.mainloop()