from abc import ABC, abstractmethod

class OrderObserver(ABC): #"Observer" Design Pattern Used
    @abstractmethod
    def update(self, order):
        pass
class EmailNotifier(OrderObserver):
    def update(self, order):
        print(f"Sending email notification for order {order.id}")
class ShipmentNotifier(OrderObserver):
    def update(self, order):
        print(f"Notifying shipment for order {order.id}")