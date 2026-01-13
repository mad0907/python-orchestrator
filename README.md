🚀 Python Agentic Orchestrator

This project is a lightweight Python version of UiPath Orchestrator / Automation Anywhere Control Room.

It allows you to:

Register bots

Submit jobs

Queue executions

Schedule agents

Track logs

Run multi-agent workflows

All using FastAPI + Python.

🗂 Folder Structure
python-orchestrator/
│
├── orchestrator/      ← Control Room
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── queue.py
│   ├── scheduler.py
│   └── routers/
│       ├── bots.py
│       ├── jobs.py
│       ├── logs.py
│       └── health.py
│
├── bot-agent/         ← Agents (Order, Inventory, Robot, Analytics)
│   ├── main.py
│   ├── order_agent.py
│   ├── inventory_agent.py
│   ├── robot_agent.py
│   └── analytics_agent.py

🔧 How to Run Orchestrator
🐳 Running the Orchestrator with Docker (Recommended)

This orchestrator is designed to run as a containerized Control Room, just like UiPath Orchestrator or Automation Anywhere Control Room.

It uses:

FastAPI for APIs

PostgreSQL for persistence

Docker Compose for orchestration

1️⃣ Prerequisites

Make sure you have installed:

Docker

Docker Compose

Verify:

docker --version
docker-compose --version

2️⃣ Start the Orchestrator

From the root folder (where docker-compose.yml is located):

docker-compose down -v
docker-compose build
docker-compose up


This will:

Start PostgreSQL

Start the Orchestrator API

Initialize the job queue and scheduler

3️⃣ Access the Control Room

Once started, the Orchestrator is available at:

http://127.0.0.1:8000


Health check:

http://127.0.0.1:8000/health


If this returns {"status":"ok"}, your Control Room is live.

4️⃣ Core Orchestrator APIs
Purpose	Endpoint
Register Agent	POST /register_bot
Submit Job	POST /jobs/submit
Get Logs	GET /logs/{job_id}
Health Check	GET /health

These APIs together form your Python RPA Control Room.

🤖 Running the Multi-Agent System

After the orchestrator is running, go to the bot-agent folder:

cd bot-agent
python main.py


This script will:

Register all agents

Submit jobs

Schedule them every 5 minutes

It behaves exactly like:

UiPath Robot Scheduler + Job Dispatcher
