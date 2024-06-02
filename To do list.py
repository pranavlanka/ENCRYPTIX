#Task -1
import tkinter as tk
from tkinter import ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x500")

        # Create a listbox to display the to-do list
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=10)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Create a entry field to add new tasks
        self.entry_field = tk.Entry(self.root, width=40)
        self.entry_field.pack(pady=10)

        # Create a button to add new tasks
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        # Create a button to update tasks
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=10)

        # Create a button to delete tasks
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.entry_field.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry_field.delete(0, tk.END)

    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task = self.listbox.get(selected_index)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(0, task)
            self.listbox.delete(selected_index)

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
