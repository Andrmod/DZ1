class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):
        return self.stock >= quantity

    def update_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if not product.is_available(quantity):
            print(f"Insufficient stock for {product.name}.")
            return

        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

        product.update_stock(quantity)
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_product(self, product_name):
        if product_name in self.items:
            product = self.items[product_name]['product']
            quantity = self.items[product_name]['quantity']
            product.stock += quantity
            del self.items[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("\nYour Cart:")
        for item_name, details in self.items.items():
            product = details['product']
            quantity = details['quantity']
            print(f"{item_name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


if __name__ == "__main__":
    # Sample products
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Mouse", 25.50, 50)
    product3 = Product("Keyboard", 45.00, 30)

    # Cart instance
    cart = Cart()

    while True:
        print("\nOnline Store")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Products:")
            for product in [product1, product2, product3]:
                print(product)

        elif choice == "2":
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))

            product_map = {product1.name: product1, product2.name: product2, product3.name: product3}
            if product_name in product_map:
                cart.add_product(product_map[product_name], quantity)
            else:
                print("Product not found.")

        elif choice == "3":
            product_name = input("Enter product name to remove: ")
            cart.remove_product(product_name)

        elif choice == "4":
            cart.display_cart()

        elif choice == "5":
            print(f"Total amount: ${cart.calculate_total():.2f}")
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")
