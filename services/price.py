import math

from repositories.product import ProductRepository
from repositories.image import ImageRepository
from repositories.price import PriceRepository
from entities.product import ProductEntity
from entities.image import ImageEntity
from entities.price import PriceEntity


class PriceService:

    @classmethod
    def update(cls):
        # clear by supplier
        PriceRepository.clear_price_by_supplier(supplier='АЙТИ')

        # get products count
        products_count = ProductRepository.get_active_products_count()

        # get products list
        offset = 0
        limit = 10000
        steps = math.ceil(products_count / limit)

        for step in range(steps):
            offset = limit*step
            product_entities = ProductRepository.get_products(limit=limit, offset=offset)

            price_entities = [PriceEntity(
                _article=product_entity.part, 
                _kod=product_entity.sku, 
                _name=product_entity.name, 
                _cena=product_entity.price, 
                _valuta='RUB', 
                _nalichie=product_entity.quantity, 
                _postavchik='АЙТИ', 
                _img=product_entity.url, 
            ) for product_entity in product_entities]

            # create
            PriceRepository.create(price_entities=price_entities)