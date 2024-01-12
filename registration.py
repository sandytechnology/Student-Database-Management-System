from tkinter import*
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql

#function
def login_window():
    root.destroy()
    import login
    
def clear():
    fname_entry.delete(0,END)
    lname_entry.delete(0,END)
    contact_entry.delete(0,END)
    email_entry.delete(0,END)
    security_combobox.current(0)
    ans_entry.delete(0,END)
    password_entry.delete(0,END)
    confirm_password_entry.delete(0,END)
    check.set(0)
def register():
    if fname_entry.get()=="" or lname_entry.get()=="" or password_entry.get()=="" or confirm_password_entry.get()=="" or ans_entry.get()=="" or security_combobox.get()=="select":
        messagebox.showerror("error","All Fields Are Required")
    elif password_entry.get()!=confirm_password_entry.get():
        messagebox.showerror("error","password and confirm password are not same")
    elif check.get()==0:
        messagebox.showerror("error","please agree to our term and condition")
    else:
        con=pymysql.connect(host="localhost",user="root",password="sandy713",database="student_database_management_system")
        cur=con.cursor()
        cur.execute("select*from registration where email=%s",email_entry.get())
        row=cur.fetchone()
        if row!=None:
            messagebox.showerror("error","user all ready exist")
        else:
            cur.execute("insert into registration(f_name,l_name,contact,email,security,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",(fname_entry.get(),lname_entry.get(),contact_entry.get(),email_entry.get(),security_combobox.get(),ans_entry.get(),password_entry.get()))
            
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registration is successfull...")
            clear()
            root.destroy()
            import login
    
#window 
root=Tk()
root.title("Registration Page")
root.geometry("1280x710+30+30")
root.resizable(0,0)

#Background Image
bg_open=Image.open("registration_bg.jpg")
bg_image=ImageTk.PhotoImage(bg_open)
bg_lbl=Label(root,image=bg_image)
bg_lbl.place(x=0,y=0)
#-----frame----
register_frm=Frame(root,width=650,height=650)
register_frm.place(x=370,y=30)

title_lbl=Label(register_frm,text="Registration Form",font=("aerial",25,"bold"))
title_lbl.place(x=30,y=5)
#----label----
fname_lbl=Label(register_frm,text="First Name : ",font=("aerial",20))
fname_lbl.place(x=30,y=55)
fname_entry=Entry(register_frm,font=("aerial",18),bg="light gray")
fname_entry.place(x=30,y=95)

lname_lbl=Label(register_frm,text="Last Name : ",font=("aerial",20))
lname_lbl.place(x=360,y=55)
lname_entry=Entry(register_frm,font=("aerial",18),bg="light gray")
lname_entry.place(x=360,y=95)

contact_lbl=Label(register_frm,text="Contact Number : ",font=("aerial",20))
contact_lbl.place(x=30,y=155)
contact_entry=Entry(register_frm,font=("aerial",18),bg="light gray")
contact_entry.place(x=30,y=195)

email_lbl=Label(register_frm,text="Email address : ",font=("aerial",20))
email_lbl.place(x=360,y=155)
email_entry=Entry(register_frm,font=("aerial",18),bg="light gray")
email_entry.place(x=360,y=195)

security_lbl=Label(register_frm,text="Security Questions : ",font=("aerial",20))
security_lbl.place(x=30,y=255)
security_combobox=Combobox(register_frm,font=("aerial",18),state="readonly")
security_combobox["values"]=("select","your mother name?","your birth place?","your best friend name?",
                             "your first pet name?","your favorite teacher name?","your favorite hobby?")
security_combobox.current(0)
security_combobox.place(x=30,y=305)

ans_lbl=Label(register_frm,text="Answer : ",font=("aerial",20))
ans_lbl.place(x=360,y=255)
ans_entry=Entry(register_frm,font=("aerial",18),bg="light gray")
ans_entry.place(x=360,y=305)

password_lbl=Label(register_frm,text="Password : ",font=("aerial",20))
password_lbl.place(x=30,y=365)
password_entry=Entry(register_frm,font=("aerial",18),bg="light gray",show="*")
password_entry.place(x=30,y=415)

confirm_password_lbl=Label(register_frm,text="Confirm Passsword : ",font=("aerial",20))
confirm_password_lbl.place(x=360,y=365)
confirm_password_entry=Entry(register_frm,font=("aerial",18),bg="light gray",show="*")
confirm_password_entry.place(x=360,y=415)

check=IntVar()
checkbutton=Checkbutton(register_frm,text="I agree all the terms and condition",onvalue=1,offvalue=0,
                        font=("aerial",16,"bold"),variable=check)
checkbutton.place(x=30,y=490)

register_btn=Button(register_frm,text="Register here",font=("Times new roman",18,"bold"),width=15,bg="royalblue",cursor="hand2",command=register)
register_btn.place(x=30,y=550)


login_btn1=Button(register_frm,text="Login ",font=("Times new roman",18,"bold"),width=15,bg="royalblue",cursor="hand2",command=login_window)
login_btn1.place(x=300,y=550)






root.mainloop()
