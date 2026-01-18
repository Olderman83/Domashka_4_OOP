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
        return Category(
            "Электроника",
            "Электронные товары",
            [sample_product]
        )

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

    def test_multiple_products_display(self):
        """Тест отображения нескольких продуктов"""
        product1 = Product("Товар 1", "Описание 1", 1000.0, 5)
        product2 = Product("Товар 2", "Описание 2", 2000.0, 10)
        product3 = Product("Товар 3", "Описание 3", 3000.0, 15)

        category = Category("Категория", "Описание", [product1, product2, product3])

        products_str = category.products

        expected = [
            "Товар 1, 1000.0 руб. Остаток: 5 шт.\n",
            "Товар 2, 2000.0 руб. Остаток: 10 шт.\n",
            "Товар 3, 3000.0 руб. Остаток: 15 шт.\n"
        ]
        assert products_str == expected

    def test_add_invalid_product(self, sample_category):
        """Тест добавления некорректного объекта"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
            sample_category.add_product("не продукт")