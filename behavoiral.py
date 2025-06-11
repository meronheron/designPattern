#strategy
class PaymentStrategy:# Strategy Interface: Base for all payment methods
    def pay(self, amount):
        pass  # every strategy must have a 'pay' method

# Concrete Strategy 1: Paying with Cash
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount}ETB with cash. Handed over bills!"
# Concrete Strategy 2: Paying with ATM Card
class AtmCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} ETB with ATM card. Transaction approved!"
# Concrete Strategy 3: Paying with Mobile App
class MobileAppPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount}ETB with mobile app. Scanned QR code!"
    
class PizzaShop:# context: The Pizza Shop that processes payments 
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy  # Holds the chosen strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy  # Switch strategy if needed

    def checkout(self, amount):
        # PizzaShop calls the strategy's pay method
        result = self.payment_strategy.pay(amount)
        return result
shop = PizzaShop(CashPayment())  #cash payment
print(shop.checkout(560))  # PizzaShop calls CashPayment's pay method

shop.set_payment_strategy(AtmCardPayment())#ATM Card payment
print(shop.checkout(560))  # PizzaShop calls AtmCardPayment's pay method

shop.set_payment_strategy(MobileAppPayment())#Mobile App payment
print(shop.checkout(560))# PizzaShop calls MobileAppPayment's pay method