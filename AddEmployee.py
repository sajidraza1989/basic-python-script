import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def add_employee():
    def submit_data():
        name = name_entry.get()
        age = age_entry.get()
        salary = salary_entry.get()
        manager = manager_entry.get()
        married = married_var.get()

        if not name or not age or not salary or not manager:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            # Save data to the database
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="python_db"
            )
            cursor = connection.cursor()
            query = "INSERT INTO employees (name, age, salary, manager, married) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, age, salary, manager, married))
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Employee added successfully!")
            add_window.destroy()
            fetch_data()  # Refresh parent window data
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # Create a new window for adding employee
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")
    add_window.geometry("400x300")

    # Name
    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_entry = tk.Entry(add_window, width=30)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Age
    tk.Label(add_window, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    age_entry = tk.Entry(add_window, width=30)
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    # Salary
    tk.Label(add_window, text="Salary:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    salary_entry = tk.Entry(add_window, width=30)
    salary_entry.grid(row=2, column=1, padx=10, pady=5)

    # Manager
    tk.Label(add_window, text="Manager:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    manager_entry = tk.Entry(add_window, width=30)
    manager_entry.grid(row=3, column=1, padx=10, pady=5)

    # Married
    tk.Label(add_window, text="Married:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    married_var = tk.StringVar(value="No")
    tk.Radiobutton(add_window, text="Yes", variable=married_var, value="Yes").grid(row=4, column=1, sticky="w")
    tk.Radiobutton(add_window, text="No", variable=married_var, value="No").grid(row=4, column=1, sticky="e")

    # Submit Button
    tk.Button(add_window, text="Submit", bg="light blue", command=submit_data).grid(row=5, column=1, pady=20)
