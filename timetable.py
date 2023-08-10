import tkinter as tk

# this function makes the entry box with custom font specified below so it isn't hard coded
def create_custom_entry(parent, font):
    entry = tk.Entry(parent, font=font, width=6)
    return entry

def load_and_update_data(file_path):
    with open(file_path, "r") as file:
        data_str = file.read()
        data_list = eval(data_str)  # Changing the string back to a list, so it can be used with .insert()

    for row in range(5): 
        for col in range(10):
            entry = entry_boxes[row][col]
            entry.delete(0, tk.END)  # Clear the entry box
            entry.insert(0, data_list[row][col])  # Insert loaded data

# Create the main tkinter window
root = tk.Tk()
root.geometry("1000x600") # Setting the dimensions of the window (1000 pixels wide by 600 pixels tall)

font = ("Helvetica", 21) # Here is the set font name and sizing

entry_boxes = [] # Creates a list to hold the entry boxes
for row in range(5): # Loop through the 5 rows 
    row_entries = []  # Make a list to hold entry boxes for the current row
    for col in range(10): # Loop through each of the 10 columns (colum 0 - column 9)
        entry = create_custom_entry(root, font) # Make the entry box with the custom font specified above
        entry.grid(column=col, row=row) # Put the entry box in the correct grid position (specified using column and row coordinates, could get confusing)
        row_entries.append(entry) # Add the entry box to the current row's list
    entry_boxes.append(row_entries) # Add the row's list to the entry_boxes list

data = [['' for _ in range(10)] for _ in range(5)]  # Create a 2d list to store entered data in, where each row corresponds to a row of entry boxes, and each column corresponds to a column of entry boxes.
# initially all the items in the list are filled with empty string ''
load_and_update_data("output2.txt")

def save_entries(): # This function saves entered data to the data list
    for row in range(5): #Loop through the 5 rows
        for col in range(10): # Loop through the 10 columns
            entry = entry_boxes[row][col] # Get the entry box for the current loop iteration
            entered_text = entry.get() # Get the text entered in the entry box at current loop iteration
            data[row][col] = entered_text  # Store the text in the data list
    print(data)
    with open("output2.txt", "w") as file: # opening text file with "w" to write to the file and delete previously stored info
        file.write(str(data)) # write to the file the timetable info

save_button = tk.Button(root, text="Save Entries", command=save_entries)  # make a button 
save_button.grid(columnspan=10, row=5)  # Put the button below the grid, spanning 10 columns

root.mainloop()  
