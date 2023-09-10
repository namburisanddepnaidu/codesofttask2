import tkinter as tk
import random
import string

def generate_password():
    password_length = int(entry_length.get())
    password_complexity = complexity_var.get()
    
    if password_complexity == "Simple":
        characters = string.ascii_letters
    elif password_complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif password_complexity == "Complex":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    result.set(generated_password)

root = tk.Tk()
root.title("Password Generator")

entry_length = tk.Entry(root)
entry_length.pack()

complexity_var = tk.StringVar()
complexity_choices = ["Simple", "Medium", "Complex"]
complexity_var.set("Simple")

complexity_menu = tk.OptionMenu(root, complexity_var, *complexity_choices)
complexity_menu.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
