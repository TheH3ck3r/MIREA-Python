import pytest
import deal
from decimal import Decimal, InvalidOperation

@deal.pre(lambda self: self.balance >= 0 )
@deal.pre(lambda self: isinstance(self.balance, Decimal) )

class BankAccount:
    def __init__(self, balance: Decimal = Decimal(0.0)):
        if balance < Decimal(0):
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.balance = balance

    def deposit(self, amount: Decimal):
        if amount < Decimal(0):
            raise ValueError("Сумма зачисления не может быть отрицательной.")
        try:
            self.balance += amount
        except InvalidOperation:
            raise ValueError("Некорректная сумма зачисления.")
        return f"{amount} средств успешно зачислены на счёт."

    def withdraw(self, amount: Decimal):
        if amount < Decimal(0):
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счету.")
        try:
            self.balance -= amount
        except InvalidOperation:
            raise ValueError("Некорректная сумма снятия.")
        return f"{amount} средств успешно сняты с счёта."

    def check_balance(self):
        return f"Баланс счёта: {self.balance}"

def test_bank_account():
    account = BankAccount()
    assert account.check_balance() == "Баланс счёта: 0"
    
    assert account.deposit(Decimal(0.2)) == "0.2 средств успешно зачислены на счёт."
    assert account.check_balance() == "Баланс счёта: 0.2"
    
    assert account.withdraw(Decimal(0.1)) == "50 средств успешно сняты с счёта."
    assert account.check_balance() == "Баланс счёта: 0.1"
    
    with pytest.raises(ValueError):
        account.withdraw(Decimal(0.6))
    
    assert account.check_balance() == "Баланс счёта: 0.1"

test_bank_account()