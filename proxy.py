#structural design pattern
from abc import ABC, abstractmethod
class PaymentService(ABC):#subject class to provide common interface
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass
class RealPaymentService(PaymentService):# real subject class that implements the PaymentService interface
    def process_payment(self, amount: float) -> str:
        # Simulate processing a payment
        return f"Processed payment of ${amount:.2f} successfully."
class PaymentServiceProxy(PaymentService):#proxy class 
    def __init__(self, is_authenticated: bool):
        self.is_authenticated = is_authenticated
        # Create the real payment service
        self.real_service = RealPaymentService()