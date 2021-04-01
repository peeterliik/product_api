# product_api
Flask REST API for a fictional Sports Equipment Shop

This API uses a local test data of products.

Running on http://127.0.0.1:5000/

#List of the product cataloge:
GET /api/v1/resources/products/all

#List of all categories:
GET /api/v1/resources/products/all_categories

#List of products of the concrete category:
GET /api/v1/resources/products/<string:category>

#Create category
POST /api/v1/resources/products/<string:category>

#Delete category
DELETE /api/v1/resources/products/<string:category>

#Update category
PUT /api/v1/resources/products/<string:category>/<string:new_category>

#Create product (and category)
POST /api/v1/resources/products/<string:category>/<string:product>

#Delete product
DELETE /api/v1/resources/products/<string:category>/<string:product>

#Update product
PUT /api/v1/resources/products/<string:category>/<string:product>/<string:new_product>

