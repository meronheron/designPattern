#structural design pattern
from abc import ABC, abstractmethod
class PaymentService(ABC):#subject class to provide common interface
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass
class RealPaymentService(PaymentService):# real subject class that implements the PaymentService interface
    def process_payment(self, amount: float) -> str:#inherited from the subject class
        # simulate processing a payment
        return f"Processed payment of ${amount:.2f} successfully."
class PaymentServiceProxy(PaymentService):#proxy class 
    def __init__(self, is_authenticated: bool):
        self.is_authenticated = is_authenticated
        # Create the real payment service
        self.real_service = RealPaymentService()
    def process_payment(self, amount: float) -> str:#inherited from the subject class
        # Check if the user is authenticated
        if not self.is_authenticated:
            return "Error: You must be logged in to process payments!"
        # If authenticated, delegate to the real service
        return self.real_service.process_payment(amount)