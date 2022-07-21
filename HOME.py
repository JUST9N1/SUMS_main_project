

from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("SUMS FOOD")
window.geometry("1350x700+0+0")
window.configure(bg = "#333333")
font1 = ("times new roman", 15, "bold")


my_Image = ImageTk.PhotoImage(Image.open("home.png"))
myLabel = Label(window, image=my_Image)
myLabel.place(x=0, y=0)

F1 = LabelFrame(window, relief=GROOVE, fg="gold", bg="#333333")
F1.place(x=0, y=0, width= 1350)

h1_lbl = Label(F1, text= "SUMS FOOD", font= ("times new roman", 15, "bold"),width=15, fg="#D98141",bg="white",bd = 12 ).grid(row= 0, column= 0, padx=10, pady=10, sticky="w")

login_btn = Button(F1, text="LOGIN", fg="#D98141",bg="white", font= font1, pady=10, padx=10)
login_btn.place(x= 1050, y=0)

signUp_btn = Button(F1, text="SIGNUP",  fg="#D98141",bg= "white", font= font1, pady=10, padx=10)
signUp_btn.place(x=1170, y=0)


h2_lbl = Label(window, text= "What do you feel like today?", font= ("times new roman", 30, "bold"),bg="#333333", fg="#D98141",bd = 12 )
h2_lbl.place(x=25, y= 100)


search_entry = Entry(window,highlightcolor="black",bd=2,  highlightbackground="black", width=40, font= font1, bg="#262626", fg="white")
search_entry.insert(0, "Search here for food or resturants..")
search_entry.place(x = 25, y= 200)

search_btn = Button(window, text="SEARCH",  fg="#D98141",bg= "white", pady=3, padx=3)
search_btn.place(x=435, y= 200)

# F3 = LabelFrame(window).pack()

# my_Image2 = ImageTk.PhotoImage(Image.open("Bottom rect.png"))
# myLabel2 = Label(window, image=my_Image2)
# myLabel2.place(x= 5, y= 350 )

my_pic = Image.open("Bottom rect.png")
resised = my_pic.resize((680, 180), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resised)
myLabel2 = Label(window, image=new_pic)
myLabel2.place(x=5, y= 500)

abtlvl = Label(window, text="""About us:
SUMS FOOD  is the finest company in Nepal that delivers food from 
hundreds of popular restaurants.As a pioneer food delivery
service provider, we are making life easier through 
online ordering. You can stay in home and order food you 
want through ur bed. We know that your time is valuable and
sometimes every minute in the day counts. That’s why we deliver! 
So you can spend more time doing the things you love. 
You can get anything from Indian food to high French cuisine
by placing a simple order online through our website.
Then just sit back, relax, and wait for your order to arrive. 
Sill not connected with us?Log in fom the top left bar if 
you already have an account or create an account with just one click 
and get connected with us.
""", bg= "#262626", fg="white", font=("times new roman", 13, "italic")).place(x=725, y=290)

F4 = LabelFrame(window)

window.mainloop()



