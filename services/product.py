import pydash

from api.product import ProductApi
from api.catalog import CatalogApi
from repositories.product import ProductRepository
from entities.product import ProductEntity

from utils.db.connection import get_connection
from settings import IT_PARTNET_LOGIN, IT_PARTNET_PASSWORD

class ProductService:

    @classmethod
    def save(cls, products):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                counter = 0

                for product in products:
                    product_sku = product.get('sku')
                    product_name = product.get('name')
                    product_part = product.get('part')
                    product_vendor = product.get('vendor')
                    product_volume = product.get('volume')
                    product_has_image = product.get('has_image', False)
                    product_weight = product.get('weight')
                    product_min_quantity = product.get('min_qty')
                    product_category_id = product.get('category')
                    product_description = product.get('description')

                    if product_sku:
                        product_entity = ProductEntity(
                            _sku=product_sku,
                            _name=product_name,
                            _part=product_part,
                            _vendor=product_vendor,
                            _volume=product_volume,
                            _has_image=product_has_image,
                            _weight=product_weight,
                            _min_quantity=product_min_quantity,
                            _category_id=product_category_id,
                            _description=product_description,
                        )
                        product_row_id = ProductRepository.update_or_create(cursor=cursor, product_entity=product_entity)

                    counter += 1
                    if counter == 15000:
                        connection.commit()
                        counter = 0
                
                if counter != 0:
                    connection.commit()
                
        finally:
            if connection:
                connection.close()

    @classmethod
    def save_active(cls, products):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                counter = 0

                for product in products:
                    product_sku = product.get('sku')
                    product_price = product.get('price')
                    product_quantity = product.get('qty')

                    if product_sku:
                        product_entity = ProductEntity(
                            _sku=product_sku,
                            _price=product_price,
                            _quantity=product_quantity,
                        )
                        product_row_id = ProductRepository.update_partially(cursor=cursor, product_entity=product_entity)

                    counter += 1
                    if counter == 15000:
                        connection.commit()
                        counter = 0
                
                if counter != 0:
                    connection.commit()
                
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_or_create(cls):
        # mark all previous data as deleted
        ProductRepository.mark_all_as_deleted()

        # get data
        products = ProductApi.get_all()

        # parse and save
        cls.save(products)


    @classmethod
    def get_active_products(cls):
        # get session_id
        session_id = CatalogApi.auth(login=IT_PARTNET_LOGIN, password=IT_PARTNET_PASSWORD)

        # get products
        products = CatalogApi.get_active_products(session_id=session_id)

        # set is_active False 
        ProductRepository.mark_all_as_inactive()

        # save active
        cls.save_active(products)
