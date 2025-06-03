# Name: Jacob Deaton
# OSU Email: deatonja@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment:
# Due Date:
# Description:

import zmq

def get_job_count(jobs):
    """Return the total number of jobs."""
    return len(jobs)

def get_job_count_by_status(jobs):
    """Return the count of jobs for each status."""
    status_counts = {}
    for job in jobs:
        status = job.get("status", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
    return status_counts

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Reply socket
    socket.bind("tcp://127.0.0.1:5558")  # Bind to a port for the microservice

    print("Job Information Microservice is running on port 5558")

    while True:
        # Receive request
        message = socket.recv_json()
        action = message.get("action")
        jobs = message.get("jobs", [])

        if action == "get_job_count":
            response = {"total_jobs": get_job_count(jobs)}
        elif action == "get_job_count_by_status":
            response = {"status_counts": get_job_count_by_status(jobs)}
        else:
            response = {"error": "Invalid action"}

        # Send response
        socket.send_json(response)

if __name__ == "__main__":
    main()