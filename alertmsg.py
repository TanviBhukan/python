from tkinter import *
import tkinter.messagebox

# Create the main application window
root = Tk()
root.title("When you press a button the message will pop up")
root.geometry('500x300')

# Function to display the message box
def onClick():
    tkinter.messagebox.showinfo("Welcome to Disneyland", "Hi I'm Tanvi")

# Create and place the button
button = Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom', pady=20)  # Added padding for better appearance

# Start the Tkinter event loop
root.mainloop()
 