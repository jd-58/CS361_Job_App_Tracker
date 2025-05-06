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



current_user = User()  # Create a User object
user_name = input("Hello! Welcome to the job tracker. Please enter your name: ")
current_user.set_name(user_name)

while True:
    print("\nJob Tracker Menu:")
    print("1. Add a new job")
    print("2. View all jobs")
    print("3. Remove a job")
    print("4. Exit")

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
        # Display jobs
        jobs = current_user.get_jobs()  # Access the user's jobs list
        if not jobs:
            print("Job list empty.")
        else:
            print("List of jobs added: ")
            job_number = 1
            for job in jobs:
                print(f"{job_number}. Title: {job.get_title()}, Status: {job.get_status()}, Notes: {job.get_notes()}")
                job_number += 1
            job_to_remove = input("Type the number of the job you would like to remove: ")
            while int(job_to_remove) > len(jobs) or int(job_to_remove) <= 0:
                job_to_remove = input("Invalid selection. Type the number of the job you would like to remove: ")
            del jobs[int(job_to_remove) - 1]
            print("Job successfully removed.")

    elif choice == "4":
        print("Exiting the Job Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


