# Job Application Statistics Microservice

## 1. Requesting data

- **Protocol:** ZeroMQ REQ/REP over TCP  
- **Endpoint (service):** `tcp://<host>:5555`  
- **Message format:** JSON string  
  ```json
  {
    "jobs": [
      {"status": "<string>"},
      …
    ],
    "query": "<string>"  # one of: "Applied", "In Progress", "Offer", "Denied"
  }

## Example call:
socket.send_string(json.dumps({
  "jobs": [{"status":"Offer"}, {"status":"Applied"}],
  "query": "Offer"
}))

# 1. Environment Setup
Use a Python virtual environment to isolate dependencies:

Create a new virtual environment in the project directory

python3 -m venv .venv

# 2. Activate the Virtual Environment
Before installing packages or running code, activate the venv:

source .venv/bin/activate

_macOS note: If you see PEP 668 errors when installing packages into the system Python, this venv approach ensures you can install freely without modifying the OS-managed interpreter._

# 3. Install Dependencies
With the venv activated, upgrade pip and install ZeroMQ bindings:

pip install --upgrade pip

pip install pyzmq

# 4. Test and run:

Run your service (still in the venv):

python stats_service.py
In another shell (either activate the same venv or repeat steps 2–3 there) run your client:

python test_client.py