import string

from flask import Flask

app = Flask(__name__)


@app.route('/admin/dish_list', methods=['GET', 'PUT'])
def dish_list(dish: list):  # put application's code here
    return


@app.route('/admin/add_new_dish', methods=['POST/PUT'])
def dish_add():  # put application's code here
    return


@app.route('/admin/dishes/<dish>', methods=['GET', 'PUT', 'DELETE'])
def dish_format():  # put application's code here
    return


@app.route('/admin/active_orders', methods=['GET'])
def active_orders(order: list):  # put application's code here
    return


@app.route('/admin/orders/,<order_id>', methods=['GET', 'PUT', 'DELETE'])
def admin_orders(order_id: int):  # put application's code here
    return


@app.route('/admin/category', methods=['GET', 'PUT', 'DELETE'])
def admin_category(admin_cat: string):  # put application's code here
    return


@app.route('/admin/search', methods=['GET/POST'])
def admin_search():  # put application's code here
    return


if __name__ == '__main__':
    app.run()
