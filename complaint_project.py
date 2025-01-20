#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
from datetime import date
import random


# In[2]:


pip install psycopg2


# In[3]:


import psycopg2 as db


# In[4]:


pip install tkcalender


# In[5]:


pip install tk


# In[6]:


from tkinter import ttk
from tkinter.ttk import *


# In[7]:


pip install tkcalendar


# In[8]:


from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
import re


# In[9]:


conn = db.connect(
    database="postgres",
    user = "postgres",
    host="localhost",
    password = "ishika",
    port =5432
                  )

cur = conn.cursor()


# In[ ]:





# In[ ]:





# In[ ]:


frame = Tk()
frame.title('Complaint Registration')
frame.geometry('500x500')
w = Canvas(frame,width=200, height=200)
w.pack()


def validatePassword(password):
    
#     pattern = re.compile(r'')
    if(len(password)<6):
        return False
    elif re.search(r'[!@#$%&]',password) is None:
        return False
    elif re.search(r'\d',password) is None:
        return False
    elif re.search(r'[A-Z]',password) is None:
        return False
    elif re.match(r'[a-z A_Z 0-9 !@#$%&]{6}',password):
#         pattern= re.compile(r'[a-z A_Z 0-9 !@#$%&]{6}',password)
#         result = pattern.match(password)
        return True

def user_registration():
    
    wind3=Toplevel(frame)
    wind3.title("user registration")
    wind3.geometry("300x300")
    
    def register_entry():
        randvar= random.randint(1,100)
        userid=str(randvar)+users_entry.get()
        paswd=passwords_entry.get()
        usernam=users_entry.get() 
        check = validatePassword(paswd)
        if(check == False):
            messagebox.showwarning('WARNING','MAKE PASSWORD CORRECT AND  STRONG')
        else:
            if(passwords_entry.get()==passwords_confirm.get()):
                cur.execute('''insert into users (user_id, user_name, passwords) values (%s,%s,%s)''',(userid,usernam,paswd))
                conn.commit()
                wind3.destroy()
            else:
                passwords_entry.delete(0,END)
                passwords_confirm.delete(0,END)
                messagebox.showerror('error','Password does not match')

        
        
    registration_label=Label(wind3,text="user name")
    registration_label.pack()
    users_entry=Entry(wind3)
    users_entry.pack()
    passwords_label=Label(wind3,text="password")
    passwords_label.pack()
    passwords_entry=Entry(wind3,show="*")
    passwords_entry.pack()
    password_confirm=Label(wind3,text="confirm password")
    password_confirm.pack()
    passwords_confirm=Entry(wind3,show="*")
    passwords_confirm.pack()
    Signup = Button(wind3,text="Sign Up",command=lambda : register_entry())
    Signup.pack()
    
