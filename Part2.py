import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_member_to_db():
    name, age, gender, email, phone = entry_name.get(), entry_age.get(), gender_var.get(), entry_email.get(), entry_phone.get()
    if not all([name, age, gender, email, phone]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    sql = f"INSERT INTO members (name, age, gender, email, phone) VALUES ('{name}', '{age}', '{gender}', '{email}', '{phone}')"
    print("SQL Query:", sql)

    try:
        conn = sqlite3.connect('tennisclub.db')
        conn.execute(sql)
        conn.commit()
        messagebox.showinfo("Success", "Member added successfully!")
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    for entry in [entry_name, entry_age, entry_email, entry_phone]:
        entry.delete(0, tk.END)

window = tk.Tk()
window.title("Tennis Club Member Registration")

labels = ["Name", "Age", "Email", "Phone"]
for i, text in enumerate(labels):
    tk.Label(window, text=f"{text}:").grid(row=i, column=0)
    globals()[f"entry_{text.lower()}"] = tk.Entry(window)
    globals()[f"entry_{text.lower()}"].grid(row=i, column=1)

tk.Label(window, text="Gender:").grid(row=3, column=0)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=3, column=2, sticky="w")

tk.Button(window, text="Add Member", command=add_member_to_db).grid(row=4, column=1, pady=20)

window.mainloop()
