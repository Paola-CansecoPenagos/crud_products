from abc import ABC, abstractmethod
from app.core.product import Product

class ProductRepository(ABC):

    @abstractmethod
    def save_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def update_product(self, product_id: str, data: dict) -> None:
        pass

    @abstractmethod
    def delete_product(self, product_id: str) -> None:
        pass
