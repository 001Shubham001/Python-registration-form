from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
  print("Accepted")

# Heading 
Label(root,text="Python Regstration Form",font="ar 15 bold").grid(row=0,column=3)

#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood= Label(root, text="Paymentmood")

#Packing Field
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for storing values
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#Creating Filed
nameEntry = Entry(root, textvariable = namevalue)
phoneEntry = Entry(root, textvariable = phonevalue)
genderEntry = Entry(root, textvariable = gendervalue)
emergencyEntry = Entry(root, textvariable = emergencyvalue)
paymentmoodEntry = Entry(root, textvariable = paymentmoodvalue)

#Packing Fiels
nameEntry.grid(row = 1, column=3)
phoneEntry.grid(row = 2, column=3)
genderEntry.grid(row = 3, column=3)
emergencyEntry.grid(row = 4, column=3)
paymentmoodEntry.grid(row = 5, column=3)

#Creating checkbox
Checkbtn = Checkbutton(text= "remember me?", variable= checkvalue)
Checkbtn.grid(row = 6, column = 3)

#Submit Button
Button(text="Submit",command= getvals).grid(row= 7, column=3)


root.mainloop()