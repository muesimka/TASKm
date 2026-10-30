import tkinter as tk

class Listbox(tk.Listbox):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

    def add_to_list(self,content):
        self.insert(tk.END, content.get)

    def delete_list(self):
        self.delete(0, tk.END)