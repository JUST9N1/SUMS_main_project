
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3, os, random

    
def calllogIn():
    main1.destroy()
    os.system("python loggingin.py")

def AboutUs():
    screen.destroy()
    global main1
    main1 = Tk()
    main1.title("SUMS FOOD")
    main1.geometry("1650x1000")

    my_Image = ImageTk.PhotoImage(Image.open("Frame 2-2 1.png"))
    myLabel = Label(main1, image=my_Image)
    myLabel.place(x=0, y=0)

    bck_btn = Button(main1, text="Back", relief=SOLID, bg= "#F5B85B",width=19,pady=6, fg="white", font=("times new roman", 20, "bold"), borderwidth=0,
                     command=calllogIn)
    bck_btn.place(x= 175, y= 634)

    main1.mainloop()



global screen
global email1Entry
global password1Entry
 
    
# login frame
screen = Tk()
screen.geometry("1650x1000")
screen.title("Login Page")
screen.configure(bg="light grey")

def opensignup():
    screen.destroy()
    os.system("python signingUp.py")

def openstatus():
    screen.destroy()
    os.system("python main.py")

# tkinter does not support placeholders for entry so following two functions removes the default inserted text once the focus is on the entry box
def remove(event): #main page email removed
    a = email1Entry.get()
    if a == "Enter Your Email":
        email1Entry.delete(0, END) #removes text in entry box from 0 to end
    
def remove2(event):
    b = password1Entry.get()
    if b == "Enter Your Password":
        password1Entry.delete(0, END)


   
def show():
    if (showw.get()==1): 
        password1Entry.config(show="")
    else:
        password1Entry.config(show="*")
        



my_pic = Image.open("login_material/login img.png")
resised = my_pic.resize((550, 690), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resised)
myLabel2 = Label(screen, image=new_pic)
myLabel2.place(x=0, y=0)

logo_btn = PhotoImage(file="signup_material/lOGO.png")
img_label = Label(image=logo_btn)

my_button = Button(screen, image=logo_btn, bg="light grey", borderwidth=0, command=AboutUs)
my_button.place(x=558, y=0)

_label = Label(screen,text="------------------------------------------------------------------------------------------------------------------------------------------------------",bg="light grey", fg="White")
_label.place(x=558, y=75)

sighntext = Label(screen, text="Welcome To Login Page", fg="#D98141", bg="light grey",font=("Times New Roman", 30, "bold"), pady=15)
sighntext.place(x=830, y=0)

