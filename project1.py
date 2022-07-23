import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

def main():
    nextpage = SignUP()
    print(nextpage)

def register():
    full_nameinfo = fullName.get()
    contactinfo = contact.get()
    emailinfo = Email.get()
    passwordinfo = passcode.get()
    cpasswordinfo = cpasscode.get()

    if full_nameinfo == "":
        messagebox.showerror("Error!!", "FullName must not empty")
    elif contactinfo == "":
        messagebox.showerror("Error!!", "Contact must not empty")
    elif emailinfo == "":
        messagebox.showerror("Error!!", "email must not empty")
    elif passwordinfo != cpasswordinfo:
        messagebox.showinfo("Error!", "Password doesn't match!")
    elif passwordinfo == "":
        messagebox.showerror("Error!!", "password must not empty")
    elif cpasswordinfo == "":
        messagebox.showerror("Error!!", "confirmation field must not empty")
    else:
        file = open(emailinfo, "w")
        file.write(full_nameinfo + "\n")
        file.write(contactinfo + "\n")
        file.write(emailinfo + "\n")
        file.write(passwordinfo + "\n")
        file.write((cpasswordinfo + "\n"))
        file.close()
        messagebox.showinfo("Success", "SignUp success go to login page.")


    # file = open(emailinfo, "w")
    # file.write(full_nameinfo+ "\n")
    # file.write(contactinfo+ "\n")
    # file.write(emailinfo+ "\n")
    # file.write(passwordinfo+ "\n")
    # file.write((cpasswordinfo+ "\n"))
    # file.close()

    fullNameEntry.delete(0, END)
    ContactNumEntr1.delete(0, END)
    emailEntr1.delete(0, END)
    passwordEntr1.delete(0, END)
    confirm_passwordEntr1.delete(0, END)




def loginstat():
    username1 = info.get()
    password = paswrd.get()
    email1Entry.delete(0, END)
    password1Entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password in verify:
           messagebox.showinfo("Login Success")
        else:
            print("something went wrong")# Password_not_recognised()

    else:
           print("user not here") # User_not_found()



