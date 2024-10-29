from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from tkinter import messagebox
import sqlite3
import os
import smtplib
import email_pass
from datetime import*
import time
from math import *
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.otp=''
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        #====icons====
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #===title=====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===LoginFrame===
        login_frame=Frame(self.root,bd=0,relief=RIDGE,bg="white")
        login_frame.place(x=250,y=90,width=700,height=490)
        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=20,relwidth=1)
        lbl_user=Label(login_frame,text="Email address",font=("Andalus",15),bg="white",fg="#767171").place(x=350,y=120)
        self.email=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.email,font=("times new roman",15),bg="#ECECEC").place(x=350,y=160,width=220)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=350,y=220)
        txt_password=Entry(login_frame,textvariable=self.password,show="x",font=("times new roman",15),bg="#ECECEC").place(x=350,y=260,width=220)
        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Aerial Rounded MT Bold",15),bg="#00B0f0",activebackground="#00B0f0",fg="white",activeforeground="white").place(x=350,y=320,width=220,height=32)
        hr=Label(login_frame,bg="lightgray").place(x=350,y=390,width=220,height=2)
        or_=Label(login_frame,bg="white",fg="gray",text="OR",font=("times new roman",13,"bold")).place(x=440,y=377)
        btn_forget=Button(login_frame,command=self.forget_window,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=390,y=410)
        self.lbl=Label(self.root,bg="white",bd=0)
        self.lbl.place(x=100,y=180,height=400,width=400)
        #self.clock_img()
        self.working()
        #====Footer===
        footer=Label(self.root,text="ABHI Student Result Mangement System\n Contact us for any Technical Issue: 987xxxxx01",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        
    def login(self):
     con=sqlite3.connect(database=r'rms.db')
     cur=con.cursor()
     try:
        if self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
           cur.execute("select fname from employee where email=? AND password=?",(self.email.get(),self.password.get()))
           fname=cur.fetchone()
           if fname==None:
             messagebox.showerror("Error","Invalid USERNAME or PASSWORD?",parent=self.root)
           else:
             self.root.destroy()
             os.system("python dashboard.py")     
     except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def forget_window(self):
       con=sqlite3.connect(database=r'rms.db')
       cur=con.cursor()
       try:
        if self.email.get()=="":
             messagebox.showerror("Error","Email address must be required",parent=self.root)
        else:
           cur.execute("select email from employee where email=?",(self.email.get(),))
           email=cur.fetchone()
           if email==None:
              messagebox.showerror("Error","Invalid Email address,try again",parent=self.root)
           else:
              #======Forget Window====
              self.var_otp=StringVar()
              self.var_new_pass=StringVar()
              self.var_conf_pass=StringVar()
              #call send_email_function()
              chk=self.send_email(email[0])
              if chk=='f':
                 messagebox.showerror("Error","Connection Error,try again",parent=self.root)
              else:
                self.forget_win=Toplevel(self.root)
                self.forget_win.title("RESET PASSWORD")
                self.forget_win.geometry("400x350+500+100")
                self.forget_win.focus_force()
                title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=240,height=30)
                self.btn_reset=Button(self.forget_win,command=self.validate_otp,text="Submit",font=("times new roman",15),bg="lightblue")
                self.btn_reset.place(x=270,y=100,width=90,height=30)
                new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=240,height=30)
                conf_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=220)
                txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=250,width=240,height=30)
                self.btn_update=Button(self.forget_win,command=self.update_password,text="Update",font=("times new roman",15),bg="lightblue",state=DISABLED)
                self.btn_update.place(x=150,y=300,width=90,height=30)
       except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update_password(self):
       if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
          messagebox.showerror("Error","Password is required",parent=self.forget_win)
       elif self.var_new_pass.get()!= self.var_conf_pass.get():
          messagebox.showerror("Error","Password & Confirm password should be same",parent=self.forget_win)
       else:  
          con=sqlite3.connect(database=r'rms.db')
          cur=con.cursor()
          try:
             cur.execute("Update employee set password=? where email=?",(self.var_new_pass.get(),self.email.get()))
             con.commit()
             messagebox.showinfo("Success","Password updated sucessfully",parent=self.root)
             self.forget_win.destroy()
          except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def validate_otp(self):
       if int(self.otp)==int(self.var_otp.get()):
          self.btn_update.config(state=NORMAL)
          self.btn_reset.config(state=DISABLED)
       else:    
          messagebox.showerror("Error","Invalid OTP, Try again",parent=self.forget_win)

    def send_email(self,to_):
       s=smtplib.SMTP('smtp.gmail.com',587)
       s.starttls()
       email_=email_pass.email_
       pass_=email_pass.pass_
       s.login(email_,pass_)
       self.otp=int(time.strftime("%H%M%S"))+int(time.strftime("%S"))
       subj='GMS-Reset Password OTP'
       msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nwith Regards,\nRMS Team'
       msg="Subject:{}\n\n{}".format(subj,msg)
       s.sendmail(email_,to_,msg)
       chk=s.ehlo()
       if chk[0]==250:
          return 's'
       else:
          return 'f'
       
    def clock_img(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))    
        draw=ImageDraw.Draw(clock)
        #===For Clock Image====
        bg=Image.open("images/c.png")
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
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #===Hour Line Image===
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #===Hour Line Image===
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("clock_new.png")

    def working(self):
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
        self.lbl.after(200,self.working)       

if __name__=="__main__":  
   root=Tk()
   obj=Login_System(root)
   root.mainloop() 