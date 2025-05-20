import zmq, json

def main():
    ctx = zmq.Context()
    socket = ctx.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Sample data: 5 jobs, 2 with the status "Offer"
    payload = {
      "jobs": [
        {"status":"Applied"},
        {"status":"Offer"},
        {"status":"In Progress"},
        {"status":"Offer"},
        {"status":"Applied"}
      ],
      "query": "Offer"
    }

    print("Sending request:", payload)
    socket.send_string(json.dumps(payload))

    reply = socket.recv_string()
    data = json.loads(reply)
    print("Received reply:", data)

if __name__ == "__main__":
    main()
