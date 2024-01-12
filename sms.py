from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def i_exit():
      result=messagebox.askyesno("Confirm","Do You Want To Exit ?",parent=root)
      if result:
            root.destroy()
      else:
            pass

def export_student():
      url=filedialog.asksaveasfilename(defaultextension=".csv")
      indexing=student_table.get_children()
      new_list=[]
      for index in indexing:
            content=student_table.item(index)
            data_list=content["values"]
            new_list.append(data_list)

      table=pandas.DataFrame(new_list,columns=["Id","Name","Mobile","Email","Address","Gender","DOB","Added Date","Added Time"])
      table.to_csv(url,index=FALSE)
      messagebox.showinfo("Success","Data is saved succefully",parent=left_frm)

def update_student():
      def update_data():
            query="update student_1 set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s"
            mycursor.execute(query,(name_entry.get(),phone_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),date,current_time,id_entry.get()))
            con.commit()
            messagebox.showinfo("update",f"Id{id_entry.get()}is update successfully",parent=update_window)
            update_window.destroy()
            show_student()
            
      update_window=Toplevel()
      update_window.grab_set()
      update_window.title("Update Student")
      update_window.resizable(0,0)
      
      id_lbl=Label(update_window,text="Id",font=("times new roman",20,"bold"))
      id_lbl.grid(row=0,column=0,padx=30,pady=15,sticky=W)
      id_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      id_entry.grid(row=0,column=1,padx=15,pady=10)
      
      name_lbl=Label(update_window,text="Name",font=("times new roman",20,"bold"))
      name_lbl.grid(row=1,column=0,padx=30,pady=15,sticky=W)
      name_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      name_entry.grid(row=1,column=1,padx=15,pady=10)
      
      phone_lbl=Label(update_window,text="Phone",font=("times new roman",20,"bold"))
      phone_lbl.grid(row=2,column=0,padx=30,pady=15,sticky=W)
      phone_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      phone_entry.grid(row=2,column=1,padx=15,pady=10)
      
      email_lbl=Label(update_window,text="Email",font=("times new roman",20,"bold"))
      email_lbl.grid(row=3,column=0,padx=30,pady=15,sticky=W)
      email_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      email_entry.grid(row=3,column=1,padx=15,pady=10)
      
      address_lbl=Label(update_window,text="Address",font=("times new roman",20,"bold"))
      address_lbl.grid(row=4,column=0,padx=30,pady=15,sticky=W)
      address_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      address_entry.grid(row=4,column=1,padx=15,pady=10)
      
      gender_lbl=Label(update_window,text="Gender",font=("times new roman",20,"bold"))
      gender_lbl.grid(row=5,column=0,padx=30,pady=15,sticky=W)
      gender_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      gender_entry.grid(row=5,column=1,padx=15,pady=10)
      
      dob_lbl=Label(update_window,text="D.O.B.",font=("times new roman",20,"bold"))
      dob_lbl.grid(row=6,column=0,padx=30,pady=15,sticky=W)
      dob_entry=Entry(update_window,font=("times new roman",20,"bold"),width=24)
      dob_entry.grid(row=6,column=1,padx=15,pady=10)
      
      update_student_btn=ttk.Button(update_window,text="Update Student",width=20,command=update_data)
      update_student_btn.grid(row=7,columnspan=2,pady=10)
      
      indexing=student_table.focus()
      content=student_table.item(indexing)
      list_data=content["values"]
      id_entry.insert(0,list_data[0])
      name_entry.insert(0,list_data[1])
      phone_entry.insert(0,list_data[2])
      email_entry.insert(0,list_data[3])
      address_entry.insert(0,list_data[4])
      gender_entry.insert(0,list_data[5])
      dob_entry.insert(0,list_data[6])

def show_student():
      query="select*from student_1"
      mycursor.execute(query)
      fetched_data=mycursor.fetchall()
      student_table.delete(*student_table.get_children())
      for data in fetched_data:
            student_table.insert("",END,values=data)
      
def delete_student():
      indexing=student_table.focus()
      content=student_table.item(indexing)
      content_id=content["values"][0]
      query="delete from student_1 where id=%s"
      mycursor.execute(query,content_id)
      con.commit()
      messagebox.showinfo("Deleted",f"Id {content_id} is deleted successfully",parent=left_frm)

      query="select*from student_1"
      mycursor.execute(query)
      fetched_data=mycursor.fetchall()
      student_table.delete(*student_table.get_children())
      for data in fetched_data:
            student_table.insert("",END,values=data)
