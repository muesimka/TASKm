import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, master, text, command=None):
        super().__init__(master, text=text, command=command, font=("Arial", 12), padx=12, pady=6, cursor="hand2")
