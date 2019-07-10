from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import sqlite3


class register():

    def form(self):
        self.lframe.destroy()

        self.regframe = Frame(self.window, height=600, width=800, bg='white')

        self.usernamelabel = Label(self.regframe, text="USERNAME", bg='white', fg='black', font=font).place(x=50, y=20)
        self.s = StringVar()
        self.usernameentry = Entry(self.regframe, font=font, textvariable=self.s, highlightthickness=.6,
                                   highlightbackground="black")
        self.usernameentry.place(x=300, y=20)

        self.accountnolabel = Label(self.regframe, text="ACCOUNTNO", bg='white', fg='black', font=font).place(x=50,
                                                                                                              y=70)
        self.n = StringVar()
        self.accountnoentry = Entry(self.regframe, font=font, textvariable=self.n, highlightthickness=.6,
                                    highlightbackground="black").place(x=300, y=70)

        self.setpasswordlabel = Label(self.regframe, text="PASSWORD", bg='white', fg='black', font=font).place(x=50,
                                                                                                               y=130)
        self.p = StringVar()
        self.setpassswordentry = Entry(self.regframe, font=font, textvariable=self.p, highlightthickness=.6,
                                       highlightbackground="black").place(x=300, y=130)

        self.accounttypelabel = Label(self.regframe, text="ACCOUNT TYPE", bg='white', fg='black', font=font).place(x=50,
                                                                                                                   y=180)
        self.a = StringVar()
        self.accounttypeentry = Entry(self.regframe, font=font, textvariable=self.a, highlightthickness=.6,
                                      highlightbackground="black").place(x=300, y=180)

        self.balancelabel = Label(self.regframe, text="BALANCE", bg='white', fg='black', font=font).place(x=50, y=230)
        self.b = StringVar()
        self.balanceentry = Entry(self.regframe, font=font, textvariable=self.b, highlightthickness=.6,
                                  highlightbackground="black").place(x=300, y=230)

        self.register = Button(self.regframe, text="REGISTER", bg='#50A8B0', fg='black', font=font,
                               command=self.insert).place(x=200, y=290)
        self.quit = Button(self.regframe, text="Quit", bg='#50A8B0', fg='black', font=font, width=10,
                           command=self.window.destroy).place(x=400, y=290)
        self.login = Buttin(self.regframe,text="Login",bg='#50a8B0' ,fg='black',font=font,width=10,command=self.login).place(x = 400,y=290)

        self.regframe.pack()

    def insert(self):
        self.conn = sqlite3.connect("details.db")
        self.x = self.s.get()
        self.y = int(self.n.get())
        self.z = self.p.get()
        self.v = self.a.get()
        self.q = int(self.b.get())
        self.conn.execute(
            "INSERT INTO database VALUES ('{}',{},'{}',{},'{}')".format(self.x, self.q, self.z, self.y, self.v))
        self.conn.commit()
        self.conn.close()


