
import tkinter as tk
from tkinter import messagebox
import sqlite3


def add_member_to_db():
    
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    email = entry_email.get()
    phone = entry_phone.get()

  
    if not name or not age or not gender or not email or not phone:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

   
    conn = sqlite3.connect('tennisclub.db')
    cursor = conn.cursor()

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            phone TEXT
        )
    ''')

  
    cursor.execute('''
        INSERT INTO members (name, age, gender, email, phone)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, gender, email, phone))

   
    conn.commit()
    conn.close()

 
    messagebox.showinfo("Success", "Member added successfully!")


    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)


window = tk.Tk()
window.title("Tennis Club Member Registration")
tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)


tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=5)


tk.Label(window, text="Gender:").grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("Male") 

tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, padx=10, pady=5, sticky="w")

tk.Label(window, text="Email:").grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(window)
entry_email.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Phone:").grid(row=4, column=0, padx=10, pady=5)
entry_phone = tk.Entry(window)
entry_phone.grid(row=4, column=1, padx=10, pady=5)


submit_button = tk.Button(window, text="Add Member", command=add_member_to_db)
submit_button.grid(row=5, column=1, pady=20)


window.mainloop()
