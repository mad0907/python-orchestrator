import threading
import time

class InventoryAgent(threading.Thread):
    def __init__(self, inventory, message_bus):
        super().__init__()
        self.inventory = inventory
        self.message_bus = message_bus

    def run(self):
        while True:
            if not self.message_bus.empty():
                message = self.message_bus.get()
                if message['type'] == 'check_stock':
                    item = message['item']
                    reply_to = message['reply_to']
                    available = self.inventory.get(item, 0)
                    response = {
                        'type': 'stock_status',
                        'item': item,
                        'available': available
                    }
                    self.message_bus.put(response)
            time.sleep(0.1)
