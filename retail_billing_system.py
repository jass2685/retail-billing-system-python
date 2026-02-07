from tkinter import*          
from tkinter import messagebox
import random,os,tempfile,smtplib
# functionality part

def clear():
    bathsoapentry.delete(0,END)
    facewashentry.delete(0,END)
    facecreameentry.delete(0,END)
    hairgelentry.delete(0,END)
    hairwashentry.delete(0,END)
    bodylotionentry.delete(0,END)
    
     
    riceentry.delete(0,END)
    oilentry.delete(0,END)
    dalentry.delete(0,END)
    wheatentry.delete(0,END)
    sugarentry.delete(0,END)
    teaentry.delete(0,END)


    maazaentry.delete(0,END)
    dewentry.delete(0,END)
    pepsientry.delete(0,END)
    cocacolaentry.delete(0,END)
    frootientry.delete(0,END)
    thumsupentry.delete(0,END)

    bathsoapentry.insert(0,0)
    facewashentry.insert(0,0)
    facecreameentry.insert(0,0)
    hairgelentry.insert(0,0)
    hairwashentry.insert(0,0)
    bodylotionentry.insert(0,0)
    
     
    riceentry.insert(0,0)
    oilentry.insert(0,0)
    dalentry.insert(0,0)
    wheatentry.insert(0,0)
    sugarentry.insert(0,0)
    teaentry.insert(0,0)

    maazaentry.insert(0,0)
    dewentry.insert(0,0)
    pepsientry.insert(0,0)
    cocacolaentry.insert(0,0)
    frootientry.insert(0,0)
    thumsupentry.insert(0,0)

    cosmeticpriceentry.delete(0,END)
    grocerypriceentry.delete(0,END)
    colddrinkpriceentry.delete(0,END)  

    cosmetictaxentry.delete(0,END)
    grocerytaxentry.delete(0,END)
    colddrinktaxentry.delete(0,END)  

    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    billingnumberentry.delete(0,END)

    textarea.delete(1.0,END)


