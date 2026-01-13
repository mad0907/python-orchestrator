import requests
import uuid
import schedule
import time

ORCHESTRATOR_URL = "http://127.0.0.1:8000"  # Localhost orchestrator
AGENTS = ["InventoryAgent", "OrderAgent", "RobotAgent", "AnalyticsAgent"]

# Step 1: Register all agents
def register_agents():
    bot_ids = {}
    for agent_name in AGENTS:
        response = requests.post(f"{ORCHESTRATOR_URL}/register_bot", params={"bot_name": agent_name})
        if response.status_code == 200:
            bot_id = response.json()
            print(f"Registered {agent_name} with bot_id: {bot_id}")
            bot_ids[agent_name] = bot_id
        else:
            print(f"Failed to register {agent_name}: {response.text}")
    return bot_ids

# Step 2: Submit job to orchestrator
def submit_job(bot_id, payload):
    response = requests.post(f"{ORCHESTRATOR_URL}/jobs/submit", params={"bot_id": bot_id, "payload": payload})
    if response.status_code == 200:
        job_id = response.json()["job_id"]
        print(f"Job submitted for bot {bot_id}. Job ID: {job_id}")
    else:
        print(f"Failed to submit job for bot {bot_id}: {response.text}")

# Step 3: Define worker task
def worker_task(bot_ids):
    for agent_name, bot_id in bot_ids.items():
        payload = f"Run {agent_name}"  # Customize payload if needed
        submit_job(bot_id, payload)

# Step 4: Scheduler
if __name__ == "__main__":
    bot_ids = register_agents()
    
    # Schedule every 5 minutes (change interval as needed)
    schedule.every(5).minutes.do(worker_task, bot_ids=bot_ids)
    
    print("Scheduler started. Running agents periodically...")
    while True:
        schedule.run_pending()
        time.sleep(1)
