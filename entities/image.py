class ImageEntity:
    """Image entity"""

    __slots__ = (
        'id',
        'url',
        'sku',
    )

    def __init__(self, _id: int = None, _url: str = None, _sku: int = None):
        """
        Конструктор
        Args:
            _id: ID
            _url: Адрес
            _sku: Артикул
        """
        self.id = _id
        self.url = _url
        self.sku = _sku
