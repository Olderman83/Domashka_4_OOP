import pytest
from src.category import Category


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self):
        """Тест корректности инициализации объекта категории"""
        # Arrange
        name = "Электроника"
        description = "Технические устройства"
        products = ["Смартфон", "Ноутбук", "Планшет"]

        # Act
        category = Category(name, description, products)

        # Assert
        assert category.name == name
        assert category.description == description
        assert category.products == products

    def test_product_count_property(self):
        """Тест подсчета количества продуктов в категории"""
        # Arrange
        products_list = ["Смартфон", "Ноутбук", "Планшет", "Наушники"]
        category = Category("Электроника", "Техника", products_list)

        # Act
        count = category.product_count

        # Assert
        assert count == 4
        assert category.product_count == len(products_list)

    def test_category_counter_increment(self):
        """Тест подсчета количества созданных категорий"""
        # Arrange
        initial_count = Category.category_count

        # Act - создаем несколько категорий
        category1 = Category("Одежда", "Модная одежда", ["Футболка", "Джинсы"])
        category2 = Category("Обувь", "Обувные изделия", ["Кроссовки", "Туфли"])
        category3 = Category("Аксессуары", "Дополнительные товары", ["Ремень", "Часы"])

        # Assert
        assert Category.category_count == initial_count + 3
        assert category1.category_count == category2.category_count == category3.category_count