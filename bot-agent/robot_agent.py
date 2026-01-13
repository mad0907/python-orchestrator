import threading
import time
import random

class RobotAgent(threading.Thread):
    def __init__(self, message_bus):
        super().__init__()
        self.message_bus = message_bus

    def run(self):
        while True:
            if not self.message_bus.empty():
                msg = self.message_bus.get()
                if msg['type'] == 'pick_item':
                    item = msg['item']
                    print(f"[RobotAgent] Picking up item: {item}")
                    time.sleep(random.randint(1, 3))  # simulate picking time
                    print(f"[RobotAgent] Delivered item: {item}")
            time.sleep(0.1)
