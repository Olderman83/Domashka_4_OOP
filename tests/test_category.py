import pytest
from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category."""

    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми товарами."""
        return [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3),
            Product("Product 3", "Desc 3", 300.0, 7)
        ]

    @pytest.fixture
    def sample_category(self, sample_products):
        """Фикстура с тестовой категорией."""
        return Category(
            name="Test Category",
            description="Test Description",
            products=sample_products)

    def test_category_initialization(self, sample_category, sample_products):
        """Тест корректной инициализации объекта Category."""
        assert sample_category.name == "Test Category"
        assert sample_category.description == "Test Description"
        assert sample_category.products == sample_products

    def test_category_attributes_types(self, sample_category):
        """Тест типов атрибутов объекта Category."""
        assert isinstance(sample_category.name, str)
        assert isinstance(sample_category.description, str)
        assert isinstance(sample_category.products, list)

    def test_category_count(self, sample_products):
        """Тест подсчета количества категорий."""
        # Сбрасываем счетчик для чистого теста
        Category.category_count = 0
        Category.product_count = 0

        Category("Cat1", "Desc1", sample_products[:2])
        assert Category.category_count == 1

        Category("Cat2", "Desc2", sample_products[2:])
        assert Category.category_count == 2

    def test_product_count(self, sample_products):
        """Тест подсчета общего количества продуктов."""
        # Сбрасываем счетчик для чистого теста
        Category.category_count = 0
        Category.product_count = 0

        Category("Cat1", "Desc1", sample_products[:2])
        assert Category.product_count == 2

        Category("Cat2", "Desc2", sample_products[2:])
        assert Category.product_count == 3
