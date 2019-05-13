from decimal import Decimal


class PriceEntity:
    """Price entity"""

    __slots__ = (
        'article',
        'kod',
        'name',
        'cena',
        'valuta',
        'nalichie',
        'postavchik',
        'img',
    )

    def __init__(
        self,
        _article: str = None, 
        _kod: str = None, 
        _name: str = None, 
        _cena: Decimal = None, 
        _valuta: str = None,
        _nalichie: str = False, 
        _postavchik: str = None,
        _img: str = '',
    ):
        """
        Конструктор
        Args:
            _article: Артикул (part)
            _kod: Код (sku)
            _name: Название
            _cena: Цена
            _valuta: Валюта
            _nalichie: Наличие
            _postavchik: Поставщик
            _img: Картинка
        """
        self.article = _article
        self.kod = _kod
        self.name = _name
        self.cena = _cena
        self.valuta = _valuta
        self.nalichie = _nalichie
        self.postavchik = _postavchik
        self.img = _img
