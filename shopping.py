class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity}x {self.name} @ ${self.price:.2f} each = ${self.total_price():.2f}"


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return f"{item_name} telah di hapus dari shopping list."
        return f"{item_name} tidak di temukan shopping list."

    def total_cost(self):
        return sum(item.total_price() for item in self.items)

    def show_list(self):
        if not self.items:
            return "Shopping list is empty."
        return "\n".join(str(item) for item in self.items)

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat daftar belanja
    shopping_list = ShoppingList()

    # Menambahkan item ke daftar belanja
    shopping_list.add_item(ShoppingItem("pisang_keju", 2, 0.5))
    shopping_list.add_item(ShoppingItem("pisang_coklat", 5, 0.3))
    shopping_list.add_item(ShoppingItem("pisang_strawberry", 1, 1.2))

    # Menampilkan daftar belanja
    print("Daftar Belanja:")
    print(shopping_list.show_list())

    # Menampilkan total biaya
    print(f"\nTotal Biaya: ${shopping_list.total_cost():.2f}")

    # Menghapus item dari daftar belanja
    print(shopping_list.remove_item("pisang_keju"))

    # Menampilkan daftar belanja setelah penghapusan
    print("\nDaftar Belanja setelah penghapusan:")
    print(shopping_list.show_list())
    print(f"\nTotal Biaya setelah penghapusan: ${shopping_list.total_cost():.2f}")