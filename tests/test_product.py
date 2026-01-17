import pytest
from src.product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization_valid_values(self):
        """Тест корректной инициализации объекта с валидными значениями"""
        # Arrange
        name = "Телефон"
        description = "Смартфон с хорошей камерой"
        price = 50000.0
        quantity = 10

        # Act
        product = Product(name, description, price, quantity)

        # Assert
        assert product.name == name
        assert product.description == description
        assert product.price == price
        assert product.quantity == quantity

    def test_product_initialization_zero_price(self):
        """Тест инициализации объекта с нулевой ценой"""
        # Arrange
        name = "Бесплатный образец"
        description = "Тестовый продукт"
        price = 0.0
        quantity = 100

        # Act
        product = Product(name, description, price, quantity)

        # Assert
        assert product.price == 0.0
        assert product.quantity == quantity
