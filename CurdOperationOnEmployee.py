import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def fetch_data():
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="python_db"
        )
        cursor = connection.cursor()

        # Fetch data from the employees table
        query = "SELECT * FROM employees"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Clear existing data in the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Insert fetched data into the Treeview
        for row in rows:
            tree.insert("", "end", values=row)

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

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

# Main window
root = tk.Tk()
root.title("Employee Data")
root.geometry("700x400")

# Frame for employee data
employee_frame = tk.Frame(root, bg="#f5f5f5")
employee_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Treeview for displaying employee data
columns = ("ID", "Name", "Age", "Salary", "Manager", "Married")
tree = ttk.Treeview(employee_frame, columns=columns, show="headings", height=10)

# Define column headings
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Salary", text="Salary")
tree.heading("Manager", text="Manager")
tree.heading("Married", text="Married")

# Define column widths
tree.column("ID", width=50, anchor="center")
tree.column("Name", width=150, anchor="center")
tree.column("Age", width=50, anchor="center")
tree.column("Salary", width=100, anchor="center")
tree.column("Manager", width=80, anchor="center")
tree.column("Married", width=80, anchor="center")

# Add Treeview to the frame
tree.pack(fill="both", expand=True)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(fill="x", pady=10)

# fetch_button = tk.Button(button_frame, text="Fetch Data", bg="#3498db", fg="white", command=fetch_data)
# fetch_button.pack(side="left", padx=10)

add_button = tk.Button(button_frame, text="Add Employee", bg="#2ecc71", fg="white", command=add_employee)
add_button.pack(side="right", padx=10)


if __name__ == "__main__":
    fetch_data();  # Initial fetch to display data

root.mainloop()