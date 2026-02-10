from src.category import BaseCategory


class Order(BaseCategory):
    """Класс для представления заказов"""

    def __init__(self, product, quantity: int):
        """Метод для инициализации экземпляра класса"""
        super().__init__(name=f"Заказ: {product.name}",
                         description=f"Заказ товара: {product.description}")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        """Строковое представление заказа"""
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."

    def __len__(self):
        """Возвращает количество товаров в заказе"""
        return self.quantity
