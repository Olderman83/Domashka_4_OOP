import pytest

from src.product import LawnGrass, Product, Smartphone


class TestProduct:
    """Тесты для класса Product"""

    # ... (существующие тесты остаются без изменений) ...

    def test_product_creation_with_zero_quantity_raises_value_error(self):
        """Тест: создание продукта с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Test", "Description", 1000.0, 0)

        assert (
            str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        )

    def test_product_creation_with_negative_quantity_raises_value_error(self):
        """Тест: создание продукта с отрицательным количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Test", "Description", 1000.0, -5)

        assert (
            str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        )

    def test_product_creation_with_positive_quantity_success(self):
        """Тест: создание продукта с положительным количеством проходит успешно"""
        product = Product("Test", "Description", 1000.0, 5)
        assert product.quantity == 5

    def test_smartphone_creation_with_zero_quantity_raises_value_error(self):
        """Тест: создание смартфона с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Smartphone("Samsung", "Описание", 100000.0, 0, 95.5, "S23", 256, "Черный")

        assert (
            str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        )

    def test_lawn_grass_creation_with_zero_quantity_raises_value_error(self):
        """Тест: создание газонной травы с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError) as exc_info:
            LawnGrass("Трава", "Описание", 500.0, 0, "Россия", "7 дней", "Зеленый")

        assert (
            str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        )

    def test_new_product_classmethod_with_zero_quantity(self):
        """Тест: создание продукта через new_product с нулевым количеством вызывает ValueError"""
        product_data = {
            "name": "Test",
            "description": "Description",
            "price": 1000.0,
            "quantity": 0,
        }

        with pytest.raises(ValueError) as exc_info:
            Product.new_product(product_data)

        assert (
            str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        )
