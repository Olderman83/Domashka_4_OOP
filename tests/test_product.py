import pytest
from src.product import Product, Smartphone, LawnGrass


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product("Test", "Description", 1000.0, 5)
        assert product.name == "Test"
        assert product.description == "Description"
        assert product.price == 1000.0
        assert product.quantity == 5

    def test_price_getter(self):
        """Тест геттера цены"""
        product = Product("Test", "Description", 1500.0, 3)
        assert product.price == 1500.0

    def test_price_setter_valid(self, capsys):
        """Тест сеттера цены с корректным значением"""
        product = Product("Test", "Description", 1000.0, 5)
        product.price = 2000.0
        assert product.price == 2000.0

    def test_product_add_method(self):
        """Тест метода сложения продуктов (__add__)"""
        product1 = Product("Товар1", "Описание1", 100.0, 5)
        product2 = Product("Товар2", "Описание2", 200.0, 3)

        total_value = product1 + product2
        assert total_value == 1100.0

    def test_product_addition_same_type(self):
        """Тест сложения продуктов одного типа"""
        product1 = Product("Продукт 1", "Описание", 100.0, 5)
        product2 = Product("Продукт 2", "Описание", 200.0, 3)
        assert product1 + product2 == 100.0 * 5 + 200.0 * 3

    def test_smartphone_addition(self):
        """Тест сложения смартфонов"""
        smartphone1 = Smartphone("Samsung", "Описание", 100000.0, 2,
                                 95.5, "S23", 256, "Черный")
        smartphone2 = Smartphone("iPhone", "Описание", 150000.0, 3,
                                 98.2, "15", 512, "Серый")
        assert smartphone1 + smartphone2 == 100000.0 * 2 + 150000.0 * 3

    def test_lawn_grass_addition(self):
        """Тест сложения газонной травы"""
        grass1 = LawnGrass("Трава 1", "Описание", 500.0, 10,
                           "Россия", "7 дней", "Зеленый")
        grass2 = LawnGrass("Трава 2", "Описание", 600.0, 5,
                           "США", "5 дней", "Темно-зеленый")
        assert grass1 + grass2 == 500.0 * 10 + 600.0 * 5
