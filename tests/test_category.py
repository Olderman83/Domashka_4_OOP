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
