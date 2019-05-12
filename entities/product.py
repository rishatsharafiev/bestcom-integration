from decimal import Decimal


class ProductEntity:
    """Product entity"""

    __slots__ = (
        'name',
        'part',
        'sku',
        'vendor',
        'volume',
        'has_image',
        'weight',
        'price',
        'quantity',
        'min_quantity',
        'category_id',
        'description',
    )

    def __init__(
        self,
        _name: str = None, 
        _part: str = None, 
        _sku: int = None, 
        _vendor: str = None, 
        _volume: Decimal = None,
        _has_image: bool = False, 
        _weight: Decimal = None,
        _price: Decimal = None,
        _quantity: str = None,
        _min_quantity: int = None,
        _category_id: int = None,
        _description: str = None,
    ):
        """
        Конструктор
        Args:
            _name: Наименование
            _part: Партномер
            _sku: Артикул
            _vendor: Вендор
            _volume: Объем
            _has_image: Обозначает есть ли у товара изображения для скачивания
            _weight: Вес
            _price: Цена
            _quantity: Кол-во
            _min_quantity: Минимальное кол-во
            _category_id: ID категории
            _description: Описание
        """
        self.name = _name
        self.part = _part
        self.sku = _sku
        self.vendor = _vendor
        self.volume = _volume
        self.has_image = _has_image
        self.weight = _weight
        self.price = _price
        self.quantity = _quantity
        self.min_quantity = _min_quantity
        self.category_id = _category_id
        self.description = _description
