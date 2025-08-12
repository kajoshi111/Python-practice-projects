# Bank Account

class BankAccount:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

class User:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.account = BankAccount(name)

class Bank:
    def __init__(self):
        self.users = {}  # name -> User

    def register(self, name, pin):
        if name in self.users:
            print("User already exists.")
            return None
        user = User(name, pin)
        self.users[name] = user
        print("Registration successful.")
        return user

    def login(self, name, pin):
        user = self.users.get(name)
        if user and user.pin == pin:
            print(f"Welcome, {name}!")
            return user
        print("Invalid name or PIN.")
        return None

    def transfer(self, from_user, to_name, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        to_user = self.users.get(to_name)
        if not to_user:
            print("Recipient not found.")
            return
        if amount > from_user.account.balance:
            print("Insufficient funds.")
            return
        from_user.account.balance -= amount
        to_user.account.balance += amount
        print(f"Transferred ${amount:.2f} to {to_name}. Your new balance: ${from_user.account.balance:.2f}")

# ---------- Main ----------
bank = Bank()
current_user = None

while True:
    if current_user is None:
        print("\n--- Bank ---")
        print("1) Register")
        print("2) Login")
        print("3) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            pin = input("PIN (numbers only): ").strip()
            bank.register(name, pin)

        elif choice == "2":
            name = input("Name: ").strip()
            pin = input("PIN: ").strip()
            current_user = bank.login(name, pin)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
    else:
        print(f"\n--- Welcome {current_user.name} ---")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Transfer")
        print("4) Check balance")
        print("5) Logout")
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Enter a number.")
                continue
            current_user.account.deposit(amt)

        elif choice == "2":
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Enter a number.")
                continue
            current_user.account.withdraw(amt)

        elif choice == "3":
            to_name = input("Send to (name): ").strip()
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Enter a number.")
                continue
            bank.transfer(current_user, to_name, amt)

        elif choice == "4":
            bal = current_user.account.balance
            print(f"Balance: ${bal:.2f}")

        elif choice == "5":
            print("Logged out.")
            current_user = None

        else:
            print("Invalid choice.")
