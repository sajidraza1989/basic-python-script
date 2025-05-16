import tkinter as tk
import math

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            history_list.insert(tk.END, f"{expression} = {result}")
            input_var.set(result)
            expression = str(result)
        except Exception:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    elif text == "√":
        try:
            result = math.sqrt(float(expression))
            history_list.insert(tk.END, f"√({expression}) = {result}")
            input_var.set(result)
            expression = str(result)
        except Exception:
            input_var.set("Error")
            expression = ""
    elif text == "x²":
        try:
            result = float(expression) ** 2
            history_list.insert(tk.END, f"({expression})² = {result}")
            input_var.set(result)
            expression = str(result)
        except Exception:
            input_var.set("Error")
            expression = ""
    elif text == "%":
        try:
            result = float(expression) / 100
            history_list.insert(tk.END, f"({expression})% = {result}")
            input_var.set(result)
            expression = str(result)
        except Exception:
            input_var.set("Error")
            expression = ""
    else:
        expression += text
        input_var.set(expression)

def clear_history():
    history_list.delete(0, tk.END)

def save_history():
    with open("history.txt", "w") as file:
        for item in history_list.get(0, tk.END):
            file.write(item + "\n")
    print("History saved to 'history.txt'")

# Initialize main window
root = tk.Tk()
root.title("Advanced Calculator with History")
root.geometry("500x700")
root.configure(bg="#2c3e50")
root.resizable(False, False)

expression = ""
input_var = tk.StringVar()

# Input field
input_frame = tk.Frame(root, bg="#34495e", bd=5)
input_frame.pack(pady=20, padx=10, fill="x")
input_field = tk.Entry(input_frame, textvar=input_var, font=("Arial", 24), justify="right", bd=0, bg="#ecf0f1", fg="#2c3e50")
input_field.pack(ipady=15, fill="x")

# Button frame
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10, padx=10, expand=True, fill="both")

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["√", "x²", "%"]
]

for row in buttons:
    button_row = tk.Frame(button_frame, bg="#2c3e50")
    button_row.pack(expand=True, fill="both")
    for button_text in row:
        button = tk.Button(
            button_row, text=button_text, font=("Arial", 18), bg="#34495e", fg="#ecf0f1",
            activebackground="#1abc9c", activeforeground="#ffffff", relief="flat", bd=0
        )
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

# History frame
# History frame
history_frame = tk.Frame(root, bg="#2c3e50", bd=5)
history_frame.pack(pady=10, padx=10, fill="both", expand=True)

history_label = tk.Label(history_frame, text="History", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
history_label.pack(anchor="w")

history_list = tk.Listbox(history_frame, font=("Arial", 14), bg="#34495e", fg="#ecf0f1", height=5)
history_list.pack(fill="both", expand=True, pady=5)

# Button frame for history actions
history_button_frame = tk.Frame(history_frame, bg="#2c3e50")
history_button_frame.pack(fill="x", pady=5)

clear_button = tk.Button(history_button_frame, text="Clear History", font=("Arial", 14), bg="#e74c3c", fg="#ffffff", command=clear_history)
clear_button.pack(side="left", padx=10, pady=5)

save_button = tk.Button(history_button_frame, text="Save History", font=("Arial", 14), bg="#1abc9c", fg="#ffffff", command=save_history)
save_button.pack(side="right", padx=10, pady=5)

root.mainloop()