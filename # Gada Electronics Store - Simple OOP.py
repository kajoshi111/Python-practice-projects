class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = [
            Product("43\" 4K Smart TV", 329.99),
            Product("55\" 4K QLED TV", 649.99),
            Product("Refrigerator 300L", 799.50),
            Product("Washing Machine 7kg", 449.00),
            Product("Microwave 1000W", 119.99),
            Product("Vacuum Cleaner", 159.99),
            Product("Steam Iron", 39.99),
            Product("Air Conditioner 12k BTU", 399.00),
            Product("Bluetooth Speaker", 59.99),
            Product("2-Slice Toaster", 24.99),
        ]
        self.cart = []

    def show_products(self):
        print("\n--- Gada Electronics Product List ---")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} - ${product.price:.2f}")

    def add_to_cart(self, product_number, quantity):
        if 1 <= product_number <= len(self.products):
            product = self.products[product_number - 1]
            self.cart.append((product, quantity))
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print("Invalid product number!")

    def show_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("\n--- Your Cart ---")
        total = 0
        for product, qty in self.cart:
            cost = product.price * qty
            print(f"{product.name} (x{qty}) = ${cost:.2f}")
            total += cost
        print(f"Total so far: ${total:.2f}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Cannot checkout.")
            return

        total = sum(product.price * qty for product, qty in self.cart)

        print("\nDo you want delivery or pickup?")
        print("1. Pickup (Free)")
        print("2. Delivery ($10 extra)")
        choice = input("Enter 1 or 2: ")

        if choice == "2":
            total += 10
            address = input("Enter delivery address: ")
            print(f"Delivery will be sent to: {address}")
        else:
            print("You chose pickup from store.")

        print(f"\nFinal Total to Pay: ${total:.2f}")
        print("Thank you for shopping at Gada Electronics!")
        self.cart = []  # Clear cart after checkout


# ----------- Main Program ------------
store = Store()

while True:
    print("\n1. Show Products & Buy")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        store.show_products()
        while True:
            try:
                product_no = int(input("Enter product number (0 to stop): "))
                if product_no == 0:
                    break
                qty = int(input("Enter quantity: "))
                store.add_to_cart(product_no, qty)
            except ValueError:
                print("Invalid input! Please enter numbers.")

    elif option == "2":
        store.show_cart()

    elif option == "3":
        store.checkout()

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
