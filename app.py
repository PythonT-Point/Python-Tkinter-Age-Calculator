from tkinter import *
import datetime
import tkinter as tk
from PIL import Image,ImageTk
wd=tk.Tk()
wd.geometry("400x400")
wd.title("Pythontpoint")
nameofperson = tk.Label(text = "Name")
nameofperson.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
nameofpersonEntry = tk.Entry()
nameofpersonEntry.grid(column=1,row=1)
yearentry = tk.Entry()
yearentry.grid(column=1,row=2)
monthentry = tk.Entry()
monthentry.grid(column=1,row=3)
dateentry = tk.Entry()
dateentry.grid(column=1,row=4)
def getinput():
    nameofperson=nameofpersonEntry.get()
    dog = Person(nameofperson,datetime.date(int(yearentry.get()),int(monthentry.get()),int(dateentry.get())))
    
    textArea = tk.Text(master=wd,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Heyya {dog}!!. You are {age} years old!!! ".format(dog=nameofperson, age=dog.age())
    textArea.insert(tk.END,answer)
button=tk.Button(wd,text="Calculate Age Of Person",command=getinput,bg="cyan")
button.grid(column=1,row=5)
class Person:
    def __init__(self,nameofperson,birthdate):
        self.nameofperson = nameofperson
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
image=Image.open('calculator.jpg')
image.thumbnail((200,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
labelimage=tk.Label(image=photo)
labelimage.grid(column=1,row=0)
wd.mainloop()