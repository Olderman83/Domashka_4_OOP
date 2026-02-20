import pytest

from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category."""

    @pytest.fixture
    def sample_product(self):
        """Фикстура для создания тестового продукта"""
        return Product("Телефон", "Смартфон", 50000.0, 10)

    @pytest.fixture
    def sample_category(self, sample_product):
        """Фикстура для создания тестовой категории"""
        return Category("Электроника", "Электронные товары", [sample_product])

    def test_category_initialization(self, sample_category):
        """Тест инициализации категории"""
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Электронные товары"
        assert len(sample_category) == 1

    def test_add_product(self, sample_category, sample_product):
        """Тест добавления продукта в категорию"""
        new_product = Product("Ноутбук", "Игровой", 150000.0, 5)

        sample_category.add_product(new_product)
        assert len(sample_category) == 2

    def test_add_invalid_product(self, sample_category):
        """Тест добавления некорректного объекта"""
        with pytest.raises(
            TypeError, match="Можно добавлять только объекты класса Product"
        ):
            sample_category.add_product("не продукт")

    def test_str_method(self, sample_category):
        """Тест метода __str__"""
        str_result = str(sample_category)
        assert "Электроника" in str_result
        assert "количество продуктов" in str_result.lower()

    def test_add_product_to_category(self):
        """Тест добавления продукта в категорию"""
        category = Category("Категория", "Описание", [])
        product = Product("Продукт", "Описание", 100.0, 5)

        category.add_product(product)
        assert len(category) == 1

    def test_middle_price_with_products(self):
        """Тест метода middle_price с несколькими товарами"""
        product1 = Product("Товар 1", "Описание 1", 100.0, 5)
        product2 = Product("Товар 2", "Описание 2", 200.0, 3)
        product3 = Product("Товар 3", "Описание 3", 300.0, 7)

        category = Category(
            "Тестовая категория", "Описание", [product1, product2, product3]
        )

        expected_middle_price = (100.0 + 200.0 + 300.0) / 3
        assert category.middle_price() == expected_middle_price

    def test_middle_price_with_one_product(self):
        """Тест метода middle_price с одним товаром"""
        product = Product("Товар", "Описание", 150.0, 10)
        category = Category("Тестовая категория", "Описание", [product])

        assert category.middle_price() == 150.0

    def test_middle_price_with_empty_category(self):
        """Тест метода middle_price с пустой категорией"""
        category = Category("Пустая категория", "Описание", [])

        assert category.middle_price() == 0

    def test_middle_price_after_adding_products(self):
        """Тест метода middle_price после добавления товаров"""
        category = Category("Тестовая категория", "Описание", [])
        assert category.middle_price() == 0

        product1 = Product("Товар 1", "Описание 1", 100.0, 5)
        category.add_product(product1)
        assert category.middle_price() == 100.0

        product2 = Product("Товар 2", "Описание 2", 200.0, 3)
        category.add_product(product2)
        assert category.middle_price() == 150.0
