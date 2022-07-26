
from ssl import VerifyFlags
from tkinter import *
import os
import sqlite3
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image



def openlogin():
    root1.destroy()
    os.system("python loggingIn.py")
    



def AboutUs():
    # root1.destroy()
    global main1
    main1 = Tk()
    main1.title("SUMS FOOD")
    main1.geometry("1650x1000")

    my_Image = ImageTk.PhotoImage(Image.open("Frame 2-2 1.png"))
    myLabel = Label(main1, image=my_Image)
    myLabel.place(x=0, y=0)

    bck_btn = Button(main1, text="Back", relief=SOLID, bg= "#F5B85B",width=19,pady=6, fg="white", font=("times new roman", 20, "bold"), borderwidth=0,
                     command=backSignup)
    bck_btn.place(x= 175, y= 634)

    main1.mainloop()


root1 = Tk()
root1.geometry("1650x1000")
root1.title("Sighn up page")
root1.config(bg="light grey")

def remove(event):
    a=fullNameEntry1.get()
    if a=="Full Name":
        fullNameEntry1.delete(0, END)

def remove2(event):
    a=emailEntr.get()
    if a=="Enter Your Email":
        emailEntr.delete(0, END)

def remove3(event):
    a= ContactNumEntr.get()
    if a=="Enter Your Phone Number":
        ContactNumEntr.delete(0, END)

def remove4(event):
    a=passwordEntr.get()
    if a=="Create Password":
        passwordEntr.delete(0, END)

def remove5(event):
    a=confirm_passwordEntr.get()
    if a=="Confirm Password":
        confirm_passwordEntr.delete(0, END)

    #show password functions for passwords
def show():
    if (showw.get()==1):
        passwordEntr.config(show='')
    else:
        passwordEntr.config(show='*')

def show2():
    if (showww.get()==1):
        confirm_passwordEntr.config(show='')
    else:
        confirm_passwordEntr.config(show='*')




my_Image = ImageTk.PhotoImage(Image.open("Rectangle 21.png"))
myLabel = Label(root1, image=my_Image)
myLabel.place(x=0, y=0)

logo_btn = PhotoImage(file="signup_material/lOGO.png")
img_label = Label(image=logo_btn)

my_button = Button(root1, image=logo_btn, bg="light grey", borderwidth=0, command=AboutUs)
my_button.pack()

_label = Label(root1,
                text="-------------------------------------------------------------------------------------------------------------------------------------------------",
                bg="light grey", fg="White")
_label.place(x=600, y=81)

