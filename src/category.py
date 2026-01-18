from src.product import Product


class Category:
    """Класс для представления категорий"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __len__(self):
        """Возвращает количество товаров в категории."""
        return len(self.__products)

    @property
    def products(self):
        """Геттер для отображения товаров в заданном формате"""
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return result

    def add_product(self, product: Product):
        """Метод для добавления товара в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")
