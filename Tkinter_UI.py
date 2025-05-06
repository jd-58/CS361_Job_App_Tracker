# Name: Jacob Deaton
# OSU Email: deatonja@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment:
# Due Date:
# Description:
import tkinter as tk
from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x200")
        self.current_user = None  # To store the user's name
        self.name_page()

    def name_page(self):
        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create the Name Page
        frame = Frame(self.master)
        frame.pack()

        label = ttk.Label(frame, text="Enter your name:")
        label.pack(pady=10)

        self.name_entry = ttk.Entry(frame)
        self.name_entry.pack(pady=10)

        submit_button = ttk.Button(frame, text="Submit", command=self.welcome_page)
        submit_button.pack(pady=10)

    def welcome_page(self):
        # Get the user's name
        user_name = self.name_entry.get().strip()
        if not user_name:
            return  # Do nothing if the name is empty

        self.current_user = user_name

        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create the Welcome Page
        frame = Frame(self.master)
        frame.pack()

        label = ttk.Label(frame, text=f"Welcome, {self.current_user}!")
        label.pack(pady=10)

        add_job_button = ttk.Button(frame, text="Add Job", command=self.add_job_page)
        add_job_button.pack(pady=10)

    def add_job_page(self):
        # Clear the window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create the Add Job Page
        frame = Frame(self.master)
        frame.pack()

        label = ttk.Label(frame, text="Add a Job")
        label.pack(pady=10)

        back_button = ttk.Button(frame, text="Back to Welcome Page", command=self.welcome_page)
        back_button.pack(pady=10)


# Run the application
"""root = Tk()
App(root)
root.mainloop()"""