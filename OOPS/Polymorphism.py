# Polymorphism =    It is the ability of different objects to respond to the same function call in different ways.


class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Output: Bark
animal_sound(Cat())  # Output: Meow                    





class Payment:
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        return "Paid via Card"

class PayPalPayment(Payment):
    def pay(self):
        return "Paid via PayPal"


def process_payment(payment_method):
    print(payment_method.pay())


process_payment(CardPayment())    # Output: Paid via Card
process_payment(PayPalPayment())  # Output: Paid via PayPal