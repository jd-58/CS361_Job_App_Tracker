

# Job Title, Custom name, notes section
import zmq
from datetime import datetime
import json

class Job:
    def __init__(self, title, status, company, date_applied, description, notes, type):
        self._title = title
        self._status = status
        self._company = company
        self._date_applied = date_applied
        self._description = description
        self._notes = notes
        self._type = type

    # Getter and Setter for title
    def get_title(self):
        return self._title

    def set_title(self, new_title):
        self._title = new_title

    def get_type(self):
        return self._type

    def set_type(self, new_type):
        self._type = new_type

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

dummy_jobs = [
    Job(
        title="Software Engineer",
        status="Applied",
        company="Meta",
        date_applied="2023-10-01",
        description="Develop and maintain software applications.",
        notes="Focus on backend development.",
        type="Job"
    ),
    Job(
        title="Web Developer",
        status="Applied",
        company="Microsoft",
        date_applied="2023-10-01",
        description="Create web apps in JavaScript",
        notes="Focus on backend development.",
        type="Job"
    ),
    Job(
        title="Data Analyst",
        status="Interview Scheduled",
        company="Amazon",
        date_applied="2023-09-15",
        description="Analyze and interpret complex data sets.",
        notes="Prepare for SQL and Python technical questions.",
        type="Internship"
    ),
    Job(
        title="Software Engineer Intern",
        status="Offer Received",
        company="Google",
        date_applied="2023-08-20",
        description="Lead product development and strategy.",
        notes="Consider relocation package.",
        type="Internship"
    )
]

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

test_user = User()
test_user.set_name("Test User")

# Add dummy jobs to the test user
for job in dummy_jobs:
    test_user.add_job(job)


def get_job_statistics(current_user):
    """Retrieve job statistics using the Statistics Microservice."""
    jobs = [{"status": job.get_status()} for job in current_user.get_jobs()]
    if not jobs:
        print("No jobs added yet.")
        return

    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Request socket
    socket.connect("tcp://127.0.0.1:5555")  # Connect to the Stats Microservice

    print("\nJob Statistics Menu:")
    print("1. Percentage of jobs with status 'Applied'")
    print("2. Percentage of jobs with status 'In Progress'")
    print("3. Percentage of jobs with status 'Offer'")
    print("4. Percentage of jobs with status 'Denied'")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        query_status = "Applied"
    elif choice == "2":
        query_status = "In Progress"
    elif choice == "3":
        query_status = "Offer"
    elif choice == "4":
        query_status = "Denied"
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")
        return

    # Send request to the stats microservice
    request = {"jobs": jobs, "query": query_status}
    socket.send_string(json.dumps(request))

    # Receive and process the response
    response = json.loads(socket.recv_string())
    percentage = response.get("percentage", 0.0)

    print(f"Percentage of jobs with status '{query_status}': {percentage:.2f}%")

def update_job_status(current_user):
    """Update the status of a job."""
    jobs = current_user.get_jobs()  # Access the user's jobs list
    if not jobs:
        print("No jobs available to update.")
        return

    print("List of jobs:")
    for idx, job in enumerate(jobs, start=1):
        print(f"{idx}. Title: {job.get_title()}, Company: {job.get_company()}, Status: {job.get_status()}")

    while True:
        job_to_update = input("Enter the number of the job you want to update: ")
        if job_to_update.isdigit() and 1 <= int(job_to_update) <= len(jobs):
            job_to_update = int(job_to_update) - 1
            break
        else:
            print("Invalid input. Please enter a valid job number.")

    new_status = input("Enter the new status for the job: ").strip()
    while not new_status:
        new_status = input("Status cannot be empty. Enter the new status for the job: ").strip()

    jobs[job_to_update].set_status(new_status)
    print(f"Job status updated successfully to '{new_status}'.")

