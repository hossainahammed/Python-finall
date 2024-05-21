from flask import Flask, render_template, request, jsonify
from product import Product, ShoppingCart

app = Flask(__name__)

products = [
    Product("Laptop", 1000),
    Product("Smartphone", 800),
    Product("Headphones", 100),
    Product("Tablet", 500)
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_name = data['product']
    product = next((p for p in products if  p.name == product_name), None)
    if product:
        cart.add_item(product)
        total_price = cart.total_price()
        return jsonify({'success': True, 'total_price': total_price})
    return jsonify({'success': False})

@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    product_name = data['product']
    product_index = next((i for i, p in enumerate(cart.items) if p.name == product_name), None)
    if product_index is not None:
        cart.remove_item(product_index)  # Pass the index of the product to remove
        total_price = cart.total_price()
        return jsonify({'success': True, 'total_price': total_price})
    return jsonify({'success': False})


if __name__ == '__main__':
    cart = ShoppingCart()
    app.run(debug=True)