def search_student():
      def search_data():
            query=("select*from student_1 where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s")
            mycursor.execute(query,(id_entry.get(),name_entry.get(),email_entry.get(),phone_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get()))
            fetched_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for data in fetched_data:
                  data_list=list(data)
                  student_table.insert("",END,values=data_list)

      search_window=Toplevel()
      search_window.grab_set()
      search_window.title("Search Student")
      search_window.resizable(0,0)
      
      id_lbl=Label(search_window,text="Id",font=("times new roman",20,"bold"))
      id_lbl.grid(row=0,column=0,padx=30,pady=15,sticky=W)
      id_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      id_entry.grid(row=0,column=1,padx=15,pady=10)
      
      name_lbl=Label(search_window,text="Name",font=("times new roman",20,"bold"))
      name_lbl.grid(row=1,column=0,padx=30,pady=15,sticky=W)
      name_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      name_entry.grid(row=1,column=1,padx=15,pady=10)
      
      phone_lbl=Label(search_window,text="Phone",font=("times new roman",20,"bold"))
      phone_lbl.grid(row=2,column=0,padx=30,pady=15,sticky=W)
      phone_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      phone_entry.grid(row=2,column=1,padx=15,pady=10)
      
      email_lbl=Label(search_window,text="Email",font=("times new roman",20,"bold"))
      email_lbl.grid(row=3,column=0,padx=30,pady=15,sticky=W)
      email_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      email_entry.grid(row=3,column=1,padx=15,pady=10)
      
      address_lbl=Label(search_window,text="Address",font=("times new roman",20,"bold"))
      address_lbl.grid(row=4,column=0,padx=30,pady=15,sticky=W)
      address_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      address_entry.grid(row=4,column=1,padx=15,pady=10)
      
      gender_lbl=Label(search_window,text="Gender",font=("times new roman",20,"bold"))
      gender_lbl.grid(row=5,column=0,padx=30,pady=15,sticky=W)
      gender_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      gender_entry.grid(row=5,column=1,padx=15,pady=10)
      
      dob_lbl=Label(search_window,text="D.O.B.",font=("times new roman",20,"bold"))
      dob_lbl.grid(row=6,column=0,padx=30,pady=15,sticky=W)
      dob_entry=Entry(search_window,font=("times new roman",20,"bold"),width=24)
      dob_entry.grid(row=6,column=1,padx=15,pady=10)
      
      search_student_btn=ttk.Button(search_window,text="Search Student",width=20,command=search_data)
      search_student_btn.grid(row=7,columnspan=2,pady=10)
      
