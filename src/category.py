class Category:
    """Класс для представления категорий"""
    category_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count +=1

    @property
    def product_count(self) -> int:
        """Возвращает количество товаров в конкретной категории."""
        return len(self.products)
