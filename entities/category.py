class CategoryEntity:
    """Category entity"""

    __slots__ = (
        'id',
        'name',
        'parent_id',
    )

    def __init__(self, _id: int, _name: str, _parent_id: int = None):
        """
        Конструктор
        Args:
            _id: ID
            _name: Название
            _parent_id: Родитель
        """
        self.id = _id
        self.name = _name
        self.parent_id = _parent_id
