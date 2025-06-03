import zmq, json

def compute_percentage(jobs, query_status):
    if not jobs:
        return 0.0
    matching = sum(1 for job in jobs if job.get("status") == query_status)
    return 100.0 * matching / len(jobs)

def main():
    ctx = zmq.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Stats service listening on tcp://*:5555…")

    while True:
        message = socket.recv_string()
        request = json.loads(message)
        jobs = request.get("jobs", [])
        query = request.get("query", "")
        pct = compute_percentage(jobs, query)
        response = {"percentage": pct}
        socket.send_string(json.dumps(response))

if __name__ == "__main__":
    main()