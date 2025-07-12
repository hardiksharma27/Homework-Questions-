from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(Payment):
    def make_payment(self):
        print("Paid using credit card")

class UPI(Payment):
    def make_payment(self):
        print("Paid using UPI")

creditcard = CreditCard()
creditcard.make_payment()

upi = UPI()
upi.make_payment()

OUTPUT --- 

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 11 Q3.py"
Paid using credit card
Paid using UPI
