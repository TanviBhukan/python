import tkinter as tk

# Create the main application window
parent = tk.Tk()
parent.title("Shinchan")

# Create a label with Times New Roman font
my_label = tk.Label(parent, text="Hello", font=("Times New Roman", 70, "bold"))

# Use grid layout to place the label
my_label.grid(column=0, row=0)

# Add a label for a Shinchan dialogue in Hindi (typed in English)
shinchan_dialogue = tk.Label(parent, text="Kya kar raha hai? Main to bas ye bolne aaya hoon ki tum bahut acche ho!", 
                              font=("Times New Roman", 20))

# Place the dialogue label below the greeting
shinchan_dialogue.grid(column=0, row=1)

# Start the Tkinter event loop
parent.mainloop()
