import threading
import time

class OrderAgent(threading.Thread):
    def __init__(self, orders, message_bus):
        super().__init__()
        self.orders = orders
        self.message_bus = message_bus

    def run(self):
        for order in self.orders:
            print(f"[OrderAgent] New order received: {order}")
            # Ask inventory agent for stock
            self.message_bus.put({'type': 'check_stock', 'item': order, 'reply_to': 'OrderAgent'})
            # Wait for stock status
            while True:
                if not self.message_bus.empty():
                    msg = self.message_bus.get()
                    if msg['type'] == 'stock_status' and msg['item'] == order:
                        if msg['available'] > 0:
                            print(f"[OrderAgent] Stock available for {order}, assigning robot.")
                            self.message_bus.put({'type': 'pick_item', 'item': order})
                        else:
                            print(f"[OrderAgent] Stock NOT available for {order}.")
                        break
            time.sleep(1)
