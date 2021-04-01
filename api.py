import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Test data
products = {'cycling': ['helmet','bike','wheels'],
            'skiing': ['skis','poles'],
            'running':['shoes','t-shirt','socks'],
            'swimming':['bathing suits','swimming cap']}



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sports Equipment Shop</h1>
<p>An API for a test project.</p>'''


@app.route('/api/v1/resources/products/all', methods=['GET'])
def api_all():
    return jsonify(products)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/products/all_categories', methods=['GET'])
def api_all_categories():
    results=list(products.keys())
    return jsonify(results)


@app.route('/api/v1/resources/products/<string:category>', methods=['GET', 'POST', 'DELETE'])
def api_category(category):
    if request.method=="GET":
        if category in products.keys():
            results = products[category]
            return jsonify(results)
        else:
            return page_not_found(404)
    elif request.method=="POST":
        products[category]=[]
    elif request.method=="DELETE":
        if category not in products.keys():
            return page_not_found(404)
        else:
            del products[category]
    return jsonify(products)


@app.route('/api/v1/resources/products/<string:category>/<string:product>', methods=['POST', 'DELETE'])
def api_product(category, product):
    if request.method=="POST":
        if category in products.keys():
            category_products=products[category]
            if product in category_products:
                return "Product already in category."
            else:
                category_products.append(product)
                products[category]=category_products
        else:
            new_category={category:[product]}
            products.update(new_category)
    elif request.method=="DELETE":
        if category not in products.keys():
            return page_not_found(404)
        category_products=products[category]
        if product not in category_products:
            return page_not_found(404)
        else:
            category_products.remove(product)
            products[category]=category_products
    return jsonify(products)

@app.route('/api/v1/resources/products/<string:category>/<string:new_category>', methods=['PUT'])
def api_update_category(category,new_category):
    if category not in products.keys():
        return page_not_found(404)
    else:
        products[new_category]=products.pop(category)
    return jsonify(products)

@app.route('/api/v1/resources/products/<string:category>/<string:product>/<string:new_product>', methods=['PUT'])
def api_update_product(category, product, new_product):
    if category not in products.keys():
        return page_not_found(404)
    category_products=products[category]
    if product not in category_products:
        return page_not_found(404)
    else:
        category_products[category_products.index(product)]=new_product
        products[category]=category_products
    return jsonify(products)

app.run()