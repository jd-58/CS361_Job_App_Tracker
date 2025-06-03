import zmq


def sort_jobs_by_type(jobs):
    """Sort jobs by type (internship vs. job)."""
    jobs_copy = jobs.copy()
    n = len(jobs_copy)

    for i in range(n):
        for j in range(0, n - i - 1):
            type1 = jobs_copy[j].get("type", "").lower()
            type2 = jobs_copy[j + 1].get("type", "").lower()
            if type1 > type2:
                jobs_copy[j], jobs_copy[j + 1] = jobs_copy[j + 1], jobs_copy[j]

    return jobs_copy


def sort_jobs_by_status(jobs):
    """Sort jobs by application status."""
    jobs_copy = jobs.copy()
    n = len(jobs_copy)

    for i in range(n):
        for j in range(0, n - i - 1):
            status1 = jobs_copy[j].get("status", "").lower()
            status2 = jobs_copy[j + 1].get("status", "").lower()
            if status1 > status2:
                jobs_copy[j], jobs_copy[j + 1] = jobs_copy[j + 1], jobs_copy[j]

    return jobs_copy


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Reply socket
    socket.bind("tcp://127.0.0.1:5559")  # Bind to a port

    print("Sorting service is running on port 5559")

    while True:
        # Receive request
        message = socket.recv_json()
        action = message.get("action")
        jobs = message.get("jobs", [])

        if action == "sort_by_type":
            sorted_jobs = sort_jobs_by_type(jobs)
        elif action == "sort_by_status":
            sorted_jobs = sort_jobs_by_status(jobs)
        else:
            sorted_jobs = jobs  # Default: return unsorted jobs

        # Send response
        socket.send_json(sorted_jobs)


if __name__ == "__main__":
    main()