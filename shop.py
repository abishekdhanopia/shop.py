import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import Tk,font
from tkinter import messagebox
import tkinter.messagebox



#press customer button:
def login(shop):
    shop.destroy()
    shop=Tk()
    shop.geometry("1500x700")
    shop.title("customer application form")
    frame=Frame(shop,width=1500,height=800,bg="deeppink")
    frame.pack()

    #Upper Heading:
    f=font.Font(weight="bold",family="Times New Roman Bold Italic",size=28)
    x=Label(frame,text="Customer Details",font=f)
    x.configure(bg="deeppink",fg="navy")
    x.place(relx=.39,rely=.0)


    # Customer Details:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=25)
    a=Label(shop,text="Date:",font=label_font,bg="deeppink")
    a.place(relx=.01,rely=.1)
    b=Label(shop,text="Bill No:",font=label_font,bg="deeppink")
    b.place(relx=.01,rely=.9)
    c=Label(shop,text="Customer Name:",font=label_font,bg="deeppink")
    c.place(relx=.01,rely=.18)
    d=Label(shop,text="Mobile No:",font=label_font,bg="deeppink")
    d.place(relx=.01,rely=.27)
    e=Label(shop,text="Spouse Name:",font=label_font,bg="deeppink")
    e.place(relx=.01,rely=.36)
    f=Label(shop,text="Weight/kg:",font=label_font,bg="deeppink")
    f.place(relx=.01,rely=.45)

    #customer address message box:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=25)
    text1=Label(shop,text="customer address:",font=label_font,bg="deeppink")
    text1.place(relx=.01,rely=.54)
    text2=Text(shop,height=3,width=35)
    text2.place(relx=.25,rely=.55)


    #Items:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=25)
    combo=Label(shop,text="item:",font=label_font,bg="deeppink")
    combo.place(relx=.01,rely=.64)
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=21)
    combo=ttk.Combobox(shop,values=["Gold","Silver","Bronze"],font=label_font)
    combo.place(relx=.25,rely=.65)

    
    
    #item description message box:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=25)
    text3=Label(shop,text="item description:",font=label_font,bg="deeppink")
    text3.place(relx=.01,rely=.73)
    text4=Text(shop,height=3,width=35)
    text4.place(relx=.25,rely=.74)


    #customer details
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=25)
    g=Label(shop,text="Principal Amount:",font=label_font,bg="deeppink")
    g.place(relx=.50,rely=.10)
    h=Label(shop,text="Actual Valuation:",font=label_font,bg="deeppink")
    h.place(relx=.50,rely=.20)
    i=Label(shop,text="Interest Rate:",font=label_font,bg="deeppink")
    i.place(relx=.50,rely=.30)
    j=Label(shop,text="Release Date:",font=label_font,bg="deeppink")
    j.place(relx=.50,rely=.40)
    k=Label(shop,text="No of Days Pledged:",font=label_font,bg="deeppink")
    k.place(relx=.50,rely=.50)
    l=Label(shop,text="Amount Received:",font=label_font,bg="deeppink")
    l.place(relx=.50,rely=.60)

    #customer details Entry Box:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=21)
    a1=Entry(font=label_font,bg="floralwhite")
    a1.place(relx=.25,rely=.1)
    b1=Entry(font=label_font,bg="floralwhite")
    b1.place(relx=.25,rely=.9)
    c1=Entry(font=label_font,bg="floralwhite")
    c1.place(relx=.25,rely=.18)
    d1=Entry(font=label_font,bg="floralwhite")
    d1.place(relx=.25,rely=.27)
    e1=Entry(font=label_font,bg="floralwhite")
    e1.place(relx=.25,rely=.36)
    f1=Entry(font=label_font,bg="floralwhite")
    f1.place(relx=.25,rely=.45)
    g1=Entry(font=label_font,bg="floralwhite")
    g1.place(relx=.75,rely=.10)


    #customer details Entry Box:
    h1=Entry(font=label_font,bg="floralwhite")
    h1.place(relx=.75,rely=.20)
    i1=Entry(font=label_font,bg="floralwhite")
    i1.place(relx=.75,rely=.30)
    j1=Entry(font=label_font,bg="floralwhite")
    j1.place(relx=.75,rely=.40)
    k1=Entry(font=label_font,bg="floralwhite")
    k1.place(relx=.75,rely=.50)
    l1=Entry(font=label_font,bg="floralwhite")
    l1.place(relx=.75,rely=.60)

    def datasave():
        import pymysql as mysql
        Connection=mysql.connect(host="localhost",user="root",password="1234",database="jewel")
        cursor=Connection.cursor()
        s="insert into userdetails(date,name,mobileno,spousename,weight,address,item,itemdesc,billno,principal,actualvalue,intersrate,releasedate,datepled,amtrec) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(a1.get(),b1.get(),c1.get(),d1.get(),e1.get(),text4.get(1.0,END),combo.get(),text2.get(1.0,END),f1.get(),g1.get(),h1.get(),i1.get(),j1.get(),k1.get(),l1.get())
        print(t)
        for x in t:
            print(type(x))
        cursor.execute(s,t)
        Connection.commit()
        print(cursor.rowcount,"new row inserted",cursor.lastrowid)

    # Enter Button:
    label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=29)
    b11=Button(shop,text="enter",fg="black",bg="violet",activebackground="violetred",command=lambda:datasave(),font=label_font)
    b11.place(relx=.70,rely=.70)



         
    

    














#home page:
shop=Tk()
shop.title("home page")
shop.geometry("1500x700")
frame=Frame(shop,width=1500,height=50,bg="magenta")
frame.place(anchor="n",relx=0.5,rely=0)
frame.pack()

#Upper Label:
f=font.Font(weight="bold",family="Times New Roman Bold Italic",size=30)
x=Label(frame,text="Thirupathi Jewellery Finance",font=f)
x.configure(bg="magenta",fg="yellow")
x.place(relx=.30,rely=.1)

#UserName and Password Field;
label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=30)
a=Label(shop,text="Password:",font=label_font,fg="darkviolet")
a.place(relx=.20,rely=.45)
b=Label(shop,text="Username:",font=label_font,fg="darkviolet")
b.place(relx=.20,rely=.30)
a1=Entry(font=label_font,bg="floralwhite")
a1.place(relx=.40,rely=.45)
b1=Entry(font=label_font,bg="floralwhite")
b1.place(relx=.40,rely=.30)

#login Button:
label_font=font.Font(weight="bold",family="Times New Roman Bold Italic",size=30)
b=Button(shop,text="Login",fg="yellow",bg="magenta",activebackground="darkviolet",command=lambda:login(shop),font=label_font)
b.place(relx=.45,rely=.75)

#lower label:
frame=Frame(shop,width=1500,height=50,bg="magenta")
frame.place(relx=.0,rely=.9)
f=font.Font(weight="bold",family="Times New Roman Bold Italic",size=30)
x=Label(frame,text="@copyrights reserved 2024",font=f)
x.configure(bg="magenta",fg="yellow")
x.place(relx=.27,rely=.1)

shop.mainloop()