import threading
import time

class AnalyticsAgent(threading.Thread):
    def __init__(self, message_bus):
        super().__init__()
        self.message_bus = message_bus

    def run(self):
        while True:
            print(f"[AnalyticsAgent] Messages in bus: {self.message_bus.qsize()}")
            time.sleep(5)
