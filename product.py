class Product:
    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        self.description = description


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, index):
        del self.items[index]

    def total_price(self):
        return sum(item.price for item in self.items)


class Recommender:
    def __init__(self, products):
        self.products = products

    def recommend_products(self, cart_items):
        cart_product_names = [item.name for item in cart_items]
        recommended_products = []

        for product in self.products:
            if product.name not in cart_product_names:
                recommended_products.append(product)

        return recommended_products[:2]
