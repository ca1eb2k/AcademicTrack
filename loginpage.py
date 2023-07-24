import tkinter as tk
from tkinter import *

root=Tk()

# For the username text
username_label=Label( text = "Username", font = 40)
username_label.grid(row=0, column=0) # positions it on the top left (row0, column0)

username_entry=Entry(root)
username_entry.grid(row=0, column=1)

email_label=Label( text = "Email", font = 40)
email_label.grid(row=1, column=0) # positions it on the top left (row0, column0)

email_entry=Entry(root)
email_entry.grid(row=1, column=1)

password_label=Label( text = "Password", font = 40)
password_label.grid(row=2, column=0) # positions it on the top left (row0, column0)

password_entry=Entry(root, show="*")
password_entry.grid(row=2, column=1)

def get_userdata():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print (username, email, password)

B1 = Button(root, text="Sign Up", font=40, command=get_userdata)
B1.grid(row=3, column=1)



root.mainloop()