def user_login():
    def complaint_register(userID):
        
        
        
        def insert_complaint():
            wind8 = Toplevel(frame)
            wind8.title("Insert Complain")
            wind8.geometry('300x300')
            domainlab = Label(wind8,text="Domain")
            domainlab.pack()
            domain = Combobox(wind8,values=['financial','technical','educational','others'])
            domain.pack()
            complaint_label=Label(wind8,text="complain")
            complaint_label.pack()
            checkingtext = Text(wind8,height=5,width=30)
            checkingtext.pack() 
            
            def insert():
                dom = domain.get()
                compy=checkingtext.get("1.0",'end-1c')
                todo=date.today()
                randvar= random.randint(1000,9999)
                try:
                    cur.execute('''insert into complaint (comp_id,comp_date,comp_text,user_id,domains,status) 
                    values (%s,%s,%s,%s,%s,'initiated');''',(randvar,todo,compy,userID,dom))
                    conn.commit()
                    wind8.destroy()
                    messagebox.showinfo("Added","Complain Added")
                except db.DatabaseError as error:
                    conn.rollback()
                    print(error)
                    wind8.destroy()
               
                
                
                
            but = Button(wind8,text="Submit",command= lambda : insert())
            but.pack()
            
        
        def showStatus():
            count =0
            wind9 = Toplevel(frame)
            tree=ttk.Treeview(wind9,selectmode="extended")
            tree.pack(padx=50,pady=20)
            
            tree['columns'] = ('Complain date','Complain','User ID','Domain','Status')
            
            tree.column('#0',anchor=CENTER,stretch=NO,width=100)
            tree.column('Complain date',anchor=CENTER,stretch=NO,width=100)
            tree.column('Complain',anchor=CENTER,stretch=NO,width=300)
            tree.column('User ID',anchor=CENTER,stretch=NO,width=100)
            tree.column('Domain',anchor=CENTER,stretch=NO,width=100)
            tree.column('Status',anchor=CENTER,stretch=NO,width=100)
            
            tree.heading('#0')
            tree.heading('Complain date',text='Complain Date')
            tree.heading('Complain',text='Complain')
            tree.heading('User ID',text='User ID')
            tree.heading('Domain',text='Domain')
            tree.heading('Status',text='Status')
            try:
                cur.execute("Select comp_date, comp_text,user_id,domains,status from complaint where user_id = '{0}'; ".format(userID))
                val = cur.fetchall()
                for i in val:
                    tree.insert('','end',iid=count,values=(i[0],i[1],i[2],i[3],i[4]))
                    count+=1
            except db.DatabaseError as error:
                conn.rollback()
                print(error)
            

            
        
            
            
           
            
        wind2=Toplevel(frame)
        wind2.title("complaint registration")
        wind2.geometry("300x300")
        addcomplain = Button(wind2,text="Add Complain",command=lambda : insert_complaint() )
        addcomplain.pack()
        showStatus = Button(wind2, text="Show Status", command= showStatus)
        showStatus.pack()
        
        
        
        
    
    def user_authenticate():
        user_name=user_entry.get()
        password=password_entry.get()
        cur.execute('Select * from users where user_name = %s and passwords = %s',[user_name,password])
        result=cur.fetchall()
        print(result)
        if(len(result)>0):
            if(result[0][2]==password):
                print('success')
                wind1.destroy()
                complaint_register(result[0][0])
               
        else:
             messagebox.showerror('error','error:wrong input')
            
        
    wind1=Toplevel(frame)
    wind1.title("user login")
    wind1.geometry('300x300')
    user_label=Label(wind1,text="user name")
    user_label.pack()
    user_entry=Entry(wind1)
    user_entry.pack()
    password_label=Label(wind1,text="password")
    password_label.pack()
    password_entry=Entry(wind1,show="*")
    password_entry.pack()
    sub_button=Button(wind1,text="submit",command=user_authenticate)
    sub_button.pack()
    
    
    
    
    
    
    