email1 = Label(screen, text="Email:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
email1.place(x=600, y=200)

email1Entry = Entry(screen, width=40, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
email1Entry.insert(0, "Enter Your Email")
email1Entry.place(x=750, y=200)
email1Entry.bind("<FocusIn>", remove) #bind function is used to know the mouse movement


password1 = Label(screen, text="Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
password1.place(x=600, y=250)

password1Entry = Entry(screen, width=40, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
password1Entry.insert(0, "Enter Your Password")
password1Entry.place(x=750, y=250)
password1Entry.bind("<FocusIn>", remove2)
showw = IntVar(value=1)



NoacntLbl = Label(screen, text="Doesn't have an Account? ", width=20, font=("times new roman", 30, "italic"),fg="white", bg="light grey")
NoacntLbl.place(x=590, y=450)

signUp_btn = PhotoImage(file="signup_material/signUp.png")
img2_label = Label(image=signUp_btn)

my_button2 = Button(screen, image=signUp_btn, bg="light grey", borderwidth=0, command=opensignup)
my_button2.place(x=600, y=530)   

    #verification check
def verify():
    a=email1Entry.get()
    b=password1.get()
    if (a=="" or a=="Enter Your Email") or (b=="" or b=="Enter Your Password"):
        messagebox.showerror("Login","One or More Fields Empty.")
    elif "@" and ".com" not in a:
        messagebox.showerror("Password Reset","Invalid Email")
    elif len(b)<6:
        messagebox.showerror("Password Reset","Password must be more than 6 characters")
    else:
        opensignup()




def reset():
    global mail_ent
    global new_ps_ent
    global new_psc_ent
    global ans1
    global num
    global top
    top = Toplevel()
    top.geometry("380x350")
    top.title("Forgot Password")

    Frame(top,bg='#b4cef3',height=400,width=400).place(x=0,y=0)
    Label(top, text='RESET PASSWORD', bg="#b4cef3", fg='white', font=('Arial',20,'bold')).place(x=50, y=20)

    # remove functionalities for placeholders
    def remove(event):
        a = mail_ent.get()
        if a == "Enter Your Email":
            mail_ent.delete(0, END)

    def remove2(event):
        b = new_ps_ent.get()
        if b == "New Password":
            new_ps_ent.delete(0, END)

            
            
    def remove3(event):
        c = new_psc_ent.get()
        if c == "Confirm New Password":
            new_psc_ent.delete(0, END)


    # show password functionaliteis for passwords
    def show():
        if (showw.get()== 1):
            new_ps_ent.config(show="")
            
        else:
            new_ps_ent.config(show= "*")
            

    def show2():
        if (showww.get() == 1):
            new_psc_ent.config(show= "")
        else:
            new_psc_ent.config(show= "*")
            
    # user inputs

    mail_ent = Entry(top)
    mail_ent.insert(0, "Enter Your Email")
    mail_ent.place(x= 40, y= 75, width= 290, height= 30)
    mail_ent.bind("<FocusIn>", remove)

    # Security questions
    ans1 = StringVar()
    a = "Q1: What is your favourite food? "
    b = "Q2: What is the name of your first pet? "
    c = "Q3: What is the name of your childhood bestfriend?"
    lst= [a, b, c]
    ques = random.choice(lst)
    num = int(ques[1]) - 1
    Label(top, text=ques, bg= "#b4cef3").place(x= 40, y= 118)
    Entry(top, textvariable=ans1).place(x=40, y= 140, width=290, height= 30)


    # new password
    new_ps_ent=Entry(top)
    new_ps_ent.insert(0, 'New Password') #default text inserted in entry box, 0 is positional argument
    new_ps_ent.place(x=40, y=190,width=210, height=30)
    new_ps_ent.bind('<FocusIn>', remove2) #bind function is used to know the mouse movement (if it is clicked or hovering and so on)
    showw=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showw,bg='#b4cef3',command=show).place(x=260,y=193)

    new_psc_ent=Entry(top)
    new_psc_ent.insert(0, 'Confirm New Password') #default text inserted in entry box, 0 is positional argument
    new_psc_ent.place(x=40, y=230,width=210, height=30)
    new_psc_ent.bind('<FocusIn>', remove3) #bind function is used to know the mouse movement (if it is clicked or hovering and so on)
    showww=IntVar(value=1)
    Checkbutton(top,text='Show',offvalue=0,variable=showww,bg='#b4cef3',command=show2).place(x=260,y=233)


    Button(top,text="CONFIRM",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2',command=lambda:verify()).place(x=120, y=280)
    
    
    #update new password
    def update():
        a=mail_ent.get()
        b=ans1.get()
        
        #database connection for password update
        conn=sqlite3.connect('Customer.db')
        c=conn.cursor()
        c.execute("SELECT * from User")
        records=c.fetchall()
        i=len(records)-1
        while i>=0:
            if records[i][1]!=a or records[i][(5+num)]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Password Reset","Invalid Credentials")
                    break
            else:
                ps_upd=new_ps_ent.get()
                psc_upd=new_psc_ent.get()
                c.execute("""UPDATE User SET
                password = :new_ps,
                c_password= :new_psc
                WHERE email = :a""",
                {
                    'new_ps':ps_upd,
                    'new_psc':psc_upd,
                    'a':a
                })
                messagebox.showinfo("Password Reset","Password Changed Successfully")
                #destroy toplevel after successful password update
                top.destroy()
                break             
        conn.commit()
        conn.close()
        
        
        
     #password verification for forgot password functionality
    def verify():
        a=mail_ent.get()
        b=ans1.get()
        c=new_ps_ent.get()
        d=new_psc_ent.get()

        if a=="" or a=="Enter Your Email" or b=="" or c=="" or c=="New Password" or d=="" or d=="Confirm New Password":
            messagebox.showerror("Password Reset","One or More Fields Empty")
        else:
            if "@" and ".com" not in a:
                messagebox.showerror("Password Reset","Invalid Email")
            elif len(c)<6 or len(d)<6:
                messagebox.showerror("Password Reset","Password must be more than 6 characters")
            elif c!=d:
                messagebox.showerror("Password Reset","Passwords Mismatch")
            else:
                update()






Login_btn = PhotoImage(file="signup_material/Login.png")
img5_label = Label(image=Login_btn)

my_button5 = Button(screen, image=Login_btn, bg="light grey", borderwidth=0,command=verify)
my_button5.place(x=600, y=351)


# forgot password and sigup links
Button(screen, text="Forgot Password?", fg="blue", bg= "white", cursor="hand2", command=reset).place(x= 990, y= 305)

# Show password checkbutton
Checkbutton(text="Show", offvalue=0, variable=showw, bg="white", command=show).place(x=1010 , y=250 )



screen.mainloop()
