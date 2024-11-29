import tkinter as tk
from tkinter import ttk

def upload_file():
    filepath = file_entry.get()
    if filepath:
        # Here you can implement the upload logic using Linode's API
        # For now, we'll just print the filepath
        print(f"Uploading file: {filepath}")
        file_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Linode Object Storage GUI")
root.geometry("1280x720")

# Create a frame for the file listing
list_frame = ttk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add a listbox to display files
file_listbox = tk.Listbox(list_frame, font=("Helvetica", 12))
file_listbox.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Add a scrollbar for the listbox
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=file_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
file_listbox.config(yscrollcommand=scrollbar.set)

# Create a frame for the input and button
input_frame = ttk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=10)

# Add an entry box for the file path
file_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Add an upload button
upload_button = ttk.Button(input_frame, text="Upload", command=upload_file)
upload_button.pack(side=tk.RIGHT)

# Start the GUI event loop
root.mainloop()
