from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1100x450+80+190")
        self.root.config(bg="white")
        self.root.focus_force()
        #===title=====
        title=Label(self.root,text="View Student Results",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=5,y=19,width=1100,height=40)
        self.var_search=StringVar()
        self.var_id=""
        #=====search====
        lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=280,y=90)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow").place(x=460,y=90,width=150)
        btn_search=Button(self.root,text="Search",font=("goudy old style",18,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=650,y=90,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",18,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=770,y=90,width=110,height=28)
        #======result_labels=====
        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks_ob=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_ob.place(x=600,y=280,width=150,height=50)
        self.full_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full_marks.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)
        #==========Button Delete===
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",18,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=540,y=360,width=130,height=28)
#==================================================
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:    
                 cur.execute("select * from result where roll=?",(self.var_search.get(),))  
                 row=cur.fetchone()
                 if row!=None:  
                     self.var_id=row[0]          
                     self.roll.config(text=row[1])
                     self.name.config(text=row[2])
                     self.course.config(text=row[3])
                     self.marks_ob.config(text=row[4])
                     self.full_marks.config(text=row[5])
                     self.per.config(text=row[6])
                 else:
                     messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")            
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))  
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()    
    obj=reportClass(root)
    root.mainloop()        