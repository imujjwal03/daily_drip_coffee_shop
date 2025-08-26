class Coffee:
    # initialize coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    # initialize order with empty list
    def __init__(self):
        self.items = []

    # add coffee to order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to order.")

    # calculate total price of order
    def total_price(self):
        return sum(item.price for item in self.items)

    # show order details 
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return 

        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price}")
        print(f"Total: ₹{self.total_price()}\n")  

    # handle checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Order confirmed! Thank you for your purchase.")
            self.items.clear()
        else:
            print("Checkout cancelled.")


# display menu and handle user input
def main():
    menu = [
        Coffee("Espresso", 50),
        Coffee("Latte", 70),
        Coffee("Cappuccino", 80),
        Coffee("Americano", 60),
        Coffee("Mocha", 90)
    ]
    order = Order()
    
    # user interaction loop
    while True:
        print("\n--- Daily Drip Coffee Shop ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ₹{coffee.price}")
        print("6. View Order")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose an option: ")
        if choice in ['1', '2', '3', '4', '5']:
            order.add_item(menu[int(choice) - 1])
        elif choice == '6':
            order.show_order()
        elif choice == '7':
            order.checkout()
            print("Thank you for visiting Daily Drip!")
            break
        elif choice == '8':
            print("Thank you for visiting Daily Drip!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
