import tkinter as tk
from tkinter import filedialog, messagebox
import zlib
import base64
import os

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def compress_file():
    input_file = file_entry.get()
    if not input_file or not os.path.isfile(input_file):
        messagebox.showerror("Error", "Please select a valid file.")
        return

    output_file = input_file + ".b64"
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)
            base64_data = base64.b64encode(compressed_data)

        with open(output_file, 'wb') as f_out:
            f_out.write(base64_data)

        messagebox.showinfo("Success", f"File compressed successfully to: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("File Compressor")
root.geometry("400x150")

# Configure grid to make the window responsive
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# File selection
tk.Label(root, text="Select File:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Compress button
compress_button = tk.Button(root, text="Compress File", bg="light blue", command=compress_file)
compress_button.grid(row=1, column=1, pady=20)

# Run the application
root.mainloop()