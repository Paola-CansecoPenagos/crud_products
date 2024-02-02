from flask import Flask, request, jsonify
from app.core.product_service import ProductService
from app.adapters.product_adapter import ProductAdapter
from app.infrastructure.mongo_repository import MongoProductRepository

app = Flask(__name__)

product_service = ProductService(MongoProductRepository())

@app.route('/api/products', methods=['GET'])
def get_all_products():
    products = product_service.get_all_products()
    return jsonify([ProductAdapter.to_dict(product) for product in products]), 200

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    if product:
        return jsonify(ProductAdapter.to_dict(product)), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_service.create_product(data)
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/api/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product_service.update_product(product_id, data)
    return jsonify({'message': 'Product updated successfully'})

@app.route('/api/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product_service.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
