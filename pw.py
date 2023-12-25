import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    use_uppercase = use_uppercase_var.get()
    use_digits = use_digits_var.get()
    use_special = use_special_var.get()

    if length <= 0:
        messagebox.showwarning("Warning", "Password length should be greater than zero.")
        return

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Information", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# main window
root = tk.Tk()
root.title("Password Generator")

# Entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, pady=10)

#this is for Uppercase, Digits, Special Characters 
use_uppercase_var = tk.IntVar()
use_digits_var = tk.IntVar()
use_special_var = tk.IntVar()

use_uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=use_uppercase_var)
use_digits_check = tk.Checkbutton(root, text="Digits", variable=use_digits_var)
use_special_check = tk.Checkbutton(root, text="Special Characters", variable=use_special_var)

use_uppercase_check.grid(row=1, column=0)
use_digits_check.grid(row=1, column=1)
use_special_check.grid(row=1, column=2)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

# Generate Password Entry
password_entry = tk.Entry(root)
password_entry.grid(row=3, column=0, columnspan=2, pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=2, pady=10)

root.mainloop()
