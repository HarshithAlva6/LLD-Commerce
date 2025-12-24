
import uuid
from Design.Factory import StateFactory
from Design.Observer import EmailNotifier, ShipmentNotifier
from Design.Strategy import CreditCardPayment, CryptoPayment

class Order:
    def __init__(self, user):
        self.id = uuid.uuid4()
        self._user = user
        self._items = [] #Encapsulation Used with _ for private
        self._state = StateFactory.get_state("NEW") #Factory Pattern Used
        self._observers = [] #Need Array since One-To-Many relationship

    def change_state(self, newState):
        self._state = newState
    def add_item(self, item):
        self._state.handle_add_item(self, item)
    def get_total(self):
        return sum(item.price for item in self._items)
    def pay(self, payStrategy): #No Array since One-to-One relationship
        total = self.get_total()
        payStrategy.collect_pay(total)
        self._state.handle_pay(self)
        self.notify()
    def attach(self, observer):
        self._observers.append(observer)
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class OrderFacade: #"Facade" Design Pattern Used
    def place_order(self, user, items, payStrategy):
        order = Order(user)
        order.attach(EmailNotifier())
        order.attach(ShipmentNotifier())
        for item in items:
            order.add_item(item)
        strategy = self._get_strategy(payStrategy)
        order.pay(strategy)
        return order
    
    def _get_strategy(self, payStrategy):
        strategies = {
            "CREDIT_CARD": CreditCardPayment(),
            "CRYPTO": CryptoPayment()
        }
        return strategies.get(payStrategy)