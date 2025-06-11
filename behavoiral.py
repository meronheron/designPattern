#strategy
class PaymentStrategy:# Strategy Interface: Base for all payment methods
    def pay(self, amount):
        pass  # every strategy must have a 'pay' method

# Concrete Strategy 1: Paying with Cash
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with cash. Handed over bills!"