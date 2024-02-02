from pymongo import MongoClient
from app.core.product_repository import ProductRepository
from app.core.product import Product
from app.adapters.product_adapter import ProductAdapter
from bson import ObjectId
from typing import List
from config import MONGO_URI, MONGO_DB_NAME


class MongoProductRepository(ProductRepository):
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB_NAME]
        self.collection = self.db['products']
        
    def get_all_products(self) -> List[Product]:
        product_data = list(self.collection.find())
        return [ProductAdapter.to_entity(data) for data in product_data]
        
    def get_product(self, product_id: str) -> Product:
        product_id_obj = ObjectId(product_id)
        product_data = self.collection.find_one({'_id': product_id_obj})
        return ProductAdapter.to_entity(product_data) if product_data else None

    def save_product(self, product: Product) -> None:
        product_data = ProductAdapter.to_dict(product)
        self.collection.insert_one(product_data)

    def update_product(self, product_id: str, data: dict) -> None:
        product_id_obj = ObjectId(product_id)
        self.collection.update_one({'_id': product_id_obj}, {'$set': data})

    def delete_product(self, product_id: str) -> None:
        product_id_obj = ObjectId(product_id)
        self.collection.delete_one({'_id': product_id_obj})