def login():
    root.destroy()
    # import main
    global screen
    global info
    global paswrd
    global email1Entry
    global password1Entry


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

    my_button = Button(screen, image=logo_btn, bg="light grey", borderwidth=0)
    my_button.place(x=558, y=0)

    _label = Label(screen,text="------------------------------------------------------------------------------------------------------------------------------------------------------",bg="light grey", fg="White")
    _label.place(x=558, y=75)

    sighntext = Label(screen, text="Welcome To Login Page", fg="#D98141", bg="light grey",font=("Times New Roman", 30, "bold"), pady=15)
    sighntext.place(x=830, y=0)

    info = StringVar()
    email1 = Label(screen, text="Email:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    email1.place(x=600, y=200)

    email1Entry = Entry(screen, width=40,textvariable=info, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
    email1Entry.place(x=750, y=200)

    paswrd = StringVar()
    password1 = Label(screen, text="Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    password1.place(x=600, y=250)

    password1Entry = Entry(screen, width=40,textvariable=paswrd, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141",highlightbackground="#D98141")
    password1Entry.place(x=750, y=250)

    Login_btn = PhotoImage(file="signup_material/Login.png")
    img5_label = Label(image=Login_btn)

    my_button5 = Button(screen, image=Login_btn, bg="light grey", borderwidth=0, command=loginstat)
    my_button5.place(x=600, y=351)

    NoacntLbl = Label(screen, text="Doesn't have an Account? ", width=20, font=("times new roman", 30, "italic"),fg="white", bg="light grey")
    NoacntLbl.place(x=590, y=450)

    signUp_btn = PhotoImage(file="signup_material/signUp.png")
    img2_label = Label(image=signUp_btn)

    my_button2 = Button(screen, image=signUp_btn, bg="light grey", borderwidth=0, command= SignUP)
    my_button2.place(x=600, y=530)

    screen.mainloop()



def SignUP():
    # Signup
    global root
    global fullName
    global contact
    global Email
    global passcode
    global cpasscode
    global fullNameEntry
    global ContactNumEntr1
    global emailEntr1
    global passwordEntr1
    global confirm_passwordEntr1


    root = Tk()
    root.geometry("1650x1000")
    root.title("Sighn up page")
    root.config(bg="light grey")

    my_Image = ImageTk.PhotoImage(Image.open("Rectangle 21.png"))
    myLabel = Label(root, image=my_Image)
    myLabel.place(x=0, y=0)


    logo_btn = PhotoImage(file="signup_material/lOGO.png")
    img_label = Label(image=logo_btn)

    my_button = Button(root, image=logo_btn,bg="light grey", borderwidth=0)
    my_button.pack()

    _label= Label(root, text="-------------------------------------------------------------------------------------------------------------------------------------------------", bg="light grey", fg="White")
    _label.place(x= 600, y= 81)

    fullName = StringVar()
    contact = StringVar()
    Email = StringVar()
    passcode = StringVar()
    cpasscode = StringVar()

    full_name = Label(root, text="Full Name:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    full_name.place(x=600, y=110)

    conntactNum = Label(root, text="Contact Number:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    conntactNum.place(x=600, y=155)

    email = Label(root, text="Email:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    email.place(x=600, y=200)

    password = Label(root, text="Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    password.place(x=600, y=250)

    confirm_password = Label(root, text="Confirm Password:", fg="white", bg="light grey", font=("Times New Roman", 20, "italic"))
    confirm_password.place(x=600, y=300)

    sighntext = Label(root, text="SIGN UP TO SUMS FOOD", fg="#D98141",bg="light grey", font=("Times New Roman", 30, "bold"), pady=15)
    sighntext.place(x=830, y=0)

    # Creating an empty label for input/entry for the labels.
    fullNameEntry = Entry(root, width=40,textvariable=fullName, bd=3, relief=SUNKEN, highlightbackground="#D98141", highlightcolor="#D98141", highlightthickness=2)
    fullNameEntry.place(x=860, y=110)

    ContactNumEntr1 = Entry(root, width=40, bd=3,textvariable=contact, relief=SUNKEN, highlightcolor="#D98141", highlightbackground="#D98141", highlightthickness=2)
    ContactNumEntr1.place(x=860, y=155)

    emailEntr1 = Entry(root, width=40, bd=3,textvariable=Email, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141", highlightbackground="#D98141")
    emailEntr1.place(x=860, y=200)

    passwordEntr1 = Entry(root, width=40,textvariable=passcode, bd=3, relief=SUNKEN, highlightthickness=2, highlightcolor="#D98141", highlightbackground="#D98141")
    passwordEntr1.place(x=860, y=250)

    confirm_passwordEntr1 = Entry(root, width=40, textvariable=cpasscode ,  bd=3, relief=SUNKEN, highlightbackground="#D98141", highlightcolor="#D98141", highlightthickness=2)
    confirm_passwordEntr1.place(x=860, y=300)

    # Now Create buttons to login or for sighnup.
    signUp_btn = PhotoImage(file="signup_material/signUp.png")
    img2_label = Label(image=signUp_btn)

    my_button2 = Button(root, image=signUp_btn,bg="light grey", borderwidth=0, command=register)
    my_button2.place(x= 600, y= 350)

    choice_lbl = Label(root, text="Or SignUp Using: ", bd=3, font=("times new roman", 19, "bold"), fg="white", bg="light grey")
    choice_lbl.place(x= 610, y=420)

    # Button to pass into login page


    facBok_btn = PhotoImage(file="signup_material/facebook.png")
    img3_label = Label(image=facBok_btn)

    my_button3 = Button(root, image=facBok_btn,bg="light grey", borderwidth=0)
    my_button3.bind("<Button-1>", lambda x: webbrowser.open_new("https://www.facebook.com"))
    my_button3.place(x= 600, y= 480)

    # Google button

    Google_btn = PhotoImage(file="signup_material/Google.png")
    img4_label = Label(image=Google_btn)

    my_button4 = Button(root, image=Google_btn,bg="light grey", borderwidth=0)
    my_button4.bind("<Button-1>", lambda x: webbrowser.open_new("https://www.google.com"))
    my_button4.place(x= 850, y= 480)

    acntLbl = Label(root, text="Already have an account?..",  bd=3, font=("times new roman", 19, "bold"), fg="white", bg="light grey")
    acntLbl.place(x = 600, y=580)


    # For loginbtn
    Login_btn = PhotoImage(file="signup_material/Login.png")
    img5_label = Label(image=Login_btn)

    my_button5 = Button(root, image=Login_btn,bg="light grey", borderwidth=0, command=login)
    my_button5.place(x= 600, y= 621)




    root.mainloop()

if __name__ == '__main__':
    main()