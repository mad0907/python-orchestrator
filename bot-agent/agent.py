import requests
import time

ORCH = "http://localhost:8000"

r = requests.post(f"{ORCH}/bots/register", params={"name":"Bot-1"})
bot_id = r.json()["bot_id"]

while True:
    requests.post(f"{ORCH}/bots/{bot_id}/heartbeat")
    time.sleep(10)
