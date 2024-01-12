from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import pymysql

def reset_password():
    if email_entry.get()=="":
        messagebox.showerror("error","Please Enter the email address to reset")
    else:
        con=pymysql.connect(host="localhost",user="root",password="sandy713",database="student_database_management_system")
        cur=con.cursor()
        cur.execute("select*from registration where email=%s",email_entry.get())
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","Please enter the valid email address")
        else:
            con.close()

            def new_password():
                if security_qns.get()=="select" or ans_entry.get()=="" or new_password_entry.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=root2)
                else:
                    con=pymysql.connect(host="localhost",user="root",password="sandy713",database="student_database_management_system")
                    cur=con.cursor()
                    cur.execute("select * from registration where email=%s and security=%s and answer=%s",(email_entry.get(),security_qns.get(),ans_entry.get())) 
                              
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Security Question or Answer is Incorrect",parent=root2)
                    else:
                        cur.execute("update registration set password=%s where email=%s",(new_password_entry.get(),email_entry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Password is reset.Please Login with new password",parent=root2)
                        security_qns.current(0)
                        ans_entry.delete(0,END)
                        new_password_entry.delete(0,END)
                        root2.destroy()
                                    
                        

                  #--gui---
            root2=Toplevel()
            root2.title("Forget Password")
            root2.geometry("470x568+400+100")
            root2.config(bg="white")
            root2.focus_force()
            root2.grab_set()
                  
            forget_lbl=Label(root2,text="Forget",font=("arial",22,"bold"),bg="white")
            forget_lbl.place(x=120,y=10)

            password_lbl=Label(root2,text="Password",font=("arial",22,"bold"),bg="white",fg="green")
            password_lbl.place(x=222,y=10)
            
            blank_lbl=Label(root2,bg="green",width=62)
            blank_lbl.place(x=15,y=80)
                           
            security_lbl=Label(root2,text="Security Questions :",font=("arial",18,"bold"),bg="white")
            security_lbl.place(x=60,y=130)
                  
            security_qns=ttk.Combobox(root2,font=("arial",18),state="readonly",width=25)
            security_qns["values"]=("select","your mother name?","your birth place?","your best friend name?",
            "your first pet name?","your favorite teacher name?","your favorite hobby?")
            security_qns.current(0)
            security_qns.place(x=60,y=170)

            ans_lbl=Label(root2,text="Answer : ",font=("arial",18,"bold"),bg="white")
            ans_lbl.place(x=60,y=220)
            ans_entry=Entry(root2, font=("arial",18,"bold"),bg="white")
            ans_entry.place(x=60,y=270)

            new_password_lbl=Label(root2,text="New Password : ",font=("arial",18,"bold"),bg="white")
            new_password_lbl.place(x=60,y=320)
            new_password_entry=Entry(root2, font=("arial",18,"bold"),bg="white")
            new_password_entry.place(x=60,y=370)

            changepassword_btn=Button(root2,text="Change Password",font=("arial",18,"bold"),bg="white",cursor="hand2",command=new_password)
            changepassword_btn.place(x=150,y=430)      
                        
            root2.mainloop()

def register_window():
    root.destroy()
    import registration
def signin():
    if email_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror("error","all fields are required")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="sandy713",database="student_database_management_system")
            cur=con.cursor()
            cur.execute("select*from registration where email=%s and password=%s",(email_entry.get(),password_entry.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email or password")
            else:
                messagebox.showinfo("Success","Welcome to the database")
                root.destroy
                import sms
            con.close()
        except Exception as e:
            messagebox.showerror("error",f"Effort is due to {e}")
# Window for login        
root=Tk()
root.title("Login Page")
root.geometry("1280x700+30+30")
root.resizable(0,0)

#Background Image
bg_open=Image.open("login_bg.jpg")
bg_image=ImageTk.PhotoImage(bg_open)
bg_lbl=Label(root,image=bg_image)
bg_lbl.place(x=0,y=0)

#frame
login_frm=Frame(root,bg="lavender")
login_frm.place(x=400,y=150)

#logo Image
logo_img=PhotoImage(file="login_logo.png")
logo_lbl=Label(login_frm,image=logo_img)
logo_lbl.grid(row=0,column=0,columnspan=2,pady=20)

#username
username_image=PhotoImage(file="username.png"),
username_lbl=Label(login_frm,image=username_image,text="username :",compound=LEFT,font=("times new roman",25,"bold"),bg="lavender")
username_lbl.grid(row=1,column=0,pady=10,padx=20)

email_entry=Entry(login_frm,font=("times new roman",20,"bold"),bd=5)
email_entry.grid(row=1,column=1,pady=10,padx=20)

#Password
password_image=PhotoImage(file="lock.png"),
password_lbl=Label(login_frm,image=password_image,text="password :",compound=LEFT,font=("times new roman",25,"bold"),bg="lavender")
password_lbl.grid(row=2,column=0,pady=10,padx=20)

password_entry=Entry(login_frm,font=("times new roman",20,"bold"),bd=5)
password_entry.grid(row=2,column=1,pady=10,padx=20)

# login Button
login_btn=Button(login_frm,text="Login",font=("Times new roman",20,"bold"),fg="Black",bg="royalblue",width=10,activebackground="royalblue",cursor="hand2",command=signin)
login_btn.grid(row=3,column=1,pady=10)

reg_btn=Button(login_frm,text="Register New Account ?",font=("Times new roman",12,"bold"),fg="Black",bg="lavender",activebackground="lavender",bd=0,cursor="hand2",command=register_window)
reg_btn.grid(row=3,column=0)

forget_btn=Button(login_frm,text="Forget Password",font=("Times new roman",12,"bold"),fg="Black",bg="lavender",activebackground="lavender",bd=0,cursor="hand2",command=reset_password)
forget_btn.grid(row=4,column=0)


root.mainloop()