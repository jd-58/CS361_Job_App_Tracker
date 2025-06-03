import zmq
from datetime import datetime

def validate_and_add_job(job_details):
    """Validate job details and return a response."""
    if not job_details.get("title") or not job_details.get("company"):
        return {"status": "error", "message": "Title and company are required."}

    # Add default values if missing
    job_details["notes"] = job_details.get("notes", None)
    job_details["location"] = job_details.get("location", None)
    job_details["date_added"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    job_details["status"] = job_details.get("status", "Applied")

    return {"status": "success", "job": job_details}

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Reply socket
    socket.bind("tcp://127.0.0.1:5556")  # Bind to a new port for the microservice

    print("Job Creation Service is running...")

    while True:
        # Receive job details from JobTracker
        job_details = socket.recv_json()

        # Validate and add job
        response = validate_and_add_job(job_details)

        # Send response back to JobTracker
        socket.send_json(response)

if __name__ == "__main__":
    main()