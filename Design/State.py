from abc import ABC, abstractmethod

class OrderState(ABC): #"State" Design Pattern Used
    @abstractmethod
    def handle_add_item(self, order, item): #Add self to avoid "Slot" confusion
        pass
    @abstractmethod
    def handle_pay(self, order):
        pass
class NewState(OrderState):
    def handle_add_item(self, order, item): #Dependency Injection Used for order
        order._items.append(item)
    def handle_pay(self, order):
        order.change_state(PaidState()) 
class PaidState(OrderState):
    def handle_add_item(self, order, item):
        raise Exception("Cannot add items to paid order")
    def handle_pay(self, order):
        raise Exception("Order is already paid")