def add_job_via_service(current_user):
    """Send job details to the microservice for validation and addition."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Request socket
    socket.connect("tcp://127.0.0.1:5556")  # Connect to the job creation microservice

    # Collect job details
    title = input("Enter the job title: ")
    company = input("Enter the company: ")
    notes_confirmation = input("Would you like to enter notes about your job entry? (yes/no): ")
    notes = input("Enter any notes about the job: ") if notes_confirmation.lower() == "yes" else None
    location = input("Enter the job location (optional): ")

    # Prompt for job type
    while True:
        print("\nSelect the job type:")
        print("1. Job")
        print("2. Internship")
        type_choice = input("Enter your choice (1/2): ")

        if type_choice == "1":
            job_type = "Job"
            break
        elif type_choice == "2":
            job_type = "Internship"
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Prepare job details
    job_details = {
        "title": title,
        "company": company,
        "notes": notes,
        "location": location if location else None,
        "type": job_type,
        "status": "Applied",
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Send job details to the microservice
    socket.send_json(job_details)

    # Receive response from the microservice
    response = socket.recv_json()

    if response.get("status") == "success":
        print("Job added successfully!")
        current_user.add_job(Job(
            title=response["job"]["title"],
            status=response["job"]["status"],
            company=response["job"]["company"],
            date_applied=response["job"]["date_added"],
            description=None,
            notes=response["job"]["notes"],
            type=response["job"]["type"]
        ))
    else:
        print(f"Error: {response.get('message')}")

def get_job_sorting(action, jobs):
    """Send sorting request to the microservice and receive sorted jobs."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Request socket
    socket.connect("tcp://127.0.0.1:5559")  # Connect to the microservice

    # Send request
    socket.send_json({"action": action, "jobs": jobs})

    # Receive response
    sorted_jobs = socket.recv_json()
    return sorted_jobs

def view_jobs_with_sorting(current_user):
    """View jobs with sorting options."""
    jobs = [{"title": job.get_title(), "type": job.get_type(), "status": job.get_status()} for job in current_user.get_jobs()]
    if not jobs:
        print("No jobs added yet.")
        return

    print("Jobs:")
    for idx, job in enumerate(jobs, start=1):
        print(f"{idx}. Title: {job['title']}, Type: {job['type']}, Status: {job['status']}")

    print("\nSorting options:")
    print("1. Sort by job type")
    print("2. Sort by application status")
    print("3. Exit sorting")

    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            print("\nHow would you like to sort the jobs?")
            print("1. Sort by type with jobs first")
            print("2. Sort by type with internships first")
            sort_choice = input("Enter your choice (1/2): ")

            if sort_choice == "1":
                sorted_jobs = get_job_sorting("sort_by_type", jobs)[::-1]
                break
            elif sort_choice == "2":
                # Reverse the order to prioritize internships first
                sorted_jobs = get_job_sorting("sort_by_type", jobs)
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    elif choice == "2":
        sorted_jobs = get_job_sorting("sort_by_status", jobs)
    else:
        return

    print("\nSorted Jobs:")
    for idx, job in enumerate(sorted_jobs, start=1):
        print(f"{idx}. Title: {job['title']}, Type: {job['type']}, Status: {job['status']}")

def get_job_information(current_user):
    """Retrieve job information using the Job Information Microservice."""
    jobs = [{"title": job.get_title(), "status": job.get_status()} for job in current_user.get_jobs()]
    if not jobs:
        print("No jobs added yet.")
        return

    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Request socket
    socket.connect("tcp://127.0.0.1:5558")  # Connect to the Job Information Microservice

    print("\nJob Information Menu:")
    print("1. View total number of jobs")
    print("2. View number of jobs by status")
    print("3. View job search statistics")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        total_jobs_response = request_job_information(current_user.get_jobs(), "get_job_count")
        print(f"Total jobs: {total_jobs_response.get('total_jobs', 0)}")
    elif choice == "2":
        status_counts_response = request_job_information(current_user.get_jobs(), "get_job_count_by_status")
        print("Jobs by status:")
        for status, count in status_counts_response.get("status_counts", {}).items():
            print(f"  {status}: {count}")
    elif choice == "3":
        get_job_statistics(current_user)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")


def request_job_information(jobs, action):

    job_dicts = [{"status": job.get_status()} for job in jobs]

    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Request socket
    socket.connect("tcp://127.0.0.1:5558")  # Connect to job_information microservice

    request = {"action": action, "jobs": job_dicts}
    socket.send_json(request)

    response = socket.recv_json()

    # Close connection
    socket.close()
    context.term()

    return response

#current_user = User()  # Create a User object
current_user = test_user
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
    print("4. Update a job's status")
    print("5. View Job Statistics")
    print("6. Help/Application Information")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_job_via_service(current_user)

    elif choice == "2":
        # View jobs with sorting options
        view_jobs_with_sorting(current_user)

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
        update_job_status(current_user)

    elif choice == "5":
        get_job_information(current_user)

    elif choice == "6":
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

    elif choice == "7":
        print("Exiting the Job Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


