
from abc import ABC, abstractmethod

class PaymentStrategy(ABC): #"Strategy" Design Pattern Used
    @abstractmethod
    def collect_pay(self, amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def collect_pay(self, amount):
        print(f"Collecting {amount} via Credit Card")
class CryptoPayment(PaymentStrategy):
    def collect_pay(self, amount):
        print(f"Collecting {amount} via Cryptocurrency")