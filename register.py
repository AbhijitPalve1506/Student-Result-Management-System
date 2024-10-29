from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # pip install pillow
import os
import sqlite3 
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #====Bg Image==
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #===Left Image==
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        #====Register Frame===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #=====variables====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        #--------Row1
        f_name=Label(frame1,text="First name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_fname).place(x=50,y=130,width=220)
        l_name=Label(frame1,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_lname).place(x=350,y=130,width=220)
        #---------Row2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_contact).place(x=50,y=200,width=220)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_email).place(x=350,y=200,width=220)
        #----------Row3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER,textvariable=self.var_question)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=220)
        self.cmb_quest.current(0)
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=240)
        txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_answer).place(x=350,y=270,width=220)
        #---------Row4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_password,show="x").place(x=50,y=340,width=220)
        cpassword=Label(frame1,text="Confirm password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=350,y=310)
        txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=self.var_cpassword,show="x").place(x=350,y=340,width=220)
        #------Terms----
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2",command=self.sign_in).place(x=200,y=460,width=150)

    def sign_in(self):
        self.root.destroy()
        os.system("python login.py")        

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_question.get()=="Select" or self.var_answer.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)            
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.var_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                else:                    
                     cur.execute("insert into employee (fname,lname,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_question.get(),
                    self.var_answer.get(),
                    self.var_password.get(),
                ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Registered Successfully",parent=self.root)            
                     self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)                

    def clear(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_answer.set("")
        self.var_password.set("")
        self.var_cpassword.set("")
        self.var_question.set("select")

if __name__=="__main__":  
   root=Tk()
   obj=Register(root)
   root.mainloop()     