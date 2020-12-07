import tkinter as tk

import random
import time
import datetime

root = tk.Tk()
root.geometry("1600x8000")


root.title("Welcome to Keshi's Restuarant")
label1 =tk.Label( text=" Karibu sana!!!!", height = "1", font=("Arial Bold", 20))
label1.place(x=1,y=1)


    #this is the menu and the prices
Label1=tk.Label(text = "You are much welcome to make an order of your choice!!", height = "4", font=("Arial Bold", 20)).pack()
Label2=tk.Label( text = "Choose the items you wish to order from the menu", font=("Arial Bold", 10)).pack()
     
Label3=tk.Label( text = "Chips                        Kshs 70").pack()
     
Label4=tk.Label( text = "Chicken                      Kshs 90").pack()
    
Label5=tk.Label( text = "Rice                         Kshs 40").pack()
     
Label6=tk.Label( text = "Spaghetti                    Kshs 50").pack()
     
Label7=tk.Label(text = "RiceBeef                   Kshs 120").pack()
    
Label8=tk.Label( text = "UgaliBeef                  Kshs 100").pack()
     
Label9=tk.Label( text = "Chapati                      Kshs 10").pack()
    
Label10=tk.Label( text = "Samosa                       Kshs 20").pack()
     
Label11=tk.Label( text = "Tea/Chocolate               Kshs 20").pack()
    
Label12=tk.Label( text = "Coffee                      Kshs 40").pack()

   #ordering part
#the user will have to key in the description of the all items in the description eg chips 2 meaning 2 plates of chips then click the button add items


  
Chips = tk.StringVar()
Chicken =tk. StringVar()
Rice= tk. StringVar()
Spaghetti= tk.StringVar()
RiceBeef = tk.StringVar()
UgaliBeef= tk.StringVar()
Chapati= tk.StringVar()
Samosa= tk.StringVar()
TeaChocolate= tk.StringVar()
Coffee= tk.StringVar()
        


Label13=tk.Label(text = "Key in the items you wish to order", font=("Arial Bold", 15))
     
Label13.place(x=25,y=80)
     
Label14=tk.Label(text = "Chips", height = "10", font=("Arial Bold", 10))
     
Label14.place(x=35,y=100)
e1= tk.Entry( textvariable = Chips)
e1.place(x=50,y=200)
     
     
     
Label15=tk.Label(text = "Chicken", font=("Arial Bold", 10))
     
Label15.place(x=35,y=120)
     
e2= tk.Entry(textvariable = Chicken)
e2.place(x=55,y=150)
     
     
Label16=tk.Label( text = "Rice", font=("Arial Bold", 10))
     
Label16.place(x=35,y=220)
e3= tk.Entry(textvariable = Rice)
e3.place(x=45,y=250)
     
Label17=tk.Label( text = "Spaghetti", font=("Arial Bold", 10))
     
Label17.place(x=35,y=270)
e4= tk.Entry( textvariable = Spaghetti)
     
e4.place(x=45,y=300)
     
     
Label18=tk.Label( text = "RiceBeef", font=("Arial Bold", 10))
     
Label18.place(x=35,y=320)
e5= tk.Entry( textvariable = RiceBeef)
e5.place(x=45,y=350)
     
Label19=tk.Label( text = "UgaliBeef" ,font=("Arial Bold", 10))
     
Label19.place(x=200,y=120)
e6=tk. Entry( textvariable = UgaliBeef)
e6.place(x=200,y=150)
     
Label20=tk.Label(text = "Chapati", font=("Arial Bold", 10))
     
Label20.place(x=200,y=170)
e7= tk.Entry( textvariable = Chapati)
e7.place(x=200,y=200)
     
Label21=tk.Label( text = "Samosa", font=("Arial Bold", 10))
     
Label21.place(x=200,y=220)
e8= tk.Entry( textvariable = Samosa)
e8.place(x=200,y=250)
     
Label22=tk.Label( text = "Tea/Chocolate", font=("Arial Bold", 10))
     
Label22.place(x=200,y=270)
e9= tk.Entry(textvariable = TeaChocolate)
e9.place(x=200,y=300)

Label22=tk.Label( text = "Coffee", font=("Arial Bold", 10))
     
Label22.place(x=200,y=320)
e10= tk.Entry( textvariable = Coffee)
e10.place(x=200,y=350)


listbox = tk.Listbox(root)
listbox.pack()

def reset():
    Chips.set("")
    Chicken.set("")
    Rice.set("")
    Spaghetti.set("")
    RiceBeef.set("")
    UgaliBeef.set("")
    Chapati.set("")
    Samosa.set("")
    TeaChocolate.set("")
    Coffee.set("")
    
def retrievedata():
 global list_data
 list_data = []
 try:
  with open("save.txt", "r", encoding="utf-8") as file:
   for f in file:
    listbox.insert(tk.END, f.strip())
    list_data.append(f.strip())
    print(list_data)
 except:
  pass
# once the user has keyed in the food description, they will click the add button to save data in the list box
def clicked():
    global list_data
    listbox.insert(tk.END, Chips.get())
    list_data.append(Chips.get())
    listbox.insert(tk.END, Chicken.get())
    list_data.append(Chicken.get())
    listbox.insert(tk.END, Rice.get())
    list_data.append(Rice.get())
    listbox.insert(tk.END, Spaghetti.get())
    list_data.append(Spaghetti.get())
    listbox.insert(tk.END, RiceBeef.get())
    list_data.append(RiceBeef.get())
    listbox.insert(tk.END, UgaliBeef.get())
    list_data.append(UgaliBeef.get())
    listbox.insert(tk.END, Chapati.get())
    list_data.append(Chapati.get())
    listbox.insert(tk.END, Samosa.get())
    list_data.append(Samosa.get())
    listbox.insert(tk.END, TeaChocolate.get())
    list_data.append(TeaChocolate.get())
    listbox.insert(tk.END, Coffee.get())
    list_data.append(Coffee.get())
    
    

#the user can delete all the items ordered by clicking delete all
#the user can delete all orders in the listbox and quit the system which means they won't recover the saved data 
    

def delete():
    global list_data
    listbox.delete(0, tk.END)
    list_data = []
#the user can delete some of the items ordered by first selecting the item from the list box then clicking delete selected
def delete_selected():
    global list_data
    selected = listbox.get(listbox.curselection())
    listbox.delete(tk.ANCHOR)
    index = list_data[list_data.index(selected)]
    print(index)
    list_data.pop(list_data.index(selected))
#the user can quit the system and save all the data so that its not lost
def quiting():
 global root
 with open("save.txt", "w", encoding="utf-8") as file:
  for d in list_data:
   file.write(d + "\n")
 root.destroy()

button = tk.Button(root, text="Add food that you wish to order", bg="pink", fg="black", command=clicked)
button.pack()

button_delete = tk.Button(text="Delete the selected food order",bg="pink", fg="black", command=delete_selected)
button_delete.pack()

button_delete_selected = tk.Button(text="Delete All orders made", bg="pink", fg="black", command=delete)
button_delete_selected.pack()

bquit = tk.Button(root, text="Quit and save data", bg="pink", fg="black", command=quiting)
bquit.pack()

button = tk.Button(root, text="Reset", bg="pink", fg="black", command=reset)

button.place(x=200,y=390)


     
  

    
     



retrievedata()
root.mainloop()