full_name = Label(root1, text="Full Name:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
full_name.place(x=600, y=110)

conntactNum = Label(root1, text="Contact Number:", fg="white", bg="light grey",
                    font=("Times New Roman", 20, "italic"))
conntactNum.place(x=600, y=155)

email = Label(root1, text="Email:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
email.place(x=600, y=200)

password = Label(root1, text="Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
password.place(x=600, y=250)

confirm_password = Label(root1, text="Confirm Password:", fg="white", bg="light grey",
                            font=("Times New Roman", 20, "italic"))
confirm_password.place(x=600, y=300)

sighntext = Label(root1, text="SIGN UP TO SUMS FOOD", fg="#D98141", bg="light grey",
                    font=("Times New Roman", 30, "bold"), pady=15)
sighntext.place(x=830, y=0)

fullNameEntry1 = Entry(root1, width=40, bd=3, relief=SUNKEN, highlightbackground="#D98141",
                           highlightcolor="#D98141", highlightthickness=2)
fullNameEntry1.insert(0, "Full Name")
fullNameEntry1.place(x=860, y=110)
fullNameEntry1.bind("<FocusIn>", remove) #bind is used to monitor the movement of mouse

ContactNumEntr = Entry(root1, width=40, bd=3, relief=SUNKEN, highlightcolor="#D98141",
                        highlightbackground="#D98141", highlightthickness=2)
ContactNumEntr.insert(0, "Enter Your Phone Number")
ContactNumEntr.place(x=860, y=155)
ContactNumEntr.bind("<FocusIn>", remove3)

emailEntr = Entry(root1, width=40, bd=3, relief=SUNKEN, highlightthickness=2,
                    highlightcolor="#D98141", highlightbackground="#D98141")
emailEntr.insert(0, "Enter Your Email")
emailEntr.place(x=860, y=200)
emailEntr.bind("<FocusIn>", remove2)

passwordEntr = Entry(root1, width=40, bd=3, relief=SUNKEN, highlightthickness=2,
                        highlightcolor="#D98141", highlightbackground="#D98141")
passwordEntr.insert(0, "Create Password")
passwordEntr.place(x=860, y=250)
passwordEntr.bind("<FocusIn>", remove4)

# checkbutton for password entry
showw=IntVar(value=1)
Checkbutton(text='Show',offvalue=0,variable=showw,bg='white',command=show).place(x=1135,y=251) #show password checkbutton


confirm_passwordEntr = Entry(root1, width=40, bd=3, relief=SUNKEN,
                                highlightbackground="#D98141", highlightcolor="#D98141", highlightthickness=2)
confirm_passwordEntr.insert(0, "Confirm Password")
confirm_passwordEntr.place(x=860, y=300)
confirm_passwordEntr.bind("<FocusIn>", remove5)

showww=IntVar(value=1)
Checkbutton(text='Show',offvalue=0,variable=showww,bg='white',command=show2).place(x=1135,y=301)
    
# for signup button
# signUp_btn = PhotoImage(file="signup_material/signUp.png")
# img2_label = Label(image=signUp_btn)
# my_button2 = Button(root1, image=signUp_btn, bg="light grey", borderwidth=0, command='')
# my_button2.place(x=600, y=350) 

choice_lbl = Label(root1, text="Or SignUp Using: ", bd=3, font=("times new roman", 19, "bold"), fg="white",
            bg="light grey")
choice_lbl.place(x=610, y=420)

# Button to pass into login page

facBok_btn = PhotoImage(file="signup_material/facebook.png")
img3_label = Label(image=facBok_btn)

my_button3 = Button(root1, image=facBok_btn, bg="light grey", borderwidth=0)
my_button3.bind("<Button-1>", lambda x: webbrowser.open_new("https://www.facebook.com/SUMS-Foods-106541142143839"))
my_button3.place(x=600, y=480)

# Google button

Google_btn = PhotoImage(file="signup_material/Google.png")
img4_label = Label(image=Google_btn)

my_button4 = Button(root1, image=Google_btn, bg="light grey", borderwidth=0)
my_button4.bind("<Button-1>", lambda x: webbrowser.open_new("https://www.google.com"))
my_button4.place(x=850, y=480)

acntLbl = Label(root1, text="Already have an account?..", bd=3, font=("times new roman", 19, "bold"), fg="white",
        bg="light grey")
acntLbl.place(x=600, y=580)

# For loginbtn
Login_btn = PhotoImage(file="signup_material/Login.png")
img5_label = Label(image=Login_btn)

my_button5 = Button(root1, image=Login_btn, bg="light grey", borderwidth=0,command=openlogin)
my_button5.place(x=600, y=621)



conn = sqlite3.connect('Customer.db')
c = conn.cursor()

try:
    c.execute(""" CREATE TABLE User(
        fullname text,
        email text PRIMARY KEY,
        contact text,
        password text,
        c_password text, 
        q1 text,
        q2 text,
        q3 text
        )""")
except:
    pass



def backSignup():
    main1.destroy()
    os.system("python signingUp.py")

def verify():
    a=fullNameEntry1.get()
    b=emailEntr.get()
    d=ContactNumEntr.get()
    e=passwordEntr.get()
    f=confirm_passwordEntr.get()
            
    if (a=="" or a=="Full Name") or (b=="" or b=="Enter Your Email") or (d=="" or d=="Enter Your Phone Number") or (e=="" or e=="Create Password") or (f=="" or f=="Confirm Password"):
        messagebox.showerror("Signup","One or More Fields Empty.")
    elif "@" and ".com" not in b:
        messagebox.showerror("Signup","Invalid Email")
    elif len(e)<6 or len(f)<6:
        messagebox.showerror("Signup","Password must be more than 6 characters")
    elif len(d)!=10:
        messagebox.showerror("Signup","Invalid Phone Number Length")
    elif e!=f:
        messagebox.showerror("Signup","Passwords Mismatch")
    else:
        try:
            int(d)
            sques()
        except:
                messagebox.showerror("Signup","Invalid Phone Number")
                 
def sques():
        global a
        global b
        global d
        a = StringVar()
        b = StringVar()
        d = StringVar()

        Frame(height=330, width= 350, bg= "white").place(x= 775, y= 210)
        Label(text="Security Questions", font=("Aerial", 16, "bold"), bg="white").place(x=847, y=210)

        Label(text="Q1: What is your favourite food?",bg='white').place(x=805,y=255)
        Entry(root1, textvariable=a).place(x=805, y=280, width=290, height=30)
        
        Label(text="Q2: What is the name of your first pet?",bg='white').place(x=805,y=330)
        Entry(root1, textvariable=b).place(x=805, y=350, width=290, height=30)

        Label(text="Q3: What is the name of your childhood best friend?",bg='white').place(x=805,y=400)
        Entry(root1,textvariable=d).place(x=805, y=420, width=290, height=30)

        Button(root1,text="SIGN UP",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=35,height=2,cursor='hand2',command=verify2).place(x= 805, y= 475)

def verify2():
        aa=a.get()
        bb=b.get()
        cc=d.get()

        if aa=="" or bb=="" or cc=="":
            messagebox.showerror("Security Questions","One or more fields empty")
        else:
            submit()

def submit():
        conn=sqlite3.connect('Customer.db')
        c=conn.cursor()
        c.execute("INSERT INTO User values (:fullNameEntry1, :emailEntr, :ContactNumEntr, :passwordEntr, :confirm_passwordEntr, :q1, :q2, :q3)",
        {
            'fullNameEntry1':fullNameEntry1.get(),
            'emailEntr':emailEntr.get(),
            'ContactNumEntr':ContactNumEntr.get(),
            'passwordEntr':passwordEntr.get(),
            'confirm_passwordEntr':confirm_passwordEntr.get(),
            'q1':a.get(),
            'q2':b.get(),
            'q3':d.get()
            })
        conn.commit()
        conn.close()

        messagebox.showinfo("Signup","User Registered Successfully")
        
        openlogin()
        


signUp_btn = PhotoImage(file="signup_material/signUp.png")
img2_label = Label(image=signUp_btn)
my_button2 = Button(root1, image=signUp_btn, bg="light grey", borderwidth=0, command=verify)
my_button2.place(x=600, y=350) 


root1.mainloop()

