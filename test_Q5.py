import pytest
from Q5 import BankingApp



def test_initial_balance():
    app = BankingApp(150.0)
    assert app.check_balance() == 150.0

def test_deposit_success():
    app = BankingApp(100.0)
    success, msg = app.deposit(50.0)
    assert success is True
    assert app.check_balance() == 150.0

def test_deposit_negative_value():
    app = BankingApp(100.0)
    success, msg = app.deposit(-25.0)
    assert success is False
    assert app.check_balance() == 100.0

def test_withdrawal_success():
    app = BankingApp(100.0)
    success, msg = app.withdraw(40.0)
    assert success is True
    assert app.check_balance() == 60.0

def test_withdrawal_insufficient_funds():
    app = BankingApp(50.0)
    success, msg = app.withdraw(75.0)
    assert success is False
    assert app.check_balance() == 50.0
