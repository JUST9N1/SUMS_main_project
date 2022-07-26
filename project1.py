from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3, os


def backSignup():
    screen.destroy()
    os.system("python signingUp.py")


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




def login():
    def login2():
        
        a = emails.get()
        bb= paswrd.get()
        conn=sqlite3.connect('Customer.db')
        c=conn.cursor()
        c.execute("SELECT * from User")
        records=c.fetchall()
        i=len(records)-1
        conn.commit()
        conn.close()
        while i>=0:
                if records[i][1]!=a or records[i][3]!=bb:
                    i=i-1
                    if i==-1:
                        messagebox.showerror("Login","Invalid Credentials")
                        break
                else:
                    messagebox.showinfo("Login","Logged in Successfully")
                    os.system("python main.py")
                    break 
                               
                    # except:
                    #     messagebox.showerror("Login","Sign Up First")

        
    global screen
    screen = Tk()
    screen.geometry("1650x1000")
    screen.title("Login Page")
    screen.configure(bg="light grey")


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

    emails = StringVar()
    email1 = Label(screen, text="Email:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    email1.place(x=600, y=200)

    email1Entry = Entry(screen, width=40,textvariable=emails, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
    email1Entry.place(x=750, y=200)

    paswrd = StringVar()
    password1 = Label(screen, text="Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    password1.place(x=600, y=250)

    password1Entry = Entry(screen, width=40,textvariable=paswrd, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
    password1Entry.place(x=750, y=250)

    Login_btn = PhotoImage(file="signup_material/Login.png")
    img5_label = Label(image=Login_btn)

    my_button5 = Button(screen, image=Login_btn, bg="light grey", borderwidth=0,command=login2)
    my_button5.place(x=600, y=351)

    NoacntLbl = Label(screen, text="Doesn't have an Account? ", width=20, font=("times new roman", 30, "italic"),fg="white", bg="light grey")
    NoacntLbl.place(x=590, y=450)

    signUp_btn = PhotoImage(file="signup_material/signUp.png")
    img2_label = Label(image=signUp_btn)

    my_button2 = Button(screen, image=signUp_btn, bg="light grey", borderwidth=0, command=backSignup)
    my_button2.place(x=600, y=530)

    screen.mainloop()
    
login()