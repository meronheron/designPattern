#structural design pattern
from abc import ABC, abstractmethod
class PaymentService(ABC):#subject class to provide common interface
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass