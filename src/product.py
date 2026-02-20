from abc import ABC, abstractmethod


class ReprMixin:
    """Миксин для отображения информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект {self.__class__.__name__} с параметрами: {self.__repr__()}"
        )


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float):
        pass


class Product(ReprMixin, BaseProduct):
    """Класс для представления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        """Представление объекта для отладки"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        """Метод сложения продуктов из одинаковых классов"""
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)

        raise TypeError(
            f"Нельзя складывать {self.__class__.__name__} и {other.__class__.__name__} товары разных категорий."
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        descriptions: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, descriptions, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity},"
            f" {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"
        )

    def __str__(self):
        return f"{super().__str__()}, Модель: {self.model}, Память: {self.memory}GB"


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
            f"'{self.country}', '{self.germination_period}', '{self.color}')"
        )

    def __str__(self):
        return f"{super().__str__()}, Страна: {self.country}, Срок прорастания: {self.germination_period}"
