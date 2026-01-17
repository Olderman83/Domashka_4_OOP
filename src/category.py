from src.product import Product


class Category:
    """Класс для представления категорий"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __len__(self):
        """Возвращает количество товаров в категории."""
        return len(self.products)
