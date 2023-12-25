import tkinter as tk
def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

#main gui
root = tk.Tk()
root.title("Simple Calculator")
root.geometry('400x560')

#display input and output
entry = tk.Entry(root, width=25,font=('Arial', 20))
entry.grid(row=0, column=0,columnspan=5)

#buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

#buttons grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=12, height=6,
              command=lambda btn=button: on_click(btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#buttons
tk.Button(root, text='C', width=12, height=6, bg="red", command=clear_entry).grid(row=row_val, column=col_val)
tk.Button(root, text='=', width=12, height=6,bg="green", command=calculate).grid(row=row_val, column=col_val + 1)

root.mainloop()
