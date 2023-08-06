import os
import subprocess
from tkinter import Tk, Button, PhotoImage, Label, font


def open_program(file_path):
    subprocess.call(['python', file_path])


root = Tk()
root.geometry("1000x600")
root.title("AcademicTracker - Home")

# Add welcome label
welcome_label = Label(root, text="Welcome to AcademicTracker!", font=("Arial", 36))
welcome_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

img1 = PhotoImage(file="timetable.png")
img2 = PhotoImage(file="homework.png")

button2 = Button(root, image=img1, command=lambda: open_program("timetable.py"))
button3 = Button(root, image=img2, command=lambda: open_program("homework.py"))

# Get the width and height of the images
img_width = img1.width()
img_height = img1.height()

button2.grid(row=2, column=2)
button3.grid(row=4, column=2)

root.mainloop()