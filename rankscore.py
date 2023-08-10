# Import necessary libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Function to calculate and display rank score based on input values
def calculate_score():
    try:
        # Convert the input values to floating-point numbers
        achieved = float(achieved_entry.get())
        merit = float(merit_entry.get())
        excellence = float(excellence_entry.get())
    except ValueError:
        # Display an error message if input values are not valid floats
        messagebox.showerror("Error", "Please enter valid numerical values in all boxes!")
        return

    # Calculate the total score before multiplication
    total_before_multiplication = achieved + merit + excellence
    
    # Check if the total before multiplication exceeds 80
    if total_before_multiplication > 80:
        messagebox.showerror("Error", "Total score before multiplication exceeds 80!")
        return
    
    # Calculate the total score based on weights and display the result
    total_score = (achieved * 2) + (merit * 3) + (excellence * 4)
    score_label.config(text="Your Rank Score is: {:.2f}".format(total_score))

# Create the main Tkinter window
root = tk.Tk()
root.title("AcademicTracker - Rank Score Calculator") # Changing the title of the window
root.iconbitmap("assets/at_logo.ico")
root.geometry("1000x600")

# Create a heading label using specified font and grid layout
heading_label = tk.Label(root, text="Rank Score Calculator", font=("Helvetica", 24, "bold"))
heading_label.grid(row=0, column=2, padx=320, columnspan=5)

# Create empty label for spacing
empty_label = tk.Label(root)
empty_label.grid(row=1, column=2)

# Create labels for input boxes
achieved_label = tk.Label(root, text="Achieved", font=("Helvetica", 15,"italic"))
achieved_label.grid(row=2, column=3, padx=20)

merit_label = tk.Label(root, text="Merit", font=("Helvetica", 15,"italic"))
merit_label.grid(row=2, column=4, padx=20)

excellence_label = tk.Label(root, text="Excellence", font=("Helvetica", 15,"italic"))
excellence_label.grid(row=2, column=5, padx=20)

# Create input entry boxes
achieved_entry = tk.Entry(root)
achieved_entry.grid(row=3, column=3)  

merit_entry = tk.Entry(root)
merit_entry.grid(row=3, column=4)  

excellence_entry = tk.Entry(root)
excellence_entry.grid(row=3, column=5)  

# Create empty label for spacing
empty_label = tk.Label(root)
empty_label.grid(row=4, column=4)

# Create a button to calculate rank score
calculate_button = tk.Button(root, text="Calculate", font=40, command=calculate_score)
calculate_button.grid(row=5, column=4)

# Create empty label for spacing
empty_label = tk.Label(root)
empty_label.grid(row=6, column=4)

# Create a label to display the calculated rank score
score_label = tk.Label(root, font=("Helvetica", 15,"italic"))
score_label.grid(row=7, column=4)

# Start the main event loop of the Tkinter application
root.mainloop()
