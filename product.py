class NegativeNumberError(Exception):
    """Ошибка невозможности использования отрицательного числа."""
    
    pass


class StatusError(Exception):
    """Ошибка статуса товара."""
    
    pass


class NameError(Exception):
    """Ошибка пустого названия товара."""

    pass


class Product:
    """Класс товара."""
    
    def __init__(self) -> None:
        """Инициализация конструктора класса."""
        
        self.name = 'Не указано'
        self.quantity = 0
        self.status = 'В пути'
        self.supplier = 'Не указан'
        self.developer = 'Не указан'
        self.price = None
        self.location = 'Не указано'
        self.color = 'Не указан'
        self.characteristics = 'Не указаны'
        self.description = 'Не указано'
        self.weight = None
        
    def get_name(self) -> str:
        """Геттер для названия.
        
        Returns:
            name: Название
        """

        return self.name
    
    def get_info(self) -> None:
        """Получение общей информации о товаре."""
        
        for key, value in self.__dict__.items():
            print(f'{key}: {value}')
        
    def set_name(self, new_name: str) -> None:
        """Сеттер для названия.
        
        Args:
            new_name: Новое название
        """
        if len(new_name.strip()) == 0:
            raise NameError('Название товара не может быть пустым')
        else:
            self.name = new_name
    
    def set_quantity(self, new_quantity: int) -> None:
        """Сеттер для количества.
        
        Args:
            new_quantity: Новое количество
        """
        
        if new_quantity < 0:
            raise NegativeNumberError('Количество не может быть отрицательным!')
        else:
            self.quantity = new_quantity
    
    def set_status(self, new_status: str) -> None:
        """Сеттер для статуса товара.
        
        Args:
            new_status: Новый статус товара.
        """
        
        if self.status == new_status:                
            raise StatusError('Нельзя присвоить товару уже имеющийся статус!')
        elif self.status != 'В пути' and new_status != 'Списан':
            self.status = new_status
        else:
            raise StatusError('Списать товар можно лишь тогда, когда он имеет статус "В наличии"!')
    
    def set_supplier(self, new_supplier: str) -> None:
        """Сеттер для поставщика.
        
        Args:
            new_supplier: Поставщик
        """
        
        self.supplier = new_supplier
    
    def set_developer(self, new_developer: str) -> None:
        """Сеттер для производителя.
        
        Args:
           new_developer: Производитель
        """
        
        self.developer = new_developer
    
    def set_price(self, new_price: float) -> None:
        """Сеттер для цены.
        
        Args:
            new_price: Цена
        """
        
        if new_price > 0:
            self.price = new_price
        else:
            raise NegativeNumberError('Стоимость товара всегда больше нуля!')
    
    def set_location(self, new_location: str) -> None:
        """Сеттер для местоположения.
        
        Args:
            new_location: Местоположение
        """
        
        self.location = new_location
    
    def set_color(self, new_color: str) -> None:
        """Сеттер для цвета.
        
        Args:
            new_color: Цвет
        """
        
        self.color = new_color
    
    def set_characteristics(self, new_characteristics: str) -> None:
        """Сеттер для характеристик.
        
        Args:
            new_characteristics: Характеристики
        """
        
        self.characteristics = new_characteristics
    
    def set_description(self, new_description: str) -> None:
        """Сеттер для описания.
        
        Args:
            new_description: Описание
        """
        
        self.description = new_description
    
    def set_weight(self, new_weight: float) -> None:
        """Сеттер для массы.
        
        Args:
            new_weight: Масса
        """
        
        if new_weight > 0:
            self.weight = new_weight
        else:
            raise NegativeNumberError('Масса не может быть отрицательной!')
