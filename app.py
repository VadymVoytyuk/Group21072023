import string

from flask import Flask

app = Flask(__name__)


@app.route('/cart', methods=['GET', 'PUT'])
def cart():  # put application's code here
    return


@app.route('/cart/order', methods=['POST'])
def cart_order():  # put application's code here
    return


@app.route('/cart/add', methods=['POST/PUT'])
def cart_add():  # put application's code here
    return


@app.route('/user', methods=['GET', 'PUT/POST', 'DELETE'])
def user():  # put application's code here
    return


@app.route('/user/register', methods=['POST'])
def user_register():  # put application's code here
    return


@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():  # put application's code here
    return


@app.route('/user/logout', methods=['POST/GET'])
def user_logout():  # put application's code here
    return


@app.route('/user/restore', methods=['POST'])
def user_restore():  # put application's code here
    return


@app.route('/user/orders', methods=['GET'])
def user_orders_history():  # put application's code here
    return


@app.route('/user/orders/<order_id>', methods=['GET'])
def user_order(order_id: int):  # put application's code here
    return


@app.route('/user/address', methods=['GET', 'POST'])
def user_addresses_list():  # put application's code here
    return


@app.route('/user/address/<address_id>', methods=['GET', 'PUT', 'DELETE'])
def user_addresses(address_id: int):  # put application's code here
    return


@app.route('/menu', methods=['GET'])
def menu():  # put application's code here
    return


@app.route('/menu/<cat_name>', methods=['GET'])
def menu_cat_name(cat_name: string):  # put application's code here
    return


@app.route('/menu/<cat_name>/<dish>', methods=['GET'])
def menu_cat_name_dish(cat_name: string, dish: string):  # put application's code here
    return


@app.route('/menu/<cat_name>/<dish>/review', methods=['POST'])
def menu_cat_name_dish_review(cat_name: string, dish: string,):  # put application's code here
    return


@app.route('/menu/search', methods=['GET/POST'])
def menu_search():  # put application's code here
    return


if __name__ == '__main__':
    app.run()
