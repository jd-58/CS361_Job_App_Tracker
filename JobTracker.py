

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
print("Hello! Welcome to the Job Tracker.")
print("This program helps you track your job applications.")
print("Current features include adding jobs, viewing jobs, and removing jobs.")
print("You will have to have access to a keyboard to type in inputs in order to use features of this program.")
user_name = input("Please enter your name: ")
current_user.set_name(user_name)

while True:
    print("")
    print("Hello " + str(current_user.get_name()) + "!")
    print("")
    print("Job Tracker Menu:")
    print("1. Add a new job")
    print("2. View all jobs")
    print("3. Remove a job")
    print("4. Help/Application Information")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            # Collect job details
            title = input("Enter the job title: ")
            company = input("Enter the company: ")
            notes = input("Enter any notes about the job: ")
            print("")
            print("Here is the job you entered: ")
            print(f"Title: {title}, Company: {company}, Notes: {notes}")
            print("")
            job_add_confirmation = input("Is this information correct? (yes/no): ")
            while job_add_confirmation.lower() != "yes" and job_add_confirmation.lower() != "no":
                job_add_confirmation = input("Invalid response. Is this information correct? (yes/no)")
            if job_add_confirmation.lower() == "yes":
                # Create a new Job object and add it to the user's jobs list
                new_job = Job(title, "Applied", company, None, None, notes)
                current_user.add_job(new_job)
                print("Job added successfully!")
                break
            elif job_add_confirmation.lower() == "no":
                print("Let's try again. Re-enter the job details.")
                print("")

    elif choice == "2":
        # Display all jobs
        jobs = current_user.get_jobs()  # Access the user's jobs list
        if not jobs:
            print("No jobs added yet.")
        else:
            job_number = 1
            for job in jobs:
                print(f"{job_number}. Title: {job.get_title()}, Status: {job.get_status()}")
                job_number += 1
            detail_choice = input("Enter the number of a job to view details, or press Enter to skip: ")
            while detail_choice.isdigit() and 1 <= int(detail_choice) <= len(jobs):
                job = jobs[int(detail_choice) - 1]
                print("")
                print(
                    f"Title: {job.get_title()}\nStatus: {job.get_status()}\nCompany: "
                    f"{job.get_company()}\nNotes: {job.get_notes()}")
                print("")
                for job in jobs:
                    print(f"{job_number}. Title: {job.get_title()}, Status: {job.get_status()}")
                    job_number += 1
                detail_choice = input("Enter the number of a job to view details, or press Enter to skip: ")

    elif choice == "3":
        # Display jobs
        jobs = current_user.get_jobs()  # Access the user's jobs list
        if not jobs:
            print("Job list empty.")
        else:
            print("List of jobs added: ")
            job_number = 1
            for job in jobs:
                print(f"{job_number}. Title: {job.get_title()}, Company: {job.get_company()}, "
                      f"Status: {job.get_status()}")
                job_number += 1
            job_to_remove = input("Type the number of the job you would like to remove: ")
            while job_to_remove.isdigit() is False:
                job_to_remove = input("Invalid input. Please type a number of the job you would like to remove.")
            while int(job_to_remove) > len(jobs) or int(job_to_remove) <= 0:
                job_to_remove = input("Invalid selection. Type the number of the job you would like to remove: ")
            confirmation = input(f"Are you sure you want to remove job {job_to_remove}: "
                                 f"{jobs[int(job_to_remove) - 1].get_title()} at "
                                 f"{jobs[int(job_to_remove) - 1].get_company()}? (yes/no): ")
            if confirmation.lower() == "yes":
                del jobs[int(job_to_remove) - 1]
                print("Job successfully removed.")
            else:
                print("Job removal canceled.")

    elif choice == "4":
        print("App features:")
        print("In the job application tracker, you can currently add a job, view information about your added jobs, "
              "or remove a job.")
        print("")
        print("Tutorial: How to use the app")
        print("1. From the main menu, select option 1 to add a new job.")
        print("2. Enter the job title, company name, and any notes when prompted.")
        print("3. Once all details are entered, the job will be saved, and you'll see a confirmation message.")
        print("4. To view your jobs, return to the main menu and select option 2. "
              "This will show you the job title and company.")
        print("If you want more details about a job, enter its number when prompted.")
        print("5. To remove a job, select option 3. Type the number of the job you would like to remove.")
        print("If you need any help, you can always navigate to the main menu and select option 4.")
        print("")
        return_to_menu = input("Press enter to return to the main menu.")

    elif choice == "5":
        print("Exiting the Job Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


