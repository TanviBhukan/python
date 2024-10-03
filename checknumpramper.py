import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        n = int(entry.get())
        if var.get() == 1:  # Check if Prime
            if is_prime(n):
                messagebox.showinfo("Result", f"{n} is a Prime number.")
            else:
                messagebox.showinfo("Result", f"{n} is not a Prime number.")
        
        elif var.get() == 2:  # Check if Perfect
            if is_perfect(n):
                messagebox.showinfo("Result", f"{n} is a Perfect number.")
            else:
                messagebox.showinfo("Result", f"{n} is not a Perfect number.")
        
        elif var.get() == 3:  # Check if Armstrong
            if is_armstrong(n):
                messagebox.showinfo("Result", f"{n} is an Armstrong number.")
            else:
                messagebox.showinfo("Result", f"{n} is not an Armstrong number.")
        else:
            messagebox.showwarning("Selection Error", "Please select an option.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

# Create the main application window
parent = tk.Tk()
parent.title("Number Checker")

# Entry for the number
entry_label = tk.Label(parent, text="Enter a number:")
entry_label.pack(pady=10)
entry = tk.Entry(parent)
entry.pack(pady=5)

# Variable for radio buttons
var = tk.IntVar()

# Radio buttons for checking types
radio1 = tk.Radiobutton(parent, text="Check for Prime", variable=var, value=1)
radio1.pack(anchor='w', padx=20)

radio2 = tk.Radiobutton(parent, text="Check for Perfect", variable=var, value=2)
radio2.pack(anchor='w', padx=20)

radio3 = tk.Radiobutton(parent, text="Check for Armstrong", variable=var, value=3)
radio3.pack(anchor='w', padx=20)

# Button to perform the check
check_button = tk.Button(parent, text="Check", command=check_number)
check_button.pack(pady=20)

# Start the Tkinter event loop
parent.mainloop()
