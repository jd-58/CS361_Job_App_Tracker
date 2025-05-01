import tkinter as tk
from tkinter import *
from tkinter import ttk


class Job:
    def __init__(self, title, status, date_applied, description, notes):
        self._title = title
        self._status = status
        self._date_applied = date_applied
        self._description = description
        self._notes = notes

        # Getter and Setter for title
        def get_title(self):
            return self._title

        def set_title(self, new_title):
            self._title = new_title

        # Getter and Setter for status
        def get_status(self):
            return self._status

        def set_status(self, new_status):
            self._status = new_status

        # Getter and Setter for date_applied
        def get_date_applied(self):
            return self._date_applied

        def set_date_applied(self, new_date_applied):
            self._date_applied = new_date_applied

        # Getter and Setter for description
        def get_description(self):
            return self._description

        def set_description(self, new_description):
            self._description = new_description

        # Getter and Setter for notes
        def get_notes(self):
            return self._notes

        def set_notes(self, new_notes):
            self._notes = new_notes


class User:
    def __init__(self):
        self._name = None
        self._jobs_applied = []     # List of Job objects

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def add_job(self, new_job):
        """Add a job object to the list of jobs applied to."""
        # TODO: make this only append if new_job is a Job object
        self._jobs_applied.append(new_job)

    def remove_job(self, job_to_remove):
        # TODO: implement removing a job
        pass

    def clear_jobs(self):
        """Remove all jobs applied to"""
        self._jobs_applied = []


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


current_user = User()
user_name = input("Hello! Welcome to the job tracker. Please enter your name: ")
current_user.set_name(user_name)
welcome_message = "Welcome, " + current_user.get_name() + "! Type 1 if you would like to add a job. "
home_screen = input(welcome_message)
while home_screen != "1":
    home_screen = input("Invalid input. Type 1 to add a job. ")

