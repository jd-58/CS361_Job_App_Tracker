import tkinter as tk
from tkinter import *
from tkinter import ttk

# Job Title, Custom name, notes section


class Job:
    def __init__(self, title, status, company, date_applied, description, notes):
        self._title = title
        self._status = status
        self._company = company
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

    def get_company(self):
        return self._company

    def set_comapny(self, new_company):
        self._company = new_company

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

    def get_jobs(self):
        return self._jobs_applied


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


current_user = User()  # Create a User object
user_name = input("Hello! Welcome to the job tracker. Please enter your name: ")
current_user.set_name(user_name)

while True:
    print("\nJob Tracker Menu:")
    print("1. Add a new job")
    print("2. View all jobs")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Collect job details
        title = input("Enter the job title: ")
        status = "Applied"
        company = input("Enter the company: ")
        notes = input("Enter any notes about the job: ")

        # Create a new Job object and add it to the user's jobs list
        new_job = Job(title, status, company, None, None, notes)
        current_user.add_job(new_job)
        print("Job added successfully!")

    elif choice == "2":
        # Display all jobs
        jobs = current_user.get_jobs()  # Access the user's jobs list
        if not jobs:
            print("No jobs added yet.")
        else:
            job_number = 1
            for job in jobs:
                print(f"{job_number}. Title: {job.get_title()}, Status: {job.get_status()}, Notes: {job.get_notes()}")
                job_number += 1

    elif choice == "3":
        print("Exiting the Job Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


