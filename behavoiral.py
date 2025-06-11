#strategy
class PaymentStrategy:# Strategy Interface: Base for all payment methods
    def pay(self, amount):
        pass  # every strategy must have a 'pay' method

# Concrete Strategy 1: Paying with Cash
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with cash. Handed over bills!"
# Concrete Strategy 2: Paying with ATM Card
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with ATM card. Transaction approved!"
# Concrete Strategy 3: Paying with Mobile App
class MobileAppPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with mobile app. Scanned QR code!"