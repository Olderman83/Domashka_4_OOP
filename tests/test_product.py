import pytest
from src.product import Product


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
