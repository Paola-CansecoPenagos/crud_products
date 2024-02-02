from app.core.product import Product

class ProductAdapter:
    @staticmethod
    def to_dict(product: Product):
        if isinstance(product, Product):
            return {
                'name': product.name,
                'price': float(product.price),
                'stock': int(product.stock),
                'category': product.category,
                'ratings': float(product.ratings) if product.ratings is not None else None,
            }
        elif isinstance(product, list):
            return [ProductAdapter.to_dict(item) for item in product]
        elif isinstance(product, dict):
            return {key: ProductAdapter.to_dict(value) for key, value in product.items()}
        else:
            return product

    @staticmethod
    def to_entity(data):
        return Product(
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            category=data['category'],
            ratings=data['ratings']
        )
