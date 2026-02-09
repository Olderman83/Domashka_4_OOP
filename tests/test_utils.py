import pytest
import json
from unittest.mock import mock_open, patch

from src.utils import load_categories_from_json
from src.category import Category


class TestLoadCategoriesFromJson:
    """Тесты для функций в utils.py"""

    @pytest.fixture
    def sample_category_data(self):
        """Фикстура с тестовыми данными категорий"""
        return [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации...",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5
                    }
                ]
            }
        ]

    @pytest.fixture
    def sample_json_content(self, sample_category_data):
        """Фикстура с JSON-контентом"""
        return json.dumps(sample_category_data, ensure_ascii=False)

    def test_load_categories_from_json_success(self, sample_json_content):
        """Тест успешной загрузки категорий из JSON файла"""
        # Мокаем open и json.load
        with patch('builtins.open', mock_open(read_data=sample_json_content)) as mock_file, \
                patch('json.load') as mock_json_load:
            # Настраиваем mock для json.load
            mock_json_load.return_value = json.loads(sample_json_content)

            # Вызываем тестируемую функцию
            categories = load_categories_from_json('dummy/path.json')

            # Проверяем, что файл был открыт с правильными параметрами
            mock_file.assert_called_once_with('dummy/path.json', 'r', encoding='utf-8')

            # Проверяем результат
            assert len(categories) == 1
            assert isinstance(categories[0], Category)
            assert categories[0].name == "Смартфоны"
            assert len(categories[0]) == 1  # Используем __len__

    def test_json_decode_error(self):
        """Тест обработки некорректного JSON"""
        with patch("builtins.open", mock_open(read_data="invalid json content")):
            with pytest.raises(json.JSONDecodeError):
                load_categories_from_json("invalid.json")
