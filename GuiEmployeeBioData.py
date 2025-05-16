from tkinter import *
from tkinter import filedialog
import mysql.connector
import shutil

def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    salary = salary_entry.get()
    manager = manager_entry.get()
    married = married_var.get()
    cv_path = cv_label.cget("text")

    # Check if a CV is selected
    if cv_path == "No file selected":
        print("Please upload a CV before submitting.")
        return

    # Upload CV to the destination
    try:
        file_extension = cv_path.split('.')[-1]  # Extract the file extension
        destination = f"D:/Uploaded_CVs/{cv_path.split('/')[-1]}"  # Preserve original file name and extension
        shutil.copy(cv_path, destination)
        cv_path = destination  # Update cv_path to the destination path
        print("CV uploaded successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")
        return

    # Save data to MySQL database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="python_db"
        )
        cursor = connection.cursor()
        query = "INSERT INTO employees (name, age, salary, manager, married, cv_path) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, salary, manager, married, cv_path))
        connection.commit()
        cursor.close()
        connection.close()
        print("Data saved successfully!")
        root.destroy()  # Close the form
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def browse_cv():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_path:
        cv_label.config(text=file_path)

root = Tk()
root.title("Employee Bio-Data Form")
root.geometry("400x400")

# Name
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=W)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Age
Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
age_entry = Entry(root, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Salary
Label(root, text="Salary:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
salary_entry = Entry(root, width=30)
salary_entry.grid(row=2, column=1, padx=10, pady=5)

# Manager
Label(root, text="Manager:").grid(row=3, column=0, padx=10, pady=5, sticky=W)
manager_entry = Entry(root, width=30)
manager_entry.grid(row=3, column=1, padx=10, pady=5)

# Married
Label(root, text="Married:").grid(row=4, column=0, padx=10, pady=5, sticky=W)
married_var = StringVar(value="No")
Radiobutton(root, text="Yes", variable=married_var, value="Yes").grid(row=4, column=1, sticky=W)
Radiobutton(root, text="No", variable=married_var, value="No").grid(row=4, column=1, sticky=E)

# Upload CV
Label(root, text="Upload CV:").grid(row=5, column=0, padx=10, pady=5, sticky=W)
Button(root, text="Browse", command=browse_cv).grid(row=5, column=1, sticky=W)
cv_label = Label(root, text="No file selected", fg="gray")
cv_label.grid(row=6, column=1, padx=10, pady=5, sticky=W)

# Submit Button
Button(root, text="Submit", bg="light blue", command=submit_data).grid(row=7, column=1, pady=20)

root.mainloop()