from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create the main window
root = Tk()
root.title('Clock')

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Create a label to display the time
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')
lbl.pack(anchor='center')

# Start the time function
time()

# Run the main loop
mainloop()
