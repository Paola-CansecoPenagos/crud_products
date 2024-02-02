from app.core.product_repository import ProductRepository
from app.adapters.product_adapter import ProductAdapter
from typing import List
from app.core.product import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
    
    def get_all_products(self) -> List[Product]:
        return self.product_repository.get_all_products()

    def get_product(self, product_id: str) -> Product:
        return self.product_repository.get_product(product_id)
    
    def create_product(self, data: dict) -> None:
        product = ProductAdapter.to_entity(data)
        self.product_repository.save_product(product)

    def update_product(self, product_id: str, data: dict) -> None:
        self.product_repository.update_product(product_id, data)

    def delete_product(self, product_id: str) -> None:
        self.product_repository.delete_product(product_id)