def adminOption(adminId):
    def deleteComplain():
        count =0
        wind5=Toplevel(frame)
        tree=ttk.Treeview(wind5,selectmode="extended")
        tree.pack(padx=50,pady=20)
        
        tree['columns'] = ('Complaint Id','Complaint Date', 'Complaint', 'User Id','Domain','Status')
            
        tree.column('#0',anchor= CENTER,stretch=NO)
        tree.column('Complaint Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint Date',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint',anchor=CENTER,stretch=NO,width=300)
        tree.column('User Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Domain',anchor=CENTER,stretch=NO,width=100)
        tree.column('Status',anchor=CENTER,stretch=NO,width=100)
            
        tree.heading('#0')
        tree.heading('Complaint Id',text='comp_id')
        tree.heading('Complaint Date',text='comp_date')
        tree.heading('Complaint',text='comp_text')
        tree.heading('User Id',text='user_id')
        tree.heading('Domain',text='Domain')
        tree.heading('Status',text='Status')
        
        cur.execute('select * from complaint order by comp_id;')
        result = cur.fetchall()
        for i in result:
            tree.insert('','end',iid=count,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            count+=1
        
        dataframe = LabelFrame(wind5,text="Operations")
        dataframe.pack(fill='x',expand="yes", padx=20)
        
        complaintLabel = Label(dataframe,text='Complaint')
        complaintLabel.grid(row=0,column=0,padx=30,pady=10)
        complaint = Entry(dataframe)
        complaint.grid(row=0,column=1,padx=30,pady=10)
        compIdLabel = Label(dataframe,text="Complaint ID")
        compIdLabel.grid(row=0,column=2,padx=30,pady=10)
        compId = Entry(dataframe)
        compId.grid(row=0,column=3,padx=30,pady=10)
        
        def selectedRecord(e):
            complaint.delete(0,END)
            compId.delete(0,END)
            
            selected = tree.focus()
            valuess = tree.item(selected,'values')
            
            complaint.insert(0,valuess[2])
            compId.insert(0,valuess[0])
            
        def deleteData():
            compID = int(compId.get())
            try: 
                cur.execute('delete from complaint where comp_id = {0};'.format(compID))
                conn.commit()
                wind5.destroy()
                deleteComplain()
                
            except db.DatabaseError as error:
                conn.rollback()
                print(error)
                
        
        tree.bind("<ButtonRelease-1>",selectedRecord)
        
        dltButton = Button(dataframe,text="Delete",command=deleteData)
        dltButton.grid(row=1,column=0,padx=30,pady=10)
        
        
    
    
    
        
    def show_complaint():
    
        count =0
        wind=Toplevel(frame)
        tree=ttk.Treeview(wind,selectmode="extended")
        tree.pack(padx=50,pady=20)
            
        tree['columns'] = ('Complaint Id','Complaint Date', 'Complaint', 'User Id','Domain','Status')
            
#         tree.column('#0',anchor= CENTER,stretch=NO)
        tree.column('Complaint Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint Date',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint',anchor=CENTER,stretch=NO,width=300)
        tree.column('User Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Domain',anchor=CENTER,stretch=NO,width=100)
        tree.column('Status',anchor=CENTER,stretch=NO,width=100)
            
#         tree.heading('#0')
        tree.heading('Complaint Id',text='comp_id')
        tree.heading('Complaint Date',text='comp_date')
        tree.heading('Complaint',text='comp_text')
        tree.heading('User Id',text='user_id')
        tree.heading('Domain',text='Domain')
        tree.heading('Status',text='Status')
        
        def searching(selected):
            count =0
            dates = str(selected) 
            if(tree.get_children()):
                for i in tree.get_children():
                    tree.delete(i)
            try: 
                cur.execute('''select * from complaint where comp_date = '{0}' ;'''.format(dates))
                rows=cur.fetchall()
                for i in rows:
                    tree.insert('','end',iid = count,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
                    count+=1
            except db.DatabaseError as error:
                conn.rollback()
                print(error)
       
        
        newframe = LabelFrame(wind,text="Filter")
        newframe.pack()
        datelabel = Label(newframe,text="Date")
        datelabel.grid(row=0,column=0,pady=30,padx=20)
        dates= DateEntry(newframe,selectmode ='day')
        dates.grid(row=0,column=1,pady=30,padx=20)
        
        def cleardata():
            dates.delete(0,END)
            
        
        cleardata()
        search = Button(newframe,text="Search",command= lambda : searching(dates.get_date()))
        search.grid(row=0,column=2,pady=30,padx=20)
        clearlabel = Button(newframe, text="Clear",command=cleardata)
        clearlabel.grid(row=0,column=3,pady=30,padx=20)
        
    def adminReg():
        wind6 = Toplevel(frame)
        wind6.title("Register")
        wind6.geometry('300x300')
        adminIdLabel = Label(wind6,text="Admin Id")
        adminIdLabel.pack()
        AdminID = Entry(wind6)
        AdminID.pack()
        Passlabel = Label(wind6,text="Password")
        Passlabel.pack()
        PassEntry = Entry(wind6)
        PassEntry.pack()
        
        def addAdmin():
            admin = AdminID.get()
            password = PassEntry.get()
            check=validatePassword(password)
            if(check == False):
                 messagebox.showwarning('WARNING','MAKE PASSWORD STRONG')
            else:
                try: 
                    cur.execute('insert into admin (admin_id,admin_pass) values(%s,%s);',(admin,password))
                    conn.commit()
                    messagebox.showinfo('Success', 'Admin Registered Successfully')
                    wind6.destroy()

                except db.DatabaseError as error:
                    conn.rollback()
                    print(error)
        
        Approved = Button(wind6,text="Approved",command= lambda :  addAdmin())
        Approved.pack()
        
    def historyShow():
        count =0
        wind6=Toplevel(frame)
        wind6.title(" complain history")
        tree=ttk.Treeview(wind6,selectmode="extended")
        tree.pack(padx=50,pady=20)
            
        tree['columns'] = ('Complaint Id','Complaint Date', 'Complaint', 'User Id','Domain','Status')
            
#         tree.column('#0',anchor= CENTER,stretch=NO)
        tree.column('Complaint Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint Date',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint',anchor=CENTER,stretch=NO,width=300)
        tree.column('User Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Domain',anchor=CENTER,stretch=NO,width=100)
        tree.column('Status',anchor=CENTER,stretch=NO,width=100)
            
#         tree.heading('#0')
        tree.heading('Complaint Id',text='comp_id')
        tree.heading('Complaint Date',text='comp_date')
        tree.heading('Complaint',text='comp_text')
        tree.heading('User Id',text='user_id')
        tree.heading('Domain',text='Domain')
        tree.heading('Status',text='Status')
        
        def searching(selected,toSelected):
            count =0
            dates = str(selected) 
            dates2 = str(toSelected)
            if(tree.get_children()):
                for i in tree.get_children():
                    tree.delete(i)
            try: 
                cur.execute('''select * from complaint where comp_date between '{0}' and '{1}'; ;'''.format(dates,dates2))
                rows=cur.fetchall()
                for i in rows:
                    tree.insert('','end',iid = count,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
                    count+=1
            except db.DatabaseError as error:
                conn.rollback()
                print(error)
       
        
        newframe = LabelFrame(wind6,text="Filter")
        newframe.pack()
        datelabel = Label(newframe,text="From Date")
        datelabel.grid(row=0,column=0,pady=30,padx=20)
        fromdates= DateEntry(newframe,selectmode ='day')
        fromdates.grid(row=0,column=1,pady=30,padx=20)
        todateLabel = Label(newframe,text="To Date")
        todateLabel.grid(row=0,column=2,pady=30,padx=20)
        todate = DateEntry(newframe,selectmode ='day')
        todate.grid(row=0,column=3,pady=30,padx=20)
        
        
        def cleardata():
            todate.delete(0,END)
            fromdates.delete(0,END)    
        
        cleardata()
        search = Button(newframe,text="Search",command= lambda : searching(fromdates.get_date(),todate.get_date()))
        search.grid(row=1,column=0,pady=30,padx=20)
        clearlabel = Button(newframe, text="Clear",command=cleardata)
        clearlabel.grid(row=1,column=1,pady=30,padx=20)
        
    def update():
        count=0
        wind7=Toplevel(frame)
        wind7.title("Update Status")
        tree=ttk.Treeview(wind7,selectmode="extended")
        tree.pack(padx=50,pady=20)
            
        tree['columns'] = ('Complaint Id','Complaint Date', 'Complaint', 'User Id','Domain','Status')
            
#         tree.column('#0',anchor= CENTER,stretch=NO)
        tree.column('Complaint Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint Date',anchor=CENTER,stretch=NO,width=100)
        tree.column('Complaint',anchor=CENTER,stretch=NO,width=300)
        tree.column('User Id',anchor=CENTER,stretch=NO,width=100)
        tree.column('Domain',anchor=CENTER,stretch=NO,width=100)
        tree.column('Status',anchor=CENTER,stretch=NO,width=100)
            
#         tree.heading('#0')
        tree.heading('Complaint Id',text='comp_id')
        tree.heading('Complaint Date',text='comp_date')
        tree.heading('Complaint',text='comp_text')
        tree.heading('User Id',text='user_id')
        tree.heading('Domain',text='Domain')
        tree.heading('Status',text='Status')
        
        cur.execute('select * from complaint order by comp_id;')
        result = cur.fetchall()
        for i in result:
            tree.insert('','end',iid=count,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
            count+=1
            
        newNew = LabelFrame(wind7,text="Filter")
        newNew.pack(fill='x',expand="yes", padx=20)
        
        compid = Entry(newNew)
        domainLabel = Label(newNew,text="Domain")
        domainLabel.grid(row=0,column=0,padx=30,pady=10)
        domain = Entry(newNew)
        domain.grid(row=0,column=1,padx=30,pady=10)
        complaintLabel = Label(newNew,text='Complaint')
        complaintLabel.grid(row=0,column=2,padx=30,pady=10)
        complaint = Text(newNew,width=20,height=10)
        complaint.grid(row=0,column=3,padx=30,pady=10)
        statLabel = Label(newNew,text="Status")
        statLabel.grid(row=0,column=4,padx=30,pady=10)
        status = Combobox(newNew,values=["initiated","under process","resolved"])
        status.grid(row=0,column=5,padx = 30,pady=10)
        
        def selectRecord(e):
            compid.delete(0,END)
            domain.delete(0,END)
            complaint.delete('1.0',"end")
            status.delete(0,END)
            
            selected = tree.focus()
            valuess = tree.item(selected,'values')
            print(valuess)
            
            compid.insert(0,valuess[0])
            domain.insert(0,valuess[4])
            complaint.insert("1.0",valuess[2])
            status.insert(0,valuess[5])
            
        def cleardata():
            domain.delete(0,END)
            complaint.delete('1.0',"end")
        
        def updateQuery():
            comp = int(compid.get())
            Stat = status.get()
            try:
                cur.execute("update complaint set status = '{0}' where comp_id ={1};".format(Stat,comp))
                conn.commit()
                wind7.destroy()
                messagebox.showinfo("Congratulation","Status Updated")
#                 update()
            except db.DatabaseError as error:
                conn.rollback()
                print(error)
                wind7.destroy()
                update()
            
            
        
        newframes = LabelFrame(wind7,text="buttons")
        newframes.pack(fill='x',expand="yes", padx=20)
        update=  Button(newframes,text="Update",command= lambda : updateQuery())
        update.grid(row=0,column=0,padx=30,pady=20)
        clear = Button(newframes,text="Clear",command= lambda: cleardata())
        clear.grid(row=0,column=1,padx=30,pady=20)
        
        tree.bind("<ButtonRelease-1>",selectRecord)
        
  
         
    wind4 = Toplevel(frame)
    wind4.title("Options")
    wind4.geometry('300x300')
    showButton = Button(wind4,text='Show Complain',command = lambda : show_complaint())
    showButton.pack()
    deleteButton = Button(wind4,text="Delete Complain", command = lambda : deleteComplain())
    deleteButton.pack()
    adminRegister = Button(wind4,text="Admin Register",command= lambda: adminReg())
    adminRegister.pack()
    updateStatus = Button(wind4,text="Update Status", command= lambda: update())
    updateStatus.pack()
    history = Button(wind4,text="History",command = lambda : historyShow())
    history.pack()
     

def login():
    

    first=Toplevel(frame)
    def authenticate():
        adminId = admin_id.get()
        adminPassword = Admin_password.get()
        if adminId == 'null' or adminPassword == "null":
            messagebox.showerror('error','error:wrong ')
           
        else:
            cur.execute('Select * from admin where admin_id = %s and admin_pass = %s',[adminId,adminPassword])
            rows = cur.fetchall();
            if(len(rows)>0):
                if(rows[0][1]==adminPassword):
                    print('success')
                    ##first.destroy()
                    adminOption(adminId)
            else:
                messagebox.showerror('error','error:wrong input')
            print(adminId)
    first.title('admin login')
    first.geometry('300x300')
    AdminLabel = Label(first,text="Admin Id")
    AdminLabel.pack()
    admin_id = Entry(first)
    admin_id.pack()
    Admin_pass_label = Label(first,text='Password')
    Admin_pass_label.pack()
    Admin_password = Entry(first,show='*')
    Admin_password.pack()

    Admin_submit = Button(first,text="Submit",command=lambda:authenticate())
    Admin_submit.pack()

l = Label(frame, text="Complaint Registeration",)
l.pack()
AdminLogin = Button(frame,text='Admin Login', command=login)
AdminLogin.pack()
UserLogin = Button(frame,text="User Login",command=user_login)
UserLogin.pack()
UserRegister=Button(frame,text="user registration",command=user_registration)
UserRegister.pack()

frame.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




