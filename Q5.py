import sys
class BankingApp:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive."
        self.balance += amount
        return True, f"Successfully deposited ${amount:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            return False, "Insufficient balance."
        self.balance -= amount
        return True, f"Successfully withdrew ${amount:.2f}"
def main():
    app = BankingApp(100.0)
    print("--- Welcome to the Simple Banking Application ---")
    
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")  
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            print(f"Current Balance: ${app.check_balance():.2f}")
        elif choice == '2':
            try:
                amt = float(input("Enter deposit amount: "))
                success, msg = app.deposit(amt)
                print(msg)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif choice == '3':
            try:
                amt = float(input("Enter withdrawal amount: "))
                success, msg = app.withdraw(amt)
                print(msg)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif choice == '4':
            print("Thank you for using Simple Banking Application!")
            sys.exit(0)
        else:
            print("Invalid selection. Please choose an option between 1 and 4.")
if __name__ == '__main__':
    main()
