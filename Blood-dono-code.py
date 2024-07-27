import tkinter as tk
from tkinter import*
from tkinter import messagebox
import mysql.connector
#sql connection
conn=mysql.connector.connect(host="localhost",user="root",password="pw",database="blooddonation")
cursor=conn.cursor()

a=tk.Tk()
a.geometry("1500x1500")  
a.title("Blood donation forum")
a.configure(background="White")
label1=Label(a,text=" APV Blood Donation ",font=("Eras Bold ITC",30,"italic")).place(x=0,y=0)
label2=Label(a, text = "''The blood you donate gives someone another chance at life.\n One day that someone maybe a close relative ,a friend,a loved one- or even you.''", bd = 10, fg = "red", font =("Harlow Solid Italic",35,"italic"))  
label2.place(x=0,y=60)
label3=Label(a,text=" Project initiated by \nJanani\nSneha\nSrilakshmi ",font=("Calibri",15,"italic")).place(x=1300,y=700)
bg=PhotoImage(file ="pic1.png")
Label( a, image = bg).place(x=500,y=200)

def window1():
    w=tk.Toplevel(a)
    w.geometry('1500x1500')
    w.configure(background="#FFF39A")
    Label(w,text=" APV Blood Donation ",fg = "#800000", bg = "#FFF39A",font=("Eras Bold ITC",30,"italic")).place(x=60,y=0)
    Label(w, text = "SEARCH FOR DONOR", fg = "#800000", bd = 40, bg = "#FFF39A", font =("Showcard Gothic",50,"bold","italic")).place(x=100,y=50)
    bg=PhotoImage(file ="pic2.png")
    label1=Label( w, image = bg).place(x=900,y=0)

    label2=Label(w,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",width=10, fg = "green",bg = "#FFF39A")
    label2.grid(row=0,column=0)
    
    Button(w, text="Return to Home screen",bd=5, fg='black',font =("Comic Sans MS",20,"bold"),
                              command=lambda:w.destroy()).place(x=950,y=700)
    
    def callmyfunc(*args):
         cursor.execute("select Name,City,Bloodgroup, Gender,Phone_No,Allergies from bloodgroup where Bloodgroup= '{}'".format(a1.get()))
         data=cursor.fetchall()
         r1=Label(w,text="NAME",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=1)
         r2=Label(w,text="CITY",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=2)
         r7=Label(w,text="BLOODGROUP",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=3)
         r3=Label(w,text="GENDER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=4)
         r4=Label(w,text="PHONE NUMBER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=5)
         r9=Label(w,text="ALLERGIES",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=6)
         i=6
         for info in data:
             for j in range(len(info)):
                 e = Entry(w, width=20, fg='blue',font =("Trebuchet MS",15,"italic")) 
                 e.grid(row=i, column=j+1)
                 e.insert(END, info[j])
             i+=1
        
             conn.commit()
    optlist=["Select required blood group:",
    "A+ve",
    "B+ve",
    "A-ve",
    "B-ve",
    "O+ve",
    "O-ve",
    "AB+ve",
    "AB-ve",
    "Rh null"]
    a1=tk.StringVar()
    a1.set(optlist[0])
    opt=tk.OptionMenu(w,a1,*optlist,command=callmyfunc)
    opt.place(x=150,y=200)
    w.mainloop()

#Window2
def window2():
    from tkinter import messagebox
    w= tk.Toplevel(a)
    w.configure(background="#FFF39A")
    w.geometry('1500x1500')
    Label(w,text=" APV Blood Donation ",fg="#800000",bg="#FFF39A",font=("Eras Bold ITC",30,"italic")).place(x=60,y=0)
    Label(w,text=" Project initiated by \nJanani\nSneha\nSrilakshmi ",fg="#800000",bg="#FFF39A",font=("Calibri",15,"italic")).place(x=1300,y=700)
    Label(w, text = "DONOR DETAILS", fg = "#800000", bd = 40, bg = "#FFF39A", font =("Showcard Gothic",50,"bold","italic")).place(x=100,y=50)
    
    bg2=PhotoImage(file ="pic10.png")
    label1=Label( w, image = bg2).place(x=800,y=0)
    Button(w, text="Return to Home screen",bd=5, fg='black',font =("Comic Sans MS",15,"bold"),
                              command=lambda:w.destroy()).place(x=1000,y=700)
   
    #For name
    name=tk.StringVar(w)
    lb= Label(w, text = "Name:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
    lb.place(anchor='nw',x=100,y=250)
    i=tk.Entry(w, textvariable=name,width=30)
    i.place(anchor='nw',x=100,y=300)
   
    #For city
    city=tk.StringVar(w)
    lb1=tk.Label(w,text="City:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
    lb1.place(x=600,y=360)
    i1=tk.Entry(w,textvariable=city,width=30)
    i1.place(anchor='nw',x=600,y=420)

    #For bloodgroup
    optlist=[
    "Select your blood group:",
    "A+ve",
    "B+ve",
    "A-ve",
    "B-ve",
    "O+ve",
    "O-ve",
    "AB+ve",
    "AB-ve",
    "Rh null"]
    a1=tk.StringVar(w)
    a1.set(optlist[0])
    opt=tk.OptionMenu(w,a1,*optlist)
    opt2=StringVar(opt)
    opt.config(width=20,fg='black',)
    opt.place(anchor='nw',x=100,y=400)
    lb2=tk.Label(w,text="Blood group:",bg='#FFF39A',font =("Trebuchet MS",25,"italic"),fg="black")
    lb2.place(x=100,y=350)
   
    #For Age
    age=tk.StringVar(w)
   
    lb3=Label(w,text='Age:',font =("Trebuchet MS",25,"italic"),fg="black",bg='#FFF39A',)
    lb4=Entry(w,textvariable=age,width=30)
    lb3.place(x=100,y=450)
    lb4.place(x=100,y=500)
   
   
    #For gender
    options=["Male","Female","Other"]
    a2=tk.StringVar()
    a2.set("Select your gender")
    opt1=OptionMenu(w,a2,*options)
    opt1.place(x=600,y=300)
    lb6=Label(w,text="Gender:",bg='#FFF39A',font=("Trebuchet MS",25,"italic"))
    lb6.place(x=600,y=250)

    #Contact details
    phonenumber=tk.StringVar(w)
   
    lb7=tk.Label(w,text="Phone number:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
    lb8=tk.Label(w,text="(Enter 10 digit no.)",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",10,"italic"))
    lb7.place(x=600,y=450)
    lb8.place(x=800,y=495)
    i2=tk.Entry(w,textvariable=phonenumber,width=30)
    i2.place(x=600,y=500)
    
    # For Allergies
    allergies=tk.StringVar(w)
    lb9=tk.Label(w,text="Allergies:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
    lb9.place(x=600,y=520)
    i3=tk.Entry(w,textvariable=allergies,width=30)
    i3.place(x=600,y=570)

    #Password
    Password=tk.StringVar(w)
    #lb10=tk.Label(w,text="Create an account ny entering password",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic")).place(x=600,y=550)
    lb10=tk.Label(w,text="Password:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
    lb10.place(x=600,y=600)
    i4=tk.Entry(w,textvariable=Password,width=30)
    i4.place(x=600,y=650)
    
    def ok():
        donorage=age.get()
        name1=name.get()
        city1=city.get()
        allergies1=allergies.get()
        gender=a2.get()
        bg=a1.get()
        p=Password.get()
        phonenumber1=phonenumber.get()
        if int(donorage)<12:
            messagebox.showerror(w, "You cannot donate blood: Underage:(")
        elif phonenumber1=="" or (int(len(phonenumber1))!=10):
            messagebox.showerror(w,"Phone number field is empty or is not 10 digits")
        elif  name1=="" or city1=="" or phonenumber1=="" or bg=="Select blood group" or gender=="Select your gender" or allergies1=="":
            messagebox.showerror(w,"Error ,One field is empty") 
        else:
            age.set("")
            name.set("")
            city.set("")
            phonenumber.set("")
            allergies.set("")
            a1.set("")
            a2.set("")
            Password.set("")
            #cursor.execute("CREATE TABLE  bloodgroup (Name VARCHAR (30),Bloodgroup TEXT,Age INT,Gender TEXT,City VARCHAR(20),Phone_No VARCHAR(10) ,Allergies VARCHAR(30),Password Varchar(20) )")
            insert= "INSERT INTO bloodgroup(Name ,Bloodgroup ,Age,Gender,City ,Phone_No ,Allergies,Password)""VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
            data = (name1,bg,donorage,gender,city1,phonenumber1,allergies1,p)
          
            cursor.execute(insert, data)
            conn.commit()
            messagebox.showinfo(w,"---RECORD ADDED---")
            w.destroy()
          
            
    Button(w,text="Submit",font=("Trebuchet MS",25,"italic"),command=ok).place(x=850,y=600)
    lb10=tk.Label(w,text="*All of the above fields are required.",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",10,"italic"))
    lb10.place(x=1000,y=600)
    w.mainloop()
def window3():
    w3= tk.Toplevel(a)
    w3.configure(background="#FFF39A")
    w3.geometry('900x900')
    cursor.execute("drop table if exists login")
    cursor.execute("create table login(Phone_No varchar(10) not null,Password varchar(30) not null)")
    Label(w3, text = "Login Page", fg = "#800000", bd = 40, bg = "#FFF39A", font =("Showcard Gothic",50,"bold","italic")).place(x=130,y=30)
    Phone=tk.StringVar(w3)
    lb1=tk.Label(w3,text="Phone Number:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic")).place(x=50,y=200)
    phone=tk.Entry(w3,textvariable=Phone,width=30).place(x=350,y=200)
    Pw=tk.StringVar(w3)
    lb1=tk.Label(w3,text="Password:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic")).place(x=50,y=300)    
    pw1=tk.Entry(w3,textvariable=Pw,show="*",width=30).place(x=350,y=300)
    Cpw=tk.StringVar(w3)
    lb1=tk.Label(w3,text="Confirm Password:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic")).place(x=50,y=400)
    pw2=tk.Entry(w3,textvariable=Cpw,show="*",width=30).place(x=350,y=400)
    Button(w3, text="Return to Home screen",bd=5, fg='black',font =("Comic Sans MS",20,"bold"),
                              command=lambda:w3.destroy()).place(x=500,y=700)
    def submit():
        Pw1=Pw.get()
        Phone1=Phone.get()
        cursor.execute('select phone_no,password from bloodgroup')
        data=cursor.fetchall()
        for i in data:
            if  i[0]==Phone1 and i[1]==Pw1:
                w3.destroy()
                def window4(*args):
                    Pw1=Pw.get()
                    Cpw1=Cpw.get()
                    Phone1=Phone.get()
                    if Cpw1==Pw1:
                        w=tk.Toplevel(a)
                        w.geometry('1500x1500')
                        w.configure(background="#FFF39A")
                        l2=Label(w,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",width=10, fg = "green",bg = "#FFF39A")
                        l2.grid(row=0,column=0)
                        cursor.execute("insert into login values('{}','{}')".format(Phone1,Pw1))
                        cursor.execute("select name,city, age, gender,phone_no,allergies,password  from bloodgroup natural join login where bloodgroup.Password=login.Password")
                        data=cursor.fetchall()
                        l1=Label(w, text = "Welcome!", fg = "#800000", bd = 40, bg = "#FFF39A", font =("Showcard Gothic",50,"bold","italic"))
                        l1.place(x=100,y=50)
                            
                        r1=Label(w,text="NAME",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=1)
                        r2=Label(w,text="CITY",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=2)
                        r9=Label(w,text="AGE",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=3)
                        r3=Label(w,text="GENDER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=4)
                        r4=Label(w,text="PHONE NUMBER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=5)
                        r5=Label(w,text="ALLERGIES",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=6)
                        r6=Label(w,text="PASSWORD",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=7)
                        i=7
                        for info in data:
                              for j in range(len(info)):
                                     e = Entry(w, width=20, fg='blue',font =("Trebuchet MS",15,"italic")) 
                                     e.grid(row=i, column=j+1)
                                     e.insert(END, info[j])
                              i+=1
                    else:
                        messagebox.showerror(w3,"Invalid Password")
                    cursor.execute("Select name,age,city,phone_no,allergies,password from bloodgroup")
                    data=cursor.fetchall()
                    def update():
                         cursor.execute("Select name,age,city,phone_no,allergies,password from bloodgroup natural join login where bloodgroup.password=login.password")
                         data=cursor.fetchall()
                         for i in data:
                              name1=i[0]
                              age1=i[1]
                              city1=i[2]
                              phone1=i[3]
                              allergies1=i[4]
                              password1=i[5]
                         lb=Label(w, text = "Update the details here:",bg='#FFF39A',fg = "Blue",  font =("Trebuchet MS",35,"italic"))
                         lb.place(x=100,y=400)
                        
                         #For name
                         name=tk.StringVar(w)
                         name.set(name1)
                         lb1=Label(w, text = "Name:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
                         lb1.place(x=20,y=500)
                         a1=tk.Entry(w, textvariable=name,width=30)
                         a1.place(x=150,y=500)
                         #Age
                         age=tk.StringVar(w)
                         age.set(age1)
                         lb2=Label(w,text='Age:',font =("Trebuchet MS",25,"italic"),fg="black",bg='#FFF39A')
                         a2=Entry(w,textvariable=age,width=30)
                         lb2.place(x=20,y=550)
                         a2.place(x=150,y=550)
                         #For city
                         city=tk.StringVar(w)
                         city.set(city1)
                         lb3=Label(w,text="City:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
                         lb3.place(x=20,y=600)
                         a3=tk.Entry(w,textvariable=city,width=30)
                         a3.place(x=150,y=600)
                         #Contact details
                         phonenumber=tk.StringVar(w)
                         phonenumber.set(phone1)
                         lb4=tk.Label(w,text="Phone number:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
                         lb4.place(x=340,y=500)
                         a4=tk.Entry(w,textvariable=phonenumber,width=30)
                         a4.place(x=600,y=500)
                         # For Allergies
                         allergies=tk.StringVar(w)
                         allergies.set(allergies1)
                         lb5=tk.Label(w,text="Allergies:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
                         lb5.place(x=340,y=550)
                         a5=tk.Entry(w,textvariable=allergies,width=30)
                         a5.place(x=600,y=550)
                         #Password
                         Password=tk.StringVar(w)
                         Password.set(password1)
                         lb6=tk.Label(w,text="Password:",bg='#FFF39A',fg = "Black",  font =("Trebuchet MS",25,"italic"))
                         lb6.place(x=340,y=600)
                         a6=tk.Entry(w,textvariable=Password,width=30)
                         a6.place(x=600,y=600)
                        
                         
                         def done():

                             nm=a1.get()
                             ag=a2.get()
                             ct=a3.get()
                             pn=a4.get()
                             allg=a5.get()
                             pw=a6.get()
                             sql = "Update  bloodgroup set Name= %s,Age= %s,City= %s,Phone_No= %s,Allergies= %s,Password= %s"
                             val = (nm,ag,ct,pn,allg,pw)
                             cursor.execute(sql, val)
                             conn.commit()
                             l2=Label(w,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",width=10, fg = "green",bg = "#FFF39A")
                             l2.grid(row=0,column=0)
                             cursor.execute("select name,city, age, gender,phone_no,allergies,password  from bloodgroup ")
                             data=cursor.fetchall()
                             l1=Label(w, text = "Welcome", fg = "#800000", bd = 40, bg = "#FFF39A", font =("Showcard Gothic",50,"bold","italic"))
                             l1.place(x=100,y=50)
                             r1=Label(w,text="NAME",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=1)
                             r2=Label(w,text="CITY",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=2)
                             r9=Label(w,text="AGE",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=3)
                             r3=Label(w,text="GENDER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=4)
                             r4=Label(w,text="PHONE NUMBER",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=5)
                             r5=Label(w,text="ALLERGIES",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=6)
                             r6=Label(w,text="PASSWORD",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15)).grid(row=3,column=7)
                             i=7
                             for info in data:
                                   for j in range(len(info)):
                                     e = Entry(w, width=20, fg='blue',font =("Trebuchet MS",15,"italic")) 
                                     e.grid(row=i, column=j+1)
                                     e.insert(END, info[j])
                                   i+=1
                            
                             lb.destroy()
                             lb1.destroy()
                             lb2.destroy()
                             lb3.destroy()
                             lb4.destroy()
                             lb5.destroy()
                             lb6.destroy()
                             a1.destroy()
                             a2.destroy()
                             a3.destroy()
                             a4.destroy()
                             a5.destroy()
                             a6.destroy()
                         dele=Button(w, text="Done",command =lambda:[done(),dele.place_forget()],height=3, width= 13)
                         dele.place(x=800,y=550)
                         conn.commit()
                    upd=Button(w, text="Update",command = update,height=3, width= 13)
                    upd.place(x=1000, y=400)
                    conn.commit()
                    def delete():
                        w4= tk.Toplevel(a)
                        w4.configure(background="#FFF39A")
                        w4.geometry('500x200')
                        confirmdel=Label(w4,text="Are you sure you want to delete your existing data?",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15))
                        confirmdel.place(x=10,y=10)
                        def yes():
                            
                            cursor.execute("Select phone_no from bloodgroup natural join login where bloodgroup.phone_no=login.phone_no")
                            data=cursor.fetchall()
                            for i in data:

                                query="delete from bloodgroup where Phone_no=%s"
                                cursor.execute(query,i)
                                w4.destroy()
                                w.destroy()

                            conn.commit()
                            messagebox.showinfo(w4,"---YOUR ACCOUNT DETAILS HAVE BEEN DELETED---")
                        yesbutton=Button(w4,text="Yes",command =lambda:yes(),height=3, width= 13)
                        nobutton=Button(w4,text="No",command =lambda:w4.destroy(),height=3, width= 13)
                        yesbutton.place(x=150,y=50)
                        nobutton.place(x=250, y=50)

                    deletebutton=Button(w,text="Delete",command =lambda:delete(),height=3, width= 13)
                    deletebutton.place(x=150, y=400)
                    conn.commit()
                    def delete():
                        w4= tk.Toplevel(a)
                        w4.configure(background="#FFF39A")
                        w4.geometry('500x200')
                        confirmdel=Label(w4,text="Are you sure you want to delete your existing data?",bg='#FFF39A',fg = "Blue",font =("Trebuchet MS",15))
                        confirmdel.place(x=10,y=10)
                        def yes():
                            
                            cursor.execute("Select phone_no from bloodgroup natural join login where bloodgroup.phone_no=login.phone_no")
                            data=cursor.fetchall()
                            for i in data:

                                query="delete from bloodgroup where Phone_no=%s"
                                cursor.execute(query,i)
                                conn.commit()
                            

                            
                            messagebox.showinfo(w4,"---YOUR ACCOUNT DETAILS HAVE BEEN DELETED---")
                            w4.destroy()
                            w.destroy()
                            
                        yesbutton=Button(w4,text="Yes",command =lambda:yes(),height=3, width= 13)
                        nobutton=Button(w4,text="No",command =lambda:w4.destroy(),height=3, width= 13)
                        yesbutton.place(x=150,y=50)
                        nobutton.place(x=250, y=50)

                    deletebutton=Button(w,text="Delete",command =lambda:delete(),height=3, width= 13)
                    deletebutton.place(x=150, y=400)
                    conn.commit()
            
    
                    w.mainloop()
                window4()    
        else:
                messagebox.showinfo(w3,"---YOUR ACCOUNT DOES NOT EXIST---")
                w3.destroy()
                
         
    Button(w3,text="Submit",font=("Trebuchet MS",25,"italic"),command=submit).place(x=400,y=500)
    w3.mainloop()
    

#Buttons in main screen
b1=Button(a, text="View available donors",bd=5, fg='black',font =("Comic Sans MS",30,"bold"),
                              command=lambda:window1())
b1.place(x=50,y=300)
b2=Button(a, text="Sign up as donor", bd=5, fg='black',font=("Comic Sans MS",30,"bold"),
                              command=lambda: window2())
b2.place(x=80,y=430)
b3=Button(a, text="Login", bd=5, fg='black',font=("Comic Sans MS",30,"bold"),
                              command=lambda: window3())
b3.place(x=180,y=550)
a.mainloop()