class Lorick(register):
    def __init__(self, window):
        self.window = window
        self.conn = sqlite3.connect("details.db")
        self.lframe = Frame(self.window, bg="white", width=800, height=600)

        self.userlabel = Label(self.lframe, text="Account Number", bg="white", fg="black", font=font)

        self.uentry = Entry(self.lframe, bg="white", font=ufont, highlightbackground="black", highlightthickness=.6)

        self.plabel = Label(self.lframe, text="Password", bg="white", fg="black", font=font)
        self.pentry = Entry(self.lframe, bg="white", font=ufont, highlightbackground="black", highlightthickness=.6)

        self.button = Button(self.lframe, text="LOGIN", bg="#50A8B0", fg="white", font=efont, command=self.verify)

        self.register = Button(self.lframe, text="REGISTER", bg='#50A8B0', fg='white', font=efont, command=self.form)

        self.quit = Button(self.lframe, text="Quit", bg="#50A8B0", fg="white", font=efont, command=self.window.destroy)

        self.userlabel.place(x=100, y=100, width=220, height=20)

        self.uentry.place(x=300, y=100, width=200, height=20)

        self.plabel.place(x=120, y=150, width=220, height=20)

        self.pentry.place(x=300, y=150, width=200, height=20)

        self.button.place(x=225, y=210, width=120, height=40)

        self.quit.place(x=350, y=210, width=120, height=40)

        self.register.place(x=480, y=210, width=120, height=40)
        window.geometry("800x600+240+180")
        self.lframe.pack()

    def fetch(self):
        self.details = []
        self.fe = self.conn.execute("select name,password,accountno,accounttype,balance from database where accountno = ? ",
                                    (self.ac,))
        for i in self.fe:
            self.details.append("Name = {}".format(i[0]))
            self.details.append("Account no = {}".format(i[2]))
            self.details.append("Account type = {}".format(i[3]))
            self.ac = i[2]
            self.details.append("Balance = {}".format(i[4]))

    def verify(self):
        ac = False
        self.temp = self.conn.execute(
            "select name,password,accountno,accounttype,balance from database where accountno = ? ",
            (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "Your are login in as {}".format(i[0])
                self.fetch()
                messagebox._show("Login Info", m)
                self.lframe.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)

        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)

    def MainMenu(self):
        self.frame = Frame(self.window, bg="white", width=800, height=600)
        window.geometry("800x600")
        self.detail = Button(self.frame, text="Account Details", bg="#50A8B0", fg="white", font=font,
                             command=self.account_detail)
        self.enquiry = Button(self.frame, text="Balance Enquiry", bg="#50A8B0", fg="white", font=font,
                              command=self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money", bg="#50A8B0", fg="white", font=font,
                              command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money", bg="#50A8B0", fg="white", font=font,
                                command=self.withdrawl_money)

        self.ministatemt = Button(self.frame,text="Ministatemt",bg="#50A8B0",fg="white",font=font,command=self.mini_statement)
        self.quit = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=font, command=self.window.destroy)
        self.detail.place(x=0, y=0, width=200, height=50)
        self.enquiry.place(x=0, y=100, width=200, height=50)
        self.deposit.place(x=0, y=200, width=200, height=50)
        self.withdrawl.place(x=0, y=300, width=200, height=50)
        self.ministatemt.place(x=0,y=400,width=200,height=50)
        self.quit.place(x=300, y=500, width=120, height=50)
        self.frame.pack()

    def account_detail(self):
        text = self.details[0] + "\n\n\n" + self.details[1] + "\n \n \n" + self.details[2]
        self.fetch()
        self.label = Label(self.frame, text=text, font=font)
        self.label.place(x=300, y=100, width=300, height=200)

    def Balance(self):
        self.fetch()
        self.label = Label(self.frame, text=self.details[3], font=font)
        self.label.place(x=300, y=100, width=300, height=200)

    def deposit_money(self):
    	self.x=StringVar()
    	self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",highlightthickness=2,textvariable=self.x,highlightbackground="white")
    	self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=font)
    	self.money_box.place(x=300, y=100,  width=233, height=20)
    	self.submitButton.place(x=535, y=100, width=65, height=20)
    	self.submitButton.bind("<Button-1>", self.deposit_trans)
    	self.empty = Label(self.frame).place(x=300,y=120,width=300,height=200)


    def deposit_trans(self,flag):
    	self.fetch()

    	text = self.details[3]
    	self.label = Label(self.frame, text=text, font=font)
    	self.label.place(x=300, y=100, width=300, height=100)
    	self.conn.execute("update database set balance = balance + ? where accountno = ?",
                          (self.money_box.get(), self.ac))
    	self.conn.commit()
    	self.fetch()
    	text = "Deposited = " + self.x.get() + "\n\n" +"Total-"+ self.details[3]
    	self.label = Label(self.frame,text=text,font=font).place(x=300,y=160,width=300,height=200)


    def withdrawl_money(self):
        self.m = StringVar()
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white",textvariable=self.m)
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=font)

        self.money_box.place(x=300, y=100, width=233, height=20)
        self.submitButton.place(x=535, y=100, width=65, height=20)
        self.submitButton.bind("<Button-1>", self.withdrawl_trans)
        
        self.empty = Label(self.frame).place(x=300,y=120,width=300,height=200)

    def withdrawl_trans(self, flag):
        self.fetch()
        self.label = Label(self.frame, text=self.details[3], font=font)
        self.label.place(x=300, y=100, width=300, height=100)
        self.conn.execute("update database set balance = balance - ? where accountno = ?",
                          (self.money_box.get(), self.ac))
        self.conn.commit()
        self.fetch()
        text = "Withdrawn = " + self.m.get() + "\n\n" + "Total-"+self.details[3]
        self.label = Label(self.frame,text=text,font=font).place(x=300,y=160,width=300,height=200)


    def mini_statement(self):
    	self.fetch()
    	text = self.details[0] + "\n\n" + self.details[1] + "\n  \n" + self.details[2] + "\n \n" +  self.details[3]
    	self.ministatemt = Label(self.frame,text=text,font=font).place(x=300,y=100,width=300,height=200)





window = Tk()
window.title("                                                                   ATM MANAGEMENT")
font = Font(size=16, family="Times New Roman")
ufont = Font(size=12)
efont = Font(size=12, family="Times New Roman", weight="bold")

topframe = Frame(window, height=40, width=800, highlightbackground="black", highlightthickness=.6, bg="white").pack()
bankname = Label(topframe, text="Sheri Bank", bg="white", font=font).place(x=350, y=4)
window.geometry("800x600+240+180")
obj = Lorick(window)
window.mainloop()

