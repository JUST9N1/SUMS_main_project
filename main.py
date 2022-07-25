import sqlite3
from tkinter import *
import random
from tkinter import messagebox
import os



class Bill_App:
        # screen.destroy()
        def __init__(self, root):
            self.root = root
            self.root.geometry("1350x700+0+0")
            self.root.title("SUMS FOOD")
            bg_color = "Black"
            font = ("times new roman", 15, "bold")
            title = Label(self.root, text="Welcome to SUMS food", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                            font=("times new roman", 30, "bold",), pady=2).pack(fill=X)
            # *****************************Variables****************
            # *****************************Items********************
            self.cake = IntVar()
            self.Burger = IntVar()
            self.Sandwich = IntVar()
            self.Pizza = IntVar()
            self.MoMo = IntVar()
            self.DrumStick = IntVar()
            # ******************************Drinks******************
            self.Lassi = IntVar()
            self.Coffee = IntVar()
            self.Lemonade = IntVar()
            self.IceTea = IntVar()
            self.LimeWater = IntVar()
            self.Dietcoke = IntVar()

            # ******************************Specials****************
            self.Largepizza = IntVar()
            self.FrenchFries = IntVar()
            self.Hotchillies = IntVar()
            self.FrozenMo = IntVar()
            self.Hokkah = IntVar()
            self.Lightwine = IntVar()

            # ****************************Total Price and Tax Variable****
            self.Items_Price = StringVar()
            self.Drinks_Price = StringVar()
            self.Specials_Price = StringVar()

            self.Items_Tax = StringVar()
            self.Drinks_Tax = StringVar()
            self.Specials_Tax = StringVar()

            # ****************************Customer*******************
            self.c_name = StringVar()
            self.c_phone = StringVar()


            self.bill_no = StringVar()
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill = StringVar()

            #############################Customer Detail Frame#######

            F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=font, fg="gold",
                            bg=bg_color)
            F1.place(x=0, y=80, relwidth=1)

    
            cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=font).grid(row=0,column=0,padx=20,pady=5)
            cname_txt = Entry(F1, width=15, textvariable=self.c_name, font=("aerial", 15), bd=7,relief=SUNKEN)
            cname_txt.grid(row=0, column=1, pady=5, padx=10)

            cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=font).grid(row=0, column=2,padx=20, pady=5)
            cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font=("aerial", 15), bd=7,relief=SUNKEN)
            # cphn_txt.insert(INSERT, contact.get())
            cphn_txt.grid(row=0, column=3, pady=5, padx=10)

            cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=font).grid(row=0, column=4,padx=20, pady=5)
            cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font=("aerial", 15), bd=7,
                                relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

            bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7,font=("aerial", 12, "bold")).grid(row=0, column=6, padx=10, pady=10)

            F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Items", font=font, fg="gold", bg=bg_color)
            F2.place(x=5, y=180, height=375)

            item1_lbl = Label(F2, text="Cake", font=font, bg=bg_color, fg="lightgreen").grid(row=0, column=0,padx=10, pady=10,sticky="w")
            item1_txt = Entry(F2, width=10, textvariable=self.cake, font=font, bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

            item2_lbl = Label(F2, text="Burger", font=font, bg=bg_color, fg="lightgreen").grid(row=1, column=0,padx=10, pady=10,sticky="w")
            item2_txt = Entry(F2, width=10, textvariable=self.Burger, font=font, bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

            item3_lbl = Label(F2, text="Sandwich", font=font, bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            item3_txt = Entry(F2, width=10, textvariable=self.Sandwich, font=font, bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

            item4_lbl = Label(F2, text="Pizza", font=font, bg=bg_color, fg="lightgreen").grid(row=3, column=0,padx=10, pady=10,sticky="w")
            item4_txt = Entry(F2, width=10, textvariable=self.Pizza, font=font, bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

            item6_lbl = Label(F2, text="Mo:Mo", font=font, bg=bg_color, fg="lightgreen").grid(row=4, column=0,padx=10, pady=10,sticky="w")
            item6_txt = Entry(F2, width=10, textvariable=self.MoMo, font=font, bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

            item7_lbl = Label(F2, text="Drum Stick", font=font, bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            item7_txt = Entry(F2, width=10, textvariable=self.DrumStick, font=font, bd=5, relief=SUNKEN).grid(
                row=5, column=1, padx=10, pady=10)

            # ********************************Drinks*************************
            F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=font, fg="gold", bg=bg_color)
            F3.place(x=275, y=180, height=375)

            drink1_lbl = Label(F3, text="Lassi", font=font, bg=bg_color, fg="lightgreen").grid(row=0, column=0,padx=10, pady=10,sticky="w")
            drink1_txt = Entry(F3, width=10, textvariable=self.Lassi, font=font, bd=5, relief=SUNKEN).grid(
                row=0, column=1, padx=10, pady=10)

            drink2_lbl = Label(F3, text="Coffee", font=font, bg=bg_color, fg="lightgreen").grid(row=1, column=0,padx=10,pady=10,sticky="w")
            drink2_txt = Entry(F3, width=10, textvariable=self.Coffee, font=font, bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

            drink3_lbl = Label(F3, text="Lemonade", font=font, bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            drink3_txt = Entry(F3, width=10, textvariable=self.Lemonade, font=font, bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

            drink4_lbl = Label(F3, text="IceTea", font=font, bg=bg_color, fg="lightgreen").grid(row=3, column=0,padx=10,pady=10,sticky="w")
            drink4_txt = Entry(F3, width=10, textvariable=self.IceTea, font=font, bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

            drink5_lbl = Label(F3, text="Lime water", font=font, bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
            drink5_txt = Entry(F3, width=10, textvariable=self.LimeWater, font=font, bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

            drink6_lbl = Label(F3, text="Diet coke", font=font, bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            drink6_txt = Entry(F3, width=10, textvariable=self.Dietcoke, font=font, bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

            F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Specials", font=font, fg="gold", bg=bg_color)
            F4.place(x=545, y=180, height=375)

            bath_lbl = Label(F4, text="large pizza", font=font, bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.Largepizza, font=font, bd=5, relief=SUNKEN).grid(
                row=0, column=1, padx=10, pady=10)

            bath_lbl = Label(F4, text="french fries", font=font, bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.FrenchFries, font=font, bd=5, relief=SUNKEN).grid(
                row=1, column=1, padx=10, pady=10)

            bath_lbl = Label(F4, text="hot chillies", font=font, bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.Hotchillies, font=font, bd=5, relief=SUNKEN).grid(
                row=2, column=1, padx=10, pady=10)

            bath_lbl = Label(F4, text="frozenMo", font=font, bg=bg_color, fg="lightgreen").grid(row=3, column=0,padx=10,pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.FrozenMo, font=font, bd=5, relief=SUNKEN).grid(
                row=3, column=1, padx=10, pady=10)

            bath_lbl = Label(F4, text="Hokkah", font=font, bg=bg_color, fg="lightgreen").grid(row=4, column=0,padx=10, pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.Hokkah, font=font, bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

            bath_lbl = Label(F4, text="Light wine", font=font, bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
            bath_txt = Entry(F4, width=10, textvariable=self.Lightwine, font=font, bd=5, relief=SUNKEN).grid(
                row=5, column=1, padx=10, pady=10)

            # ********************* Bill Area ********************
            F5 = LabelFrame(self.root, bd=10, bg=bg_color, relief=GROOVE)
            F5.place(x=815, y=180, width=532, height=375)
            bill_title = Label(F5, text="Bill Area", font=("aerial", 16, "bold"), bd=7, relief=GROOVE).pack(
                fill=X)
            scrol_y = Scrollbar(F5, orient=VERTICAL)
            self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT, fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH, expand=1)

            # ****************************Button Frame*******************

            F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=font, fg="gold",
                            bg=bg_color)
            F6.place(x=0, y=560, relwidth=1, height=140)

            m1 = Label(F6, text="Total Items Price", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
            m1_txt = Entry(F6, width=18, textvariable=self.Items_Price, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

            m2 = Label(F6, text="Total Drinks Price", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
            m2_txt = Entry(F6, width=18, textvariable=self.Drinks_Price, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

            m3 = Label(F6, text="Total Specials price", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
            m3_txt = Entry(F6, width=18, textvariable=self.Specials_Price, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

            c1 = Label(F6, text="Items Tax", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
            c1_txt = Entry(F6, width=18, textvariable=self.Items_Tax, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

            c2 = Label(F6, text="Drinks Tax", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
            c2_txt = Entry(F6, width=18, textvariable=self.Drinks_Tax, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

            c3 = Label(F6, text="Specials Tax", bg=bg_color, fg="white",
                        font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
            c3_txt = Entry(F6, width=18, textvariable=self.Specials_Tax, font=("aerial", 10, "bold"), bd=7,
                            relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

            btn_F = Frame(F6, bd=7, relief=GROOVE)
            btn_F.place(x=730, width=585, height=105)

            total_btn = Button(btn_F, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                                font=font, command=self.total).grid(row=0, column=0, padx=5, pady=5)
            GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",
                                bd=2, pady=15, width=10, font=font).grid(row=0, column=1, padx=5, pady=5)
            Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", bd=2,
                                pady=15, width=10, font=font).grid(row=0, column=2, padx=5, pady=5)
            Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", bd=2,
                                pady=15, width=10, font=font).grid(row=0, column=3, padx=5, pady=5)
            self.welcome_bill()

        def total(self):
            # For Items
            self.i_c_p = self.cake.get() * 100
            self.i_B_p = self.Burger.get() * 250
            self.i_S_p = self.Sandwich.get() * 75
            self.i_P_p = self.Pizza.get() * 300
            self.i_M_p = self.MoMo.get() * 110
            self.i_DS_p = self.DrumStick.get() * 290
            self.total_items_price = float(
                (self.i_c_p) +
                (self.i_B_p) +
                (self.i_S_p) +
                (self.i_P_p) +
                (self.i_M_p) +
                (self.i_DS_p)
            )
            self.Items_Price.set("Rs " + str(self.total_items_price))
            self.i_tax = round(self.total_items_price * 0.05, 2)
            self.Items_Tax.set("Rs " + str(self.i_tax))

            # For Drinks
            self.d_Las_p = self.Lassi.get() * 160
            self.d_C_p = self.Coffee.get() * 90
            self.d_L_p = self.Lemonade.get() * 120
            self.d_I_p = self.IceTea.get() * 60
            self.d_LW_p = self.LimeWater.get() * 110
            self.d_DC_p = self.Dietcoke.get() * 60
            self.total_drinks_price = float(
                (self.d_Las_p) +
                (self.d_C_p) +
                (self.d_L_p) +
                (self.d_I_p) +
                (self.d_LW_p) +
                (self.d_DC_p)
            )
            self.Drinks_Price.set("Rs " + str(self.total_drinks_price))
            self.d_tax = round(self.total_drinks_price * 0.05, 2)
            self.Drinks_Tax.set("Rs " + str(self.d_tax))

            # For Specials
            self.s_LP_p = self.Largepizza.get() * 660
            self.s_FF_p = self.FrenchFries.get() * 150
            self.s_Hc_p = self.Hotchillies.get() * 250
            self.s_FM_p = self.FrozenMo.get() * 150
            self.s_H_p = self.Hokkah.get() * 350
            self.s_LW_p = self.Lightwine.get() * 900

            self.total_specials_price = float(
                (self.s_LP_p) +
                (self.s_FF_p) +
                (self.s_Hc_p) +
                (self.s_FM_p) +
                (self.s_H_p) +
                (self.s_LW_p)
            )
            self.Specials_Price.set("Rs " + str(self.total_specials_price))
            self.s_tax = round(self.total_specials_price * 0.05, 2)
            self.Specials_Tax.set("Rs " + str(self.s_tax))

            self.Total_bill = float(
                self.total_items_price +
                self.total_drinks_price +
                self.total_specials_price +
                self.i_tax +
                self.d_tax +
                self.s_tax
            )

        def welcome_bill(self):
            self.txtarea.delete("1.0", END)
            self.txtarea.insert(END, "\t\t\tWelcome to SUMS food\n")
            self.txtarea.insert(END, f"\nBill Number : {self.bill_no.get()}")
            self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
            self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
            self.txtarea.insert(END, f"\n*************************************************************")
            self.txtarea.insert(END, f"\n Products \t\t\t QTY\t\t\tPrice ")
            self.txtarea.insert(END, f"\n*************************************************************")

        def bill_area(self):
            if self.c_name.get() == "" or self.c_phone.get() == "":
                messagebox.showerror("Error", "Customers details mustn't empty!!!")
            elif self.Items_Price.get() == "Rs 0.0" and self.Drinks_Price.get() == "Rs 0.0" and self.Specials_Price.get() == "Rs 0.0":
                messagebox.showerror("Error", "No Product selected!!")
            else:
                self.welcome_bill()
                # ********** Items *********
                if self.cake.get() != 0:
                    self.txtarea.insert(END, f"\n Cake\t\t\t {self.cake.get()}\t\t\t{self.i_c_p}")

                if self.Burger.get() != 0:
                    self.txtarea.insert(END, f"\n Burger\t\t\t {self.Burger.get()}\t\t\t{self.i_B_p}")

                if self.Sandwich.get() != 0:
                    self.txtarea.insert(END, f"\n Sandwich\t\t\t {self.Sandwich.get()}\t\t\t{self.i_S_p}")

                if self.Pizza.get() != 0:
                    self.txtarea.insert(END, f"\n Pizza\t\t\t {self.Pizza.get()}\t\t\t{self.i_P_p}")

                if self.MoMo.get() != 0:
                    self.txtarea.insert(END, f"\n Mo:Mo\t\t\t {self.MoMo.get()}\t\t\t{self.i_M_p}")

                if self.DrumStick.get() != 0:
                    self.txtarea.insert(END, f"\n Drum Stick\t\t\t {self.DrumStick.get()}\t\t\t{self.i_DS_p}")

                # ********** Drinks *********
                if self.Lassi.get() != 0:
                    self.txtarea.insert(END, f"\n Lassi\t\t\t {self.Lassi.get()}\t\t\t{self.d_Las_p}")

                if self.Coffee.get() != 0:
                    self.txtarea.insert(END, f"\n Coffee\t\t\t {self.Coffee.get()}\t\t\t{self.d_C_p}")

                if self.Lemonade.get() != 0:
                    self.txtarea.insert(END, f"\n Lemonade\t\t\t {self.Lemonade.get()}\t\t\t{self.d_L_p}")

                if self.IceTea.get() != 0:
                    self.txtarea.insert(END, f"\n IceTea\t\t\t {self.IceTea.get()}\t\t\t{self.d_I_p}")

                if self.LimeWater.get() != 0:
                    self.txtarea.insert(END, f"\n Lime water\t\t\t {self.LimeWater.get()}\t\t\t{self.d_LW_p}")

                if self.Dietcoke.get() != 0:
                    self.txtarea.insert(END, f"\n Diet Coke\t\t\t {self.DrumStick.get()}\t\t\t{self.d_DC_p}")

                # ********** Specials *********
                if self.Largepizza.get() != 0:
                    self.txtarea.insert(END, f"\n Large pizza\t\t\t {self.Largepizza.get()}\t\t\t{self.s_LP_p}")

                if self.FrenchFries.get() != 0:
                    self.txtarea.insert(END,
                                        f"\n French Fries\t\t\t {self.FrenchFries.get()}\t\t\t{self.s_FF_p}")

                if self.Hotchillies.get() != 0:
                    self.txtarea.insert(END,
                                        f"\n Hot chillies\t\t\t {self.Hotchillies.get()}\t\t\t{self.s_Hc_p}")

                if self.FrozenMo.get() != 0:
                    self.txtarea.insert(END, f"\n FrozenMo\t\t\t {self.FrozenMo.get()}\t\t\t{self.s_FM_p}")

                if self.Hokkah.get() != 0:
                    self.txtarea.insert(END, f"\n Hokkah\t\t\t {self.Hokkah.get()}\t\t\t{self.s_H_p}")

                if self.Lightwine.get() != 0:
                    self.txtarea.insert(END, f"\n Light Wine\t\t\t {self.Lightwine.get()}\t\t\t{self.s_LW_p}")

                self.txtarea.insert(END, f"\n=============================================================")

                if self.Items_Tax.get() != "Rs 0.0":
                    self.txtarea.insert(END, f"\n Items Tax \t\t\t\t{self.Items_Tax.get()}")

                if self.Drinks_Tax.get() != "Rs 0.0":
                    self.txtarea.insert(END, f"\n Drinks Tax \t\t\t\t{self.Drinks_Tax.get()}")

                if self.Specials_Tax.get() != "Rs 0.0":
                    self.txtarea.insert(END, f"\n Specials Tax \t\t\t\t{self.Specials_Tax.get()}")

                self.txtarea.insert(END, f"\n Total Bill :  \t\t\t\t{self.Total_bill}")

                self.txtarea.insert(END, f"\n=============================================================")
                self.save_bill()

        def save_bill(self):
            op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
            if op > 0:
                self.bill_data = self.txtarea.get("1.0", END)
                f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("saved", f"Bill no. : {self.bill_no.get()} saved Successfully")
            else:
                return

        def find_bill(self):
            present = "no"
            for i in os.listdir("bills/"):
                if i.split(".")[0] == self.search_bill.get():
                    f1 = open(f"bills/{i}", "r")
                    self.txtarea.delete("1.0", END)
                    for d in f1:
                        self.txtarea.insert(END, d)
                    f1.close()
                    present = "yes"
            if present == "no":
                messagebox.showerror("Error", "Invalid Bill No.")

        def clear_data(self):
            op = messagebox.askyesno("Clear", "Do you really want to clear data?? ")
            if op > 0:
                # *****************************Items********************
                self.cake.set(0)
                self.Burger.set(0)
                self.Sandwich.set(0)
                self.Pizza.set(0)
                self.MoMo.set(0)
                self.DrumStick.set(0)

                # ******************************Drinks******************
                self.Lassi.set(0)
                self.Coffee.set(0)
                self.Lemonade.set(0)
                self.IceTea.set(0)
                self.LimeWater.set(0)
                self.Dietcoke.set(0)

                # ******************************Specials****************
                self.Largepizza.set(0)
                self.FrenchFries.set(0)
                self.Hotchillies.set(0)
                self.FrozenMo.set(0)
                self.Hokkah.set(0)
                self.Lightwine.set(0)

                # ****************************Total Price and Tax Variable****
                self.Items_Price.set("")
                self.Drinks_Price.set("")
                self.Specials_Price.set("")

                self.Items_Tax.set("")
                self.Drinks_Tax.set("")
                self.Specials_Tax.set("")

                # ****************************Customer*******************
                self.c_name.set("")
                self.c_phone.set("")

                self.bill_no.set("")
                x = random.randint(1000, 9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")
                self.welcome_bill()

        def Exit_app(self):
            op = messagebox.askyesno("Exit", "Are you sure? ")
            if op > 0:
                self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()