def add_student():
      def add_data():
            if id_entry.get()==""or name_entry.get()==""or phone_entry.get()==""or email_entry.get()==""or address_entry.get()=="" or gender_entry.get()=="" or dob_entry.get()=="":      
                  messagebox.showerror("Error","All fields are required",parent=add_window)    
            else:
                  try:
                        mycursor.execute("insert into student_1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_entry.get(),name_entry.get(),phone_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),date,current_time))
                        
                        con.commit()
                        
                        result=messagebox.askyesno("confirm","Data added succefully.Do You Want To Clean The Form",parent=add_window)
                        
                        if result:
                              id_entry.delete(0,END)
                              name_entry.delete(0,END)
                              phone_entry.delete(0,END)
                              email_entry.delete(0,END)
                              address_entry.delete(0,END)
                              gender_entry.delete(0,END)
                              dob_entry.delete(0,END) 
                        
                        else:
                              pass 
                  except:
                        messagebox.showerror("Error","Id can not be same",parent=add_window)
                        return
                  
                  query=("select*from student_1")
                  mycursor.execute(query)
                  fetched_data=mycursor.fetchall()
                  student_table.delete(*student_table.get_children())
                  for data in fetched_data:
                        datalist=list(data)
                        student_table.insert("",END,values=datalist)
                                          
      add_window=Toplevel()
      add_window.grab_set()
      add_window.title("Add Student")
      add_window.resizable(0,0)
      
      id_lbl=Label(add_window,text="Id",font=("times new roman",20,"bold"))
      id_lbl.grid(row=0,column=0,padx=30,pady=15,sticky=W)
      id_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      id_entry.grid(row=0,column=1,padx=15,pady=10)
      
      name_lbl=Label(add_window,text="Name",font=("times new roman",20,"bold"))
      name_lbl.grid(row=1,column=0,padx=30,pady=15,sticky=W)
      name_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      name_entry.grid(row=1,column=1,padx=15,pady=10)
      
      phone_lbl=Label(add_window,text="Phone",font=("times new roman",20,"bold"))
      phone_lbl.grid(row=2,column=0,padx=30,pady=15,sticky=W)
      phone_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      phone_entry.grid(row=2,column=1,padx=15,pady=10)
      
      email_lbl=Label(add_window,text="Email",font=("times new roman",20,"bold"))
      email_lbl.grid(row=3,column=0,padx=30,pady=15,sticky=W)
      email_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      email_entry.grid(row=3,column=1,padx=15,pady=10)
      
      address_lbl=Label(add_window,text="Address",font=("times new roman",20,"bold"))
      address_lbl.grid(row=4,column=0,padx=30,pady=15,sticky=W)
      address_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      address_entry.grid(row=4,column=1,padx=15,pady=10)
      
      gender_lbl=Label(add_window,text="Gender",font=("times new roman",20,"bold"))
      gender_lbl.grid(row=5,column=0,padx=30,pady=15,sticky=W)
      gender_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      gender_entry.grid(row=5,column=1,padx=15,pady=10)
      
      dob_lbl=Label(add_window,text="D.O.B.",font=("times new roman",20,"bold"))
      dob_lbl.grid(row=6,column=0,padx=30,pady=15,sticky=W)
      dob_entry=Entry(add_window,font=("times new roman",20,"bold"),width=24)
      dob_entry.grid(row=6,column=1,padx=15,pady=10)
      
      add_student_btn=ttk.Button(add_window,text="Add Student",width=20,command=add_data)
      add_student_btn.grid(row=7,columnspan=2,pady=10)
      
def connect_database():
      def connect():
            global mycursor,con
            try:
                  con=pymysql.connect(host="localhost",user="root",password="sandy713",database="student_database_management_system")
                  mycursor=con.cursor()    
            except:
                  messagebox.showerror("Error","Inavalid Details",parent=connect_database)
                  return
            try:    
                  # query="create database student_management_system"
                  # mycursor.execute(query)
                  
                  query="use student_database_management_system"
                  mycursor.execute(query)
                  
                  query="create table student_1(id int auto_increment not null primary key, name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))"
                  mycursor.execute(query)
      
            except:
                  query="use student_database_management_system "
                  mycursor.execute(query)
                  
            messagebox.showinfo("Success","Database Connection is Successfully",parent=connect_database)
            
            connect_database.destroy()
            
            add_student_btn.config(state=NORMAL)
            search_student_btn.config(state=NORMAL)   
            update_student_btn.config(state=NORMAL)
            show_student_btn.config(state=NORMAL)
            export_student_btn.config(state=NORMAL)
            delete_student_btn.config(state=NORMAL)
            
            
      connect_database=Toplevel()
      connect_database.grab_set()
      connect_database.geometry("500x250+700+250")
      
      connect_database.title("Database connection")
      connect_database.resizable(0,0)

      hostname_lbl=Label(connect_database,text="Host Name",font=("times new roman",20 ,"bold"))
      hostname_lbl.grid(row=0,column=0,padx=20,pady=10)

      hostname_entry=Entry(connect_database,font=("times new roman",20 ,"bold"),bd=2)
      hostname_entry.grid(row=0,column=1,padx=10,pady=10)

      username_lbl=Label(connect_database,text="Username",font=("times new roman",20 ,"bold"))
      username_lbl.grid(row=1,column=0,padx=20,pady=10)

      username_entry=Entry(connect_database,font=("times new roman",20 ,"bold"),bd=2)
      username_entry.grid(row=1,column=1,padx=10,pady=10)

      password_lbl=Label(connect_database,text="Password",font=("times new roman",20 ,"bold"))
      password_lbl.grid(row=2,column=0,padx=20,pady=10)

      password_entry=Entry(connect_database,font=("times new roman",20 ,"bold"),bd=2)
      password_entry.grid(row=2,column=1,padx=10,pady=10)

      connect_btn=ttk.Button(connect_database,text="CONNECT",width=20,command=connect)
      connect_btn.grid(row=3,columnspan=2,pady=20)
            
def clock():
      try:
            global date,current_time
            date=time.strftime("%d/%m/%Y")
            current_time=time.strftime("%H:%M:%S")
            datetime_lbl.config(text=f"    DATE:{date}\nTIME:{current_time}")
            datetime_lbl.after(1000,clock)
      except Exception as e:
            messagebox.showerror("error",f"Effor is due to{e}")


#gui window
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme("radiance")

root.geometry("1174x680+0+0")
root.resizable(0,0)
root.title("student management")

datetime_lbl=Label(root,font=("times new roman",18,"bold"))
datetime_lbl.place(x=5,y=5)
clock()

s="Student Management System"
slider_lbl=Label(root,text=s,font=("times new roman",28,"bold"),width=35)
slider_lbl.place(x=200,y=0)

connect_btn=ttk.Button(root,text="Connect Database",command=connect_database)
connect_btn.place(x=980,y=0)

#left frame
left_frm=Frame(root)
left_frm.place(x=30,y=80,width=300,height=600)

add_student_btn=ttk.Button(left_frm,text="Add Student",width=25,state=DISABLED,command=add_student)
add_student_btn.grid(row=1,column=0,pady=22)

search_student_btn=ttk.Button(left_frm,text="Search Student",width=25,state=DISABLED,command=search_student)
search_student_btn.grid(row=2,column=0,pady=22)

delete_student_btn=ttk.Button(left_frm,text="Delete Student",width=25,state=DISABLED,command=delete_student)
delete_student_btn.grid(row=3,column=0,pady=22)

update_student_btn=ttk.Button(left_frm,text="Update Student",width=25,state=DISABLED,command=update_student)
update_student_btn.grid(row=4,column=0,pady=22)

show_student_btn=ttk.Button(left_frm,text="Show Student",width=25,state=DISABLED,command=show_student)
show_student_btn.grid(row=5,column=0,pady=22)

export_student_btn=ttk.Button(left_frm,text="Export Data",width=25,state=DISABLED,command=export_student)
export_student_btn.grid(row=6,column=0,pady=22)

exit_btn=ttk.Button(left_frm,text="Exit",width=25,command=i_exit)
exit_btn.grid(row=7,column=0,pady=22)

#right frame
right_frm=Frame(root)
right_frm.place(x=350,y=80,width=820,height=600)

scrollbar_x=Scrollbar(right_frm,orient=HORIZONTAL)
scrollbar_y=Scrollbar(right_frm,orient=VERTICAL)

student_table=ttk.Treeview(right_frm,column=("Id","Name","Mobile No","Email","Address","Gender","D.O.B.","Added Date","Added Time"),xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

scrollbar_x.config(command=student_table.xview)
scrollbar_y.config(command=student_table.yview)

student_table.heading("Id",text="Id")
student_table.heading("Name",text="Name")
student_table.heading("Mobile No",text="Mobile No")
student_table.heading("Email",text="Email")
student_table.heading("Address",text="Address")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B.",text="D.O.B.")
student_table.heading("Added Date",text="Added Date")
student_table.heading("Added Time",text="Added Time")

student_table.column("Id",width=35,anchor=CENTER)
student_table.column("Name",width=300,anchor=CENTER)
student_table.column("Mobile No",width=200,anchor=CENTER)
student_table.column("Email",width=300,anchor=CENTER)
student_table.column("Address",width=300,anchor=CENTER)
student_table.column("Gender",width=150,anchor=CENTER)
student_table.column("D.O.B.",width=150,anchor=CENTER)
student_table.column("Added Date",width=150,anchor=CENTER)
student_table.column("Added Time",width=150,anchor=CENTER)


style=ttk.Style()
style.configure("Treeview",rowheight=35,font=("aerial",12),foreground="black",background="white",fieldbackground="white")
style.configure("Treeview.Heading",font=("aerial",12,),foreground="black",background="white",fieldbackground="white")

student_table.config(show="headings")

scrollbar_x.pack(side=BOTTOM, fill=X)
scrollbar_y.pack(side=RIGHT,fill=Y)

student_table.pack(fill=BOTH,expand=1)
 
root.mainloop()












