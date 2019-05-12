from api.product import ProductApi
from repositories.product import ProductRepository
from entities.product import ProductEntity

from utils.db.connection import get_connection


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
                    if counter == 20000:
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
