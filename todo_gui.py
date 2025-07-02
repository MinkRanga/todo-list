import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

# Function to update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# --- GUI Layout ---

# Input field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Add button
add_btn = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_btn.pack(pady=5)

# Task list
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# Delete button
delete_btn = tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task)
delete_btn.pack(pady=5)

# Start the app
root.mainloop()