def send_email():
    def send_gmail():
        try:
         ob = smtplib.SMTP('smtp.gmail.com', 587)
         ob.starttls()
         ob.login(senderentry.get(), passwordentry.get())
         message = email_textarea.get(1.0, END)
         ob.sendmail(senderentry.get(), receiverentry.get(), message)
         ob.quit()
         messagebox.showinfo('Success', 'Bill is successfully sent!')
         root1.destroy()
        except :
         messagebox.showerror('Error','Something went wrong,please try again')
    if textarea.get(1.0, END) == '\n':
      messagebox.showerror('Error', 'Bill is empty')  
    else:

     root1 = Toplevel()
     root1.grab_set()
     root1.title('Send Email')
     root1.config(bg='grey2')
     root1.resizable(0, 0)

    # Sender Frame
    senderframe = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    senderframe.grid(row=0, column=0, padx=40, pady=20)

    
    senderlabel = Label(senderframe, text="Sender's Email", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    senderlabel.grid(row=0, column=0, padx=10, pady=8)
    senderentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    senderentry.grid(row=0, column=1, padx=10, pady=8)

    passwordlabel = Label(senderframe, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    passwordlabel.grid(row=1, column=0, padx=10, pady=8)
    passwordentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
    passwordentry.grid(row=1, column=1, padx=10, pady=8)

    # Recipient Frame
    recipientframe = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    recipientframe.grid(row=1, column=0, padx=40, pady=20)

    receiverlabel = Label(recipientframe, text="Receiver's Email", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    receiverlabel.grid(row=0, column=0, padx=10, pady=8)
    receiverentry = Entry(recipientframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    receiverentry.grid(row=0, column=1, padx=10, pady=8)

    messagelabel = Label(recipientframe, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    messagelabel.grid(row=1, column=0, padx=10, pady=8)

    email_textarea = Text(recipientframe, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=40, height=7)
    email_textarea.grid(row=2, column=0, columnspan=2, padx=10, pady=8)
    email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t'))

    sendbutton = Button(root1, text="Send Email", font=('arial', 16, 'bold'),bg='green', fg='white', width=16, command=send_email)
    sendbutton.grid(row=2, column=0, pady=10)


def open_email_window():
    global senderentry, passwordentry, receiverentry, email_textarea
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
        return

    root1 = Toplevel()
    root1.title('Send Email')
    root1.config(bg='grey2')
    root1.resizable(0, 0)

    

    # Sender Frame
    senderframe = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    senderframe.grid(row=0, column=0, padx=40, pady=20)

    senderlabel = Label(senderframe, text="Sender's Email", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    senderlabel.grid(row=0, column=0, padx=10, pady=8)
    senderentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    senderentry.grid(row=0, column=1, padx=10, pady=8)

    passwordlabel = Label(senderframe, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    passwordlabel.grid(row=1, column=0, padx=10, pady=8)
    passwordentry = Entry(senderframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
    passwordentry.grid(row=1, column=1, padx=10, pady=8)

    # Recipient Frame
    recipientframe = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    recipientframe.grid(row=1, column=0, padx=40, pady=20)

    receiverlabel = Label(recipientframe, text="Receiver's Email", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    receiverlabel.grid(row=0, column=0, padx=10, pady=8)
    receiverentry = Entry(recipientframe, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    receiverentry.grid(row=0, column=1, padx=10, pady=8)

    messagelabel = Label(recipientframe, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
    messagelabel.grid(row=1, column=0, padx=10, pady=8)

    email_textarea = Text(recipientframe, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=40, height=10)
    email_textarea.grid(row=2, column=0, columnspan=2, padx=10, pady=8)
    email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t'))

    sendbutton = Button(root1, text="Send Email", font=('arial', 16, 'bold'),bg='green', fg='white', width=16, command=open_email_window)
    sendbutton.grid(row=2, column=0, pady=10)

def print_bill():
    if textarea.get(1.0,END)=='/n':
       messagebox.showerror('error','bill is empty')
    else: 
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
        

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billingnumberentry.get():
            f=open('bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('error','invalid bill number')    
    


if not os.path.exists('bills'):
     os.mkdir('bills')


def save_bill():
 global billnumber
 result=messagebox.askyesno('confirm','Do you want to save the bill?')
 if result:
      bill_content= textarea.get(1.0,END)
      file=open(f'bills/{billnumber}.txt','w') 
      file.write(bill_content)
      file.close()
      messagebox.showinfo('success',f'bill number{billnumber}is saved successfully')
      billnumber=random.randint(50,1000)


billnumber=random.randint(50,1000)

def total():
    global bathsoapprice,hairwashprice,facewashprice,facecreameprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,dalprice,wheatprice,sugarprice,teaprice
    global maazaprice,dewprice,pepsiprice,cocacolaprice,frootiprice,thumsupprice
    global totalbill
    # cosmetic price calculation
    bathsoapprice=int(bathsoapentry.get())*20
    facewashprice=int(facewashentry.get())*50
    facecreameprice=int(facecreameentry.get())*80
    hairwashprice=int(hairwashentry.get())*150
    hairgelprice=int(hairgelentry.get())*250
    bodylotionprice=int(bodylotionentry.get())*500

    totalcosmeticprice=bathsoapprice+facewashprice+facecreameprice+hairwashprice+hairgelprice+bodylotionprice
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,str(totalcosmeticprice)+'Rs')
    cosmetictax=totalcosmeticprice*0.20
    cosmetictaxentry.delete(0,END)
    cosmetictaxentry.insert(0,str(cosmetictax)+'Rs')

    # grocery price calculation
    riceprice=int(riceentry.get())*250
    oilprice=int(oilentry.get())*500
    dalprice=int(dalentry.get())*300
    wheatprice=int(wheatentry.get())*600
    sugarprice=int(sugarentry.get())*400
    teaprice=int(teaentry.get())*300
    
    totalgroceryprice=riceprice+oilprice+dalprice+wheatprice+sugarprice+teaprice
    grocerypriceentry.delete(0,END)
    grocerypriceentry.insert(0,str(totalgroceryprice)+'Rs')
    grocerytax=totalgroceryprice*0.52
    grocerytaxentry.delete(0,END)
    grocerytaxentry.insert(0,str(grocerytax)+'Rs')

 # colddrinks price calculation
    maazaprice=int(maazaentry.get())*70
    dewprice=int(dewentry.get())*80
    pepsiprice=int(pepsientry.get())*80
    cocacolaprice=int(cocacolaentry.get())*90
    frootiprice=int(frootientry.get())*60
    thumsupprice=int(thumsupentry.get())*80

    totalcolddrinksprice=maazaprice+dewprice+pepsiprice+cocacolaprice+frootiprice +thumsupprice
    colddrinkpriceentry.delete(0,END)
    colddrinkpriceentry.insert(0,str(totalcolddrinksprice)+'Rs')
    colddrinktax=totalcolddrinksprice*0.12
    colddrinktaxentry.delete(0,END)
    colddrinktaxentry.insert(0,str(colddrinktax)+'Rs')

    totalbill=totalcosmeticprice+totalcolddrinksprice+totalgroceryprice+cosmetictax+colddrinktax+grocerytax


def bill_area():
    total()
    if nameentry.get()==''or phoneentry.get()=='':
     messagebox.showerror('Error','Customer Detail Are Required')
     return
    elif cosmeticpriceentry.get()=='' and grocerypriceentry.get()=='' and colddrinkpriceentry.get()=='':
       messagebox.showerror('Error','No Product Are Selected')
       return
    elif cosmeticpriceentry.get()=='0 Rs' and grocerypriceentry.get()=='0 Rs' and colddrinkpriceentry.get()=='0 Rs':
       messagebox.showerror('Error','No Product Are Selected')
       return
    else:
     textarea.delete(1.0,END)
     textarea.insert(END,'\t\t\t**WELCOME CUSTOMER**\n')
     textarea.insert(END,f'\nBill Number: {billnumber}\n')
     textarea.insert(END,f'\nCustomer Name: {nameentry.get()}\n')
     textarea.insert(END,f'\nCustomer Phone Number: {phoneentry.get()}\n')               
     textarea.insert(END,'\n============================================================')
     textarea.insert(END,'Product\t\t\t Quantity\t\t\tPrice')
     textarea.insert(END,'\n============================================================')
     if bathsoapentry.get()!='0':
          textarea.insert(END,f'Bath Soap\t\t\t{bathsoapentry.get()}\t\t\t{bathsoapprice}Rs\n')
     if hairwashentry.get()!='0':
          textarea.insert(END,f'hair wash\t\t\t{hairwashentry.get()}\t\t\t{hairwashprice}Rs\n')
     if facewashentry.get()!='0':
          textarea.insert(END,f'face wash\t\t\t{facewashentry.get()}\t\t\t{facewashprice}Rs\n')
     if facecreameentry.get()!='0':
          textarea.insert(END,f'face creame\t\t\t{facecreameentry.get()}\t\t\t{facecreameprice}Rs\n')
     if hairgelentry.get()!='0':
          textarea.insert(END,f'hair gel\t\t\t{hairgelentry.get()}\t\t\t{hairgelprice}Rs\n')
     if bodylotionentry.get()!='0':
          textarea.insert(END,f'body lotion\t\t\t{bodylotionentry.get()}\t\t\t{bodylotionprice}Rs\n')
     if riceentry.get()!='0':
          textarea.insert(END,f'\nrice\t\t\t{riceentry.get()}\t\t\t{riceprice}Rs')   
     if oilentry.get()!='0':
          textarea.insert(END,f'\noil\t\t\t{oilentry.get()}\t\t\t{oilprice}Rs')   
     if dalentry.get()!='0':
          textarea.insert(END,f'\ndal\t\t\t{dalentry.get()}\t\t\t{dalprice}Rs')   
     if wheatentry.get()!='0':
          textarea.insert(END,f'\nwheat\t\t\t{wheatentry.get()}\t\t\t{wheatprice}Rs')   
     if sugarentry.get()!='0':
          textarea.insert(END,f'\nsugar\t\t\t{sugarentry.get()}\t\t\t{sugarprice}Rs')   
     if teaentry.get()!='0':
          textarea.insert(END,f'\ntea\t\t\t{teaentry.get()}\t\t\t{teaprice}Rs')   
     if maazaentry.get()!='0':
          textarea.insert(END,f'\nmaaza\t\t\t{maazaentry.get()}\t\t\t{maazaprice}Rs')   
     if dewentry.get()!='0':
          textarea.insert(END,f'\ndew\t\t\t{dewentry.get()}\t\t\t{dewprice}Rs')   
     if pepsientry.get()!='0':
          textarea.insert(END,f'\npepsi\t\t\t{pepsientry.get()}\t\t\t{pepsiprice}Rs')   
     if cocacolaentry.get()!='0':
          textarea.insert(END,f'\ncocacola\t\t\t{cocacolaentry.get()}\t\t\t{cocacolaprice}Rs')   
     if frootientry.get()!='0':
          textarea.insert(END,f'\nfrooti\t\t\t{frootientry.get()}\t\t\t{frootiprice}Rs')   
     if thumsupentry.get()!='0':
          textarea.insert(END,f'\nthumsup\t\t\t{thumsupentry.get()}\t\t\t{thumsupprice}Rs')
     textarea.insert(END,'\n------------------------------------------------------------')
     
     if cosmetictaxentry.get()!='0.0Rs':
          textarea.insert(END,f'\nCosmetic Tax\t\t{cosmetictaxentry.get()}')
     if grocerytaxentry.get()!='0.0Rs':
          textarea.insert(END,f'\nGrocery Tax\t\t{grocerytaxentry.get()}')
     if colddrinktaxentry.get()!='0.0Rs':
          textarea.insert(END,f'\nColddrink Tax\t\t{colddrinktaxentry.get()}')
     textarea.insert(END,f'\nTotal Bill \t\t\t\t{totalbill}')
     textarea.insert(END,'\n------------------------------------------------------------')
     save_bill()

root=Tk()
root.title("RETAIL BILLING SYSTEM")
root.geometry("1700x900")
# root.iconbitmap("icon.ico")
headinglabel=Label(root,text='RETAIL BILLING SYSTEM',font=('times new roman',50,'bold'),bg='grey2',fg='white',bd=12,relief=RIDGE)
headinglabel.pack(fill=X,pady=8)
   
customer_detail_frame=LabelFrame(root,text='customer details',font=('calibri',16,'bold'),fg='blue',bd=8,bg='grey2',relief=RIDGE)
customer_detail_frame.pack(fill=X)

namelabel=Label(customer_detail_frame,text='Name',font=('calibri',16,'bold'),bg='grey2',fg='white')
namelabel.grid(row=0,column=0,padx=20)

nameentry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=19)
nameentry.grid(row=0,column=1,padx=8)

phonelabel=Label(customer_detail_frame,text='Phone Number',font=('calibri',16,'bold'),bg='grey2',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phoneentry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=19)
phoneentry.grid(row=0,column=3,padx=8)

billingnumberlabel=Label(customer_detail_frame,text='Billing Number',font=('calibri',16,'bold'),bg='grey2',fg='white')
billingnumberlabel.grid(row=0,column=4,padx=20,pady=2)

billingnumberentry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=19)
billingnumberentry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_detail_frame,text='SEARCH',font=('calibri',12,'bold'),bd=7,width=10,command=open_email_window)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsframe=Frame(root)
productsframe.pack(pady=10)

cosmeticsframe=LabelFrame(productsframe,text='cosmetic ',font=('calibri',16,'bold'),fg='blue',bd=8,bg='grey2',relief=RIDGE)
cosmeticsframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticsframe,text='Body Soap',font=('calibri',16,'bold'),bg='grey2',fg='white')
bathsoaplabel.grid(row=0,column=0,padx=9,pady=10,sticky='w')
bathsoapentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
bathsoapentry.grid(row=0,column=1,pady=7)
bathsoapentry.insert(0,0)

facewashlabel=Label(cosmeticsframe,text='Face Wash',font=('calibri',16,'bold'),bg='grey2',fg='white')
facewashlabel.grid(row=1,column=0,padx=9,pady=10,sticky='w')
facewashentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
facewashentry.grid(row=1,column=1,padx=10,pady=7)
facewashentry.insert(0,0)

facecreamelabel=Label(cosmeticsframe,text='Face Creame',font=('calibri',16,'bold'),bg='grey2',fg='white')
facecreamelabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
facecreameentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
facecreameentry.grid(row=2,column=1,padx=10,pady=7)
facecreameentry.insert(0,0)

hairwashlabel=Label(cosmeticsframe,text='Hair Wash',font=('calibri',16,'bold'),bg='grey2',fg='white')
hairwashlabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
hairwashentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
hairwashentry.grid(row=3,column=1,padx=10,pady=7)
hairwashentry.insert(0,0)


hairgellabel=Label(cosmeticsframe,text='Hair Gel',font=('calibri',16,'bold'),bg='grey2',fg='white')
hairgellabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
hairgelentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
hairgelentry.grid(row=4,column=1,padx=10,pady=7)
hairgelentry.insert(0,0)


bodylotionlabel=Label(cosmeticsframe,text='Body Lotion',font=('calibri',16,'bold'),bg='grey2',fg='white')
bodylotionlabel.grid(row=5,column=0,padx=10,pady=9,sticky='w')
bodylotionentry=Entry(cosmeticsframe,font=('calibri',16,'bold'),width=9,bd=5)
bodylotionentry.grid(row=5,column=1,padx=10,pady=7)
bodylotionentry.insert(0,0)


groceryframe=LabelFrame(productsframe,text='Grocery',font=('calibri',16,'bold'),fg='blue',bd=8,bg='grey2',relief=RIDGE)
groceryframe.grid(row=0,column=1)

ricelabel=Label(groceryframe,text='Rice',font=('calibri',16,'bold'),bg='grey2',fg='white')
ricelabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
riceentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
riceentry.grid(row=0,column=1,padx=10,pady=7)
riceentry.insert(0,0)

oillabel=Label(groceryframe,text='Oil',font=('calibri',16,'bold'),bg='grey2',fg='white')
oillabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
oilentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
oilentry.grid(row=1,column=1,padx=10,pady=7)
oilentry.insert(0,0)


dallabel=Label(groceryframe,text='Dal',font=('calibri',16,'bold'),bg='grey2',fg='white')
dallabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
dalentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
dalentry.grid(row=2,column=1,padx=10,pady=7)
dalentry.insert(0,0)


wheatlabel=Label(groceryframe,text='Wheat',font=('calibri',16,'bold'),bg='grey2',fg='white')
wheatlabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
wheatentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
wheatentry.grid(row=3,column=1,padx=10,pady=7)
wheatentry.insert(0,0)


sugarlabel=Label(groceryframe,text='Sugar',font=('calibri',16,'bold'),bg='grey2',fg='white')
sugarlabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
sugarentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
sugarentry.grid(row=4,column=1,padx=10,pady=7)
sugarentry.insert(0,0)


tealabel=Label(groceryframe,text='Tea',font=('calibri',16,'bold'),bg='grey2',fg='white')
tealabel.grid(row=5,column=0,padx=10,pady=9,sticky='w')
teaentry=Entry(groceryframe,font=('calibri',16,'bold'),width=9,bd=5)
teaentry.grid(row=5,column=1,padx=10,pady=7)
teaentry.insert(0,0)


colddrinksframe=LabelFrame(productsframe,text='Cold Drinks',font=('calibri',16,'bold'),fg='blue',bd=8,bg='grey2',relief=RIDGE)
colddrinksframe.grid(row=0,column=2)

maazalabel=Label(colddrinksframe,text='Maaza',font=('calibri',16,'bold'),bg='grey2',fg='white')
maazalabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
maazaentry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
maazaentry.grid(row=0,column=1,padx=10,pady=7)
maazaentry.insert(0,0)

dewlabel=Label(colddrinksframe,text='Dew',font=('calibri',16,'bold'),bg='grey2',fg='white')
dewlabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
dewentry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
dewentry.grid(row=1,column=1,padx=10,pady=7)
dewentry.insert(0,0)

pepsilabel=Label(colddrinksframe,text='Pepsi',font=('calibri',16,'bold'),bg='grey2',fg='white')
pepsilabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
pepsientry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
pepsientry.grid(row=2,column=1,padx=10,pady=7)
pepsientry.insert(0,0)

cocacolalabel=Label(colddrinksframe,text='Coca Cola',font=('calibri',16,'bold'),bg='grey2',fg='white')
cocacolalabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
cocacolaentry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
cocacolaentry.grid(row=3,column=1,padx=10,pady=7)
cocacolaentry.insert(0,0)

frootilabel=Label(colddrinksframe,text='Frooti',font=('calibri',16,'bold'),bg='grey2',fg='white')
frootilabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
frootientry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
frootientry.grid(row=4,column=1,padx=10,pady=7)
frootientry.insert(0,0)

thumsuplabel=Label(colddrinksframe,text='Thums Up',font=('calibri',16,'bold'),bg='grey2',fg='white')
thumsuplabel.grid(row=5,column=0,padx=10,pady=9,sticky='w')
thumsupentry=Entry(colddrinksframe,font=('calibri',16,'bold'),width=9,bd=5)
thumsupentry.grid(row=5,column=1,padx=10,pady=7)
thumsupentry.insert(0,0)

billframe=Frame(productsframe,bd=8,relief=RIDGE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text='Bill Area',font=('calibri',16,'bold'),bd=7,relief=RIDGE)
billarealabel.pack()

Scrollbar=Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=19,width=60,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)

billmenuframe=LabelFrame(root,text='Bill Menu',font=('calibri',16,'bold'),fg='blue',bd=8,bg='grey2',relief=RIDGE)
billmenuframe.pack()

cosmeticpricelabel=Label(billmenuframe,text='Cosmetic Price',font=('calibri',16,'bold'),bg='grey2',fg='white')
cosmeticpricelabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
cosmeticpriceentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
cosmeticpriceentry.grid(row=0,column=1,padx=10,pady=2)

grocerypricelabel=Label(billmenuframe,text='Grocery Price',font=('calibri',16,'bold'),bg='grey2',fg='white')
grocerypricelabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
grocerypriceentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
grocerypriceentry.grid(row=1,column=1,padx=10,pady=2)

colddrinkpricelabel=Label(billmenuframe,text='Cold Drink Price',font=('calibri',16,'bold'),bg='grey2',fg='white')
colddrinkpricelabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
colddrinkpriceentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
colddrinkpriceentry.grid(row=2,column=1,padx=10,pady=2)

cosmetictaxlabel=Label(billmenuframe,text='Cosmetic Tax',font=('calibri',16,'bold'),bg='grey2',fg='white')
cosmetictaxlabel.grid(row=0,column=2,padx=10,pady=9,sticky='w')
cosmetictaxentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
cosmetictaxentry.grid(row=0,column=3,padx=10,pady=2)

grocerytaxlabel=Label(billmenuframe,text='Grocery Tax',font=('calibri',16,'bold'),bg='grey2',fg='white')
grocerytaxlabel.grid(row=1,column=2,padx=10,pady=9,sticky='w')
grocerytaxentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
grocerytaxentry.grid(row=1,column=3,padx=10,pady=2)

colddrinktaxlabel=Label(billmenuframe,text='Cold Drink Tax',font=('calibri',16,'bold'),bg='grey2',fg='white')
colddrinktaxlabel.grid(row=2,column=2,padx=10,pady=9,sticky='w')
colddrinktaxentry=Entry(billmenuframe,font=('calibri',16,'bold'),width=9,bd=5)
colddrinktaxentry.grid(row=2,column=3,padx=10,pady=2)

buttonframe=Frame(billmenuframe,bd=8,relief=RIDGE)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,text='Total',font=('calibri',16,'bold'),bg='grey2',fg='white',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=9)

billbutton=Button(buttonframe,text='Bill',font=('calibri',16,'bold'),bg='grey2',fg='white',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=9)

emailbutton=Button(buttonframe,text='Email',font=('calibri',16,'bold'),bg='grey2',fg='white',bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=9)

printbutton=Button(buttonframe,text='Print',font=('calibri',16,'bold'),bg='grey2',fg='white',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=9)

clearbutton=Button(buttonframe,text='Clear',font=('calibri',16,'bold'),bg='grey2',fg='white',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=9)


root.mainloop()